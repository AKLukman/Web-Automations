# Python + Playwright Environment Setup in VS Code

A simple guide to setting up a Python virtual environment and Playwright in **Visual Studio Code** on Windows, macOS, and Linux.

---

## 📋 Prerequisites

Before starting, make sure you have:

* [Python](https://www.python.org/downloads/) installed
* [Visual Studio Code](https://code.visualstudio.com/) installed
* Basic knowledge of Python and the VS Code terminal

---

## 🧩 1. Install VS Code Extensions

Open VS Code and install the following extensions:

| Extension           | Publisher | Purpose                                       |
| ------------------- | --------- | --------------------------------------------- |
| **Python**          | Microsoft | Python language support                       |
| **Pylance**         | Microsoft | IntelliSense, autocomplete, and type checking |
| **Python Debugger** | Microsoft | Python debugging support                      |

You can install them from:

**VS Code → Extensions → Search**

```text
Python
Pylance
Python Debugger
```

---

## 🐍 2. Create a Virtual Environment

Open the VS Code terminal and navigate to your project folder.

### Windows

```bash
py -m venv venv
```

If `py` is not available:

```bash
python -m venv venv
```

### macOS / Linux

```bash
python3 -m venv venv
```

This creates a virtual environment named `venv`.

---

## ⚡ 3. Activate the Virtual Environment

### Windows - Command Prompt

```cmd
venv\Scripts\activate
```

### Windows - PowerShell

```powershell
.\venv\Scripts\Activate.ps1
```

### macOS / Linux

```bash
source venv/bin/activate
```

After activation, you should see `(venv)` in your terminal.

Example:

```text
(venv) H:\Automations\Practice>
```

---

## 🎭 4. Install Playwright

Make sure the virtual environment is activated before installing Playwright.

### Windows / macOS / Linux

```bash
pip install playwright
```

### macOS / Linux

You can also use:

```bash
pip3 install playwright
```

Verify the installation:

```bash
pip show playwright
```

You should see information similar to:

```text
Name: playwright
Version: x.x.x
Location: .../venv/.../site-packages
```

---

## 🌐 5. Install Chromium

Playwright requires browser binaries to run browser automation.

Install Chromium with:

```bash
playwright install chromium
```

Or use:

```bash
python -m playwright install chromium
```

---

## ⚙️ 6. Select the Python Interpreter in VS Code

After creating your virtual environment, tell VS Code to use it.

### Steps

1. Press `Ctrl + Shift + P` on Windows/Linux or `Cmd + Shift + P` on macOS.
2. Search for:

   ```text
   Python: Select Interpreter
   ```
3. Select the Python interpreter inside your `venv`.

### Windows

```text
venv\Scripts\python.exe
```

### macOS / Linux

```text
venv/bin/python
```

> **Important:** Select the same virtual environment where you installed Playwright.

---

## 🧪 7. Test Playwright

Create a Python file:

```text
test_playwright.py
```

Add the following code:

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()

    page.goto("https://example.com")

    print(page.title())

    browser.close()
```

Run the script:

```bash
python test_playwright.py
```

If everything is configured correctly, the browser will launch and the page title will be printed in the terminal.

---

## 📁 Recommended Project Structure

Your project can look like this:

```text
Practice/
│
├── venv/
│
├── tests/
│   └── test_playwright.py
│
├── .gitignore
└── README.md
```

### `.gitignore`

If you're using GitHub, **do not commit your virtual environment**.

Create a `.gitignore` file:

```gitignore
# Virtual environment
venv/

# Python cache
__pycache__/
*.py[cod]

# VS Code
.vscode/

# Environment variables
.env
```

> You can choose to commit `.vscode/settings.json` if your project needs shared VS Code settings. Avoid committing personal or machine-specific settings.

---

## 🔍 Troubleshooting

### `Python was not found`

Try:

```bash
py --version
```

or:

```bash
python --version
```

If Python is installed but Windows opens the Microsoft Store, check:

**Settings → Apps → Advanced app settings → App execution aliases**

Disable the `python.exe` and `python3.exe` aliases if necessary.

---

### `Import "playwright.sync_api" could not be resolved`

First, make sure Playwright is installed:

```bash
pip show playwright
```

Then verify that VS Code is using your virtual environment:

**Ctrl + Shift + P → Python: Select Interpreter**

Select:

```text
venv\Scripts\python.exe
```

Then reload VS Code.

---

### Auto-completion is not working

Make sure these extensions are installed and enabled:

* Python
* Pylance

Then reload the VS Code window:

**Ctrl + Shift + P → Developer: Reload Window**

You can also manually trigger IntelliSense with:

```text
Ctrl + Space
```

---

## 🚀 Quick Setup

If Python is already installed, the basic setup is:

### Windows

```bash
py -m venv venv
venv\Scripts\activate
pip install playwright
playwright install chromium
```

### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
pip install playwright
playwright install chromium
```

Then select the `venv` interpreter in VS Code.

---

## ✅ Setup Checklist

* [ ] Python installed
* [ ] VS Code installed
* [ ] Python extension installed
* [ ] Pylance installed
* [ ] Python Debugger installed
* [ ] Virtual environment created
* [ ] Virtual environment activated
* [ ] Playwright installed
* [ ] Chromium installed
* [ ] VS Code interpreter set to `venv`
* [ ] Playwright test successfully executed

---

## 📚 Useful Resources

* [Python Documentation](https://docs.python.org/3/)
* [VS Code Python Documentation](https://code.visualstudio.com/docs/languages/python)
* [Playwright Python Documentation](https://playwright.dev/python/)
* [Playwright Python GitHub](https://github.com/microsoft/playwright-python)
