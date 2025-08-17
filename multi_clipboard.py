import pyperclip
import threading
import time
import keyboard  

# store 5 slots
clips = [""] * 5
counter = 0
last_clear_time = time.time()
clear_duration = 60 # secs

def clipboard_watcher():
    global counter, clips, last_clear_time
    old = ""
    while True:
        # if 60 secs are over then reset all the clips
        if  time.time() - last_clear_time >= clear_duration:
            clips[:] = [""] * 5
            counter = 0
            last_clear_time = time.time()
        
        new = pyperclip.paste()
        if new != old and new.strip() != "":
            slot = counter % 5
            clips[slot] = new
            print(f"[+] Stored in slot {slot+1}: {new[:40]}...")  # see the content copied in the terminal
            old = new
            counter += 1
        time.sleep(1)

def paste_from_slot(slot):
    if clips[slot]:
        pyperclip.copy(clips[slot])              # put slot content into clipboard
        keyboard.press_and_release("ctrl+v")     # paste it instantly
        print(f"[+] Pasted slot {slot+1}: {clips[slot][:40]}...")
    else:
        print(f"[!] Slot {slot+1} empty.")

def register_hotkeys():
    for i in range(5):
        keyboard.add_hotkey(f"ctrl+shift+{i+1}", lambda i=i: paste_from_slot(i))
    print("Hotkeys ready: ctrl+shift+1 … ctrl+shift+5")

# start clipboard monitoring thread
t1 = threading.Thread(target=clipboard_watcher, daemon=True)
t1.start()

# setup hotkeys
register_hotkeys()

print("Clipboard Manager running... (Ctrl+C to quit)")
keyboard.wait()  # keep running
