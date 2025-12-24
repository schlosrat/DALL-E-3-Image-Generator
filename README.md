# DALL-E 3 Image Studio
A lightweight Python-based desktop application that provides a graphical user interface (GUI) for generating images using OpenAI's DALL-E 3 model. This tool allows users to customize image quality, aspect ratio, manage session history, and save high-resolution images locally.

## Features
Customizable Generation: Toggle between Standard and HD quality.

Multiple Aspect Ratios: Support for Square (1:1), Portrait (9:16), and Landscape (16:9).

Session History: Automatically tracks prompts and images generated during the current session.

Local Saving: Save high-resolution PNG files directly to your computer.

Real-time Feedback: Includes an indeterminate progress bar and status updates during the generation process.

## Prerequisites
1. Install Python
Ensure you have Python 3.8 or higher installed.

Windows/macOS: Download from python.org.

Linux: Use your package manager (e.g., sudo apt install python3).

2. OpenAI API Key
You will need a valid API key from OpenAI. Ensure your account has a positive credit balance to avoid "billing limit" errors.

## Setup Instructions
1. Create a Virtual Environment
It is recommended to use a virtual environment to manage dependencies.

### Windows:
Bash
```
python -m venv venv
venv\Scripts\activate
```
### Linux / macOS:
Bash
```
python3 -m venv venv
source venv/bin/activate
```
2. Install Dependencies
Install the required libraries using pip:

Bash
```
pip install openai pillow requests
```
## Running the Application
Execute the code from your command prompt:

### Windows:
From a CMD window
Bash
```
python main.py
```

### Linux / macOS:
From a Terminal window
Bash
```
python3 main.py
```
## Using the Interface
The GUI is divided into two main sections: Generation Controls (Left) and Session History (Right).

### Generation Controls
API Key: Enter your OpenAI Secret Key here. Characters are masked for security.

Size Pane: Choose between Standard (faster/cheaper) and HD (higher detail).

Aspect Ratio Pane: Select your desired output format (Square, Portrait, or Landscape).

Prompt: Enter a detailed description of the image you want to create.

Generate: Click to start. The Progress Bar will indicate active generation.

Save Current: Saves the currently displayed image as a PNG file.

### Session History
History List: Every successful generation is added here. Clicking an entry reloads that image and its original prompt.

Clear History: Permanently removes all entries from the current session.

## License
This project is licensed under the MIT License.

Copyright (c) 2024

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.