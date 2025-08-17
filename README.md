# 🖋 Multi-Clipboard Manager

A Python clipboard manager that lets you **store multiple clipboard entries** and **paste them anywhere** using **hotkeys**.  

---

## Features ✨

- Store **5 clipboard slots**  
- Auto-clear clipboard slots after a **timeout** (default: 60s)  
- Paste any slot with **Ctrl+Shift+1 … Ctrl+Shift+5**  
- Lightweight, runs in the background  
- Works on Linux, Windows, and macOS  

---

## How It Works 🛠

The script constantly monitors your clipboard and keeps track of up to **5 recent entries**.  
Use the hotkeys to instantly paste any slot wherever your cursor is.  

---

## Requirements 📦

- **Python 3.8+**  
- Modules: `pyperclip`, `keyboard`  

> Linux users may require `sudo` to use the keyboard module.  

---

## Installation & Execution ⚡

```bash
# Clone the repository
git clone https://github.com/almostDaed04/Multiple_Clipboard_Manager.git
cd Multiple_Clipboard_Manager

# Create & activate a virtual environment
python3 -m venv myenv
source myenv/bin/activate  # Linux/macOS
myenv\Scripts\activate     # Windows

# Install dependencies
pip install pyperclip keyboard

# Run the script
sudo python multi_clipboard.py  # Linux (if hotkeys require root)
python multi_clipboard.py       # Windows/macOS
