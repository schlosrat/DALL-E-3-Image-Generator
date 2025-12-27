import tkinter as tk
from tkinter import messagebox, filedialog, ttk
import threading
import requests
from io import BytesIO
from PIL import Image, ImageTk
from openai import OpenAI

class DalleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("DALL-E 3 Studio")
        self.root.geometry("1150x950")

        self.history = []
        self.current_img_data = None
        self.quality_var = tk.StringVar(value="standard")
        self.size_var = tk.StringVar(value="1024x1024")
        self.style_var = tk.StringVar(value="")

        self.paned = tk.PanedWindow(root, orient="horizontal", sashwidth=4)
        self.paned.pack(fill="both", expand=True)

        # LEFT SIDE: Controls
        left_frame = tk.Frame(self.paned, padx=20, pady=10)
        self.paned.add(left_frame, width=700)

        tk.Label(left_frame, text="OpenAI API Key:", font=("Arial", 10, "bold")).pack(anchor="w")
        self.api_entry = tk.Entry(left_frame, width=60, show="*")
        self.api_entry.pack(fill="x", pady=(0, 10))

        # --- SETTINGS PANES ---
        settings_container = tk.Frame(left_frame)
        settings_container.pack(fill="x", pady=5)

        size_pane = tk.LabelFrame(settings_container, text="Quality", padx=10, pady=10)
        size_pane.pack(side="left", fill="both", expand=True, padx=(0, 5))
        ttk.Radiobutton(size_pane, text="Standard", variable=self.quality_var, value="standard").pack(side="left", padx=5)
        ttk.Radiobutton(size_pane, text="HD", variable=self.quality_var, value="hd").pack(side="left", padx=5)

        aspect_pane = tk.LabelFrame(settings_container, text="Aspect Ratio", padx=10, pady=10)
        aspect_pane.pack(side="left", fill="both", expand=True, padx=(5, 0))
        ttk.Radiobutton(aspect_pane, text="Square", variable=self.size_var, value="1024x1024").pack(side="left", padx=5)
        ttk.Radiobutton(aspect_pane, text="Portrait", variable=self.size_var, value="1024x1792").pack(side="left", padx=5)
        ttk.Radiobutton(aspect_pane, text="Landscape", variable=self.size_var, value="1792x1024").pack(side="left", padx=5)

        # --- ARTISTIC CONTROLS (Style Only) ---
        art_pane = tk.LabelFrame(left_frame, text="Artistic Controls", padx=10, pady=10)
        art_pane.pack(fill="x", pady=10)

        tk.Label(art_pane, text="In The Style Of:").grid(row=0, column=0, sticky="w")
        self.style_entry = tk.Entry(art_pane, textvariable=self.style_var)
        self.style_entry.grid(row=0, column=1, sticky="ew", padx=5)
        art_pane.columnconfigure(1, weight=1)

        # --- PROMPT INPUT WITH SCROLLBAR ---
        tk.Label(left_frame, text="Prompt:", font=("Arial", 10, "bold")).pack(anchor="w", pady=(10, 0))
        prompt_container = tk.Frame(left_frame)
        prompt_container.pack(fill="x", pady=5)
        
        self.prompt_text = tk.Text(prompt_container, height=4, wrap="word")
        self.prompt_scroll = tk.Scrollbar(prompt_container, command=self.prompt_text.yview)
        self.prompt_text.configure(yscrollcommand=self.prompt_scroll.set)
        
        self.prompt_scroll.pack(side="right", fill="y")
        self.prompt_text.pack(side="left", fill="x", expand=True)

        btn_frame = tk.Frame(left_frame)
        btn_frame.pack(fill="x")
        self.gen_button = tk.Button(btn_frame, text="Generate", command=self.on_generate_click, bg="#28a745", fg="white", width=15)
        self.gen_button.pack(side="left", padx=5)
        self.save_button = tk.Button(btn_frame, text="Save Current", command=self.save_image, bg="#007BFF", fg="white", width=15, state="disabled")
        self.save_button.pack(side="left", padx=5)

        self.progress = ttk.Progressbar(left_frame, mode="indeterminate")
        self.progress.pack(fill="x", pady=10)

        self.image_display = tk.Label(left_frame, bg="#333333", height=25)
        self.image_display.pack(fill="both", expand=True)

        # RIGHT SIDE: History
        right_frame = tk.Frame(self.paned, padx=10, pady=10, bg="#f8f9fa")
        self.paned.add(right_frame, width=400)

        tk.Label(right_frame, text="Session History", font=("Arial", 12, "bold"), bg="#f8f9fa").pack()
        self.history_listbox = tk.Listbox(right_frame, font=("Arial", 9))
        self.history_listbox.pack(fill="both", expand=True, pady=5)
        self.history_listbox.bind("<<ListboxSelect>>", self.on_history_select)

        tk.Label(right_frame, text="Selected Full Prompt:", font=("Arial", 9, "bold"), bg="#f8f9fa").pack(anchor="w")
        self.history_prompt_display = tk.Text(right_frame, height=6, bg="#e9ecef", wrap="word")
        self.history_prompt_display.pack(fill="x", pady=(0, 5))
        
        self.copy_to_input_btn = tk.Button(right_frame, text="Copy to Prompt Input", command=self.copy_history_to_input)
        self.copy_to_input_btn.pack(fill="x", pady=(0, 10))
        
        self.clear_button = tk.Button(right_frame, text="Clear History", command=self.clear_history, bg="#dc3545", fg="white")
        self.clear_button.pack(fill="x", pady=5)

    def handle_error(self, error_msg):
        self.progress.stop()
        self.gen_button.config(state="normal")
        messagebox.showerror("Error", error_msg)

    def on_generate_click(self):
        api_key = self.api_entry.get().strip()
        user_prompt = self.prompt_text.get("1.0", tk.END).strip()
        style_prefix = self.style_var.get().strip()
        
        if not api_key or not user_prompt: return

        full_prompt = f"{style_prefix} {user_prompt}".strip() if style_prefix else user_prompt
        self.gen_button.config(state="disabled")
        self.progress.start(10)
        
        # Pass both the full prompt (for the API) and original prompt (for the listbox)
        threading.Thread(target=self.generate_image, args=(api_key, full_prompt, user_prompt)).start()

    def generate_image(self, api_key, full_prompt, original_prompt):
        try:
            client = OpenAI(api_key=api_key)
            params = {
                "model": "dall-e-3", 
                "prompt": full_prompt, 
                "size": self.size_var.get(), 
                "quality": self.quality_var.get(), 
                "n": 1
            }

            response = client.images.generate(**params)
            raw_data = requests.get(response.data[0].url).content
            
            img = Image.open(BytesIO(raw_data))
            img.thumbnail((650, 500), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(img)

            # Store full_prompt for reproduction and original_prompt for display
            new_entry = {
                "full_prompt": full_prompt, 
                "original_prompt": original_prompt, 
                "photo": photo, 
                "raw": raw_data
            }
            self.history.insert(0, new_entry)
            self.root.after(0, self.update_ui_with_new, new_entry)
        except Exception as e:
            error_str = str(e)
            self.root.after(0, lambda: self.handle_error(error_str))

    def update_ui_with_new(self, entry):
        self.progress.stop()
        self.gen_button.config(state="normal")
        self.save_button.config(state="normal")
        
        # Omit the "In The Style Of" prefix by using only the original_prompt
        display_text = entry['original_prompt'][:35]
        self.history_listbox.insert(0, f"[{len(self.history)}] {display_text}...")
        self.display_entry(entry)

    def on_history_select(self, event):
        selection = self.history_listbox.curselection()
        if selection: self.display_entry(self.history[selection[0]])

    def display_entry(self, entry):
        self.image_display.config(image=entry["photo"])
        self.image_display.image = entry["photo"]
        self.current_img_data = entry["raw"]
        
        # Continue to show the full prompt in the read-only display for easy copying
        self.history_prompt_display.delete("1.0", tk.END)
        self.history_prompt_display.insert("1.0", entry["full_prompt"])

    def copy_history_to_input(self):
        text = self.history_prompt_display.get("1.0", tk.END).strip()
        if text:
            self.prompt_text.delete("1.0", tk.END)
            self.prompt_text.insert("1.0", text)
            self.style_var.set("")

    def clear_history(self):
        if messagebox.askyesno("Clear History", "Delete all generated images in this session?"):
            self.history.clear()
            self.history_listbox.delete(0, tk.END)
            self.image_display.config(image="", text="History Cleared")
            self.image_display.image = None
            self.history_prompt_display.delete("1.0", tk.END)
            self.save_button.config(state="disabled")

    def save_image(self):
        if not self.current_img_data: return
        path = filedialog.asksaveasfilename(defaultextension=".png")
        if path:
            with open(path, "wb") as f: f.write(self.current_img_data)

if __name__ == "__main__":
    root = tk.Tk()
    app = DalleApp(root)
    root.mainloop()