import pyautogui
import keyboard

# Set the initial state of the program to "stopped"
is_running = False

# Define a function that handles the space key press event
def handle_space_press():
    global is_running
    
    # If the program is already running, stop it
    if is_running == False:
        
        is_running = True
        print("Program started")
        
        # Loop until the space key is pressed again
        while is_running:
            pyautogui.click()
            
            # Check if the space key has been pressed again
            if keyboard.is_pressed('c'):
                is_running = False
                print("Program stopped")
                break 

# Bind the space key to the handle_space_press function
keyboard.add_hotkey("space", handle_space_press)

# Start the keyboard listener
keyboard.wait()