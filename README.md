# DALL-E 3 Studio
A lightweight Python-based desktop application that provides a graphical user interface (GUI) for generating images using OpenAI's DALL-E 3 model. This tool allows users to customize image quality, aspect ratio, manage session history, and save high-resolution images locally.

## Features
* **Customizable Generation:** Toggle between Standard and HD quality.
* **Multiple Aspect Ratios:** Support for Square (1:1), Portrait (9:16), and Landscape (16:9).
* **Session History:** Automatically tracks prompts and images generated during the current session.
* **Local Saving:** Save high-resolution PNG files directly to your computer.
* **Real-time Feedback:** Includes an indeterminate progress bar and status updates during the generation process.

## Prerequisites
1. Install Python: *Ensure you have Python 3.8 or higher installed.*

### Windows/macOS:
Download from [Python.org](https://python.org).

### Linux:
Use your package manager (e.g., sudo apt install python3).

2. OpenAI API Key

You will need a valid API key from OpenAI. Ensure your account has a positive credit balance to avoid "billing limit" errors.

This application requires an OpenAI API key to function. Using the API is often significantly more cost-effective than monthly subscriptions if you only generate a modest number of images per month. While subscriptions can cost $20+/month, DALL-E 3 API costs are pay-per-use, typically ranging from **$0.04 to $0.12** per image depending on quality and resolution. See the **Cost Estimation** section below for details. 

## How to obtain an OpenAI API key:

1. **Create an Account:** Visit the [OpenAI API Platform](https://platform.openai.com/) and sign up.
2. **Add Credits:** Navigate to **Settings > Billing** and add a small amount of credit (e.g., $5 or $10) to your account balance.
3. **Generate a Key:** Go to the API Keys section in your dashboard, click "Create new secret key", and copy it immediately. You can use this key immediately by pasting it into this application, or you can save it (securely) in a text file on your computer for later use.
    * *NOTE: Treat any OpenAI API Key you generate like a password in that anyone who has it can use the OpenAI API to create content using your funds.*
    * For security purposes, you may want to **Delete** the key from your OpenAI account once you're done using it for a session. Deleting a key doesn't impact your funds balance. You can always generate a new, fresh key anytime you need one. If you want to save the key on your computer for later reuse, it's recommended that you store it securely in a password manager or other similar tool.
6. **Set Limits:** To prevent unexpected charges, you can set a "Hard Limit" in **Settings > Limits** to cap your monthly spending. This is especially useful if you've configured OpenAI to automatically charge your card when your balance is low. Alternatively, you can configure your OpenAI API account to only refill your credits when you log in and do this manually.

## Setup Instructions
1. Create a Virtual Environment

*It is recommended to use a virtual environment to manage dependencies with any Python application.*

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

*Install the required libraries using pip:*

Bash
```
pip install openai pillow requests
```

## Running the Application
Execute the code from your command prompt:

### Windows:
Using a CMD window
Bash
```
python main.py
```

### Linux / macOS:
Using a Terminal window
Bash
```
python3 main.py
```
## Using the Interface
The GUI is divided into two main sections: Generation Controls (Left) and Session History (Right).

### Generation Controls
* **API Key:** Enter your OpenAI Secret Key here. Characters are masked for security.
* **Size Pane:** Choose between Standard (faster/cheaper) and HD (greater detail).
* **Aspect Ratio Pane:** Select your desired output format (Square, Portrait, or Landscape).
* **Prompt:** Enter a detailed description of the image you want to create.
* **Generate:** Click to start. The Progress Bar will indicate active generation.
* **Save Current:** Saves the currently displayed image as a PNG file.

### Session History
* **History List:** Every successful generation is added here. Clicking an entry reloads that image and its original prompt.
* **Clear History:** Permanently removes all entries from the current session.

## Cost Estimation

DALL-E 3 pricing is based on the image size and quality selected in the application. Below is a breakdown of the estimated cost per image generated as of late 2024:

| Aspect Ratio | Standard Quality | HD Quality |
| :--- | :--- | :--- |
| **Square (1024×1024)** | $0.040 / image | $0.080 / image |
| **Landscape (1792×1024)** | $0.080 / image | $0.120 / image |
| **Portrait (1024×1792)** | $0.080 / image | $0.120 / image |

### Why use the API?
For users who generate a few dozen images a month, the API is significantly cheaper than a flat-rate subscription.
* **API User**: 25 Standard Square images = **$1.00 total**.
* **Subscription User**: Flat monthly fee = **$20.00+ total**.

*Note: Pricing is set by OpenAI and is subject to change. You can always check your current spending in the [OpenAI Usage Dashboard](https://platform.openai.com/usage).*

## Security
Your privacy and the security of your credentials are a top priority. This application is designed to run entirely on your local machine with the following security principles:

* **Local Execution:** All application code executes solely on your local computer; no third-party servers (other than OpenAI) are involved in the generation process.

* **Credential Privacy:** Your OpenAI API Key is never stored, logged, or shared by this application. It is only held in active memory during your session to facilitate secure communication with OpenAI.

* **Encrypted Transmission:** All calls to the DALL-E API for image generation and retrieval are made over secure, encrypted HTTPS connections.

* **Data Sovereignty:** Your prompts and the resulting images remain on your local system. The application does not maintain an external database or "phone home" with your creative content.

* **No Hidden Persistence:** Once the application is closed, the session history—including your API key and prompts—is cleared from the system's active memory.

**Recommendation:** For maximum security, treat your API key like a password. Avoid hardcoding it into the source code and always use the masked input field provided in the GUI.

## License
This project is licensed under the MIT License.

Copyright (c) 2024

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
