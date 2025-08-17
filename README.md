# 🖋 Multi-Clipboard Manager

A Python clipboard manager that lets you **store multiple clipboard entries** and paste them anywhere using **hotkeys**.  

---

## Features ✨

- 5 clipboard slots  
- Auto-clear after a timeout (default: 60s)  
- Paste with `Ctrl+Shift+1` … `Ctrl+Shift+5`  
- Lightweight & runs in the background  

---

## Installation & Execution ⚡

```bash
# Clone repo
git clone https://github.com/almostDaed04/Multiple_Clipboard_Manager.git
cd Multiple_Clipboard_Manager

# Create & activate virtual environment
python3 -m venv myenv
source myenv/bin/activate

# Install dependencies
pip install pyperclip
pip install keyboard

# Run the script (Linux users may need sudo for keyboard module)
sudo python multi_clipboard.py
