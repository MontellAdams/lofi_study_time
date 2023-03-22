import pyautogui
import pydirectinput


# Press the key combination "Win+P"
pyautogui.hotkey('win', 'p')

# Press the down arrow key twice to select "PC screen only"
pydirectinput.press(['up', 'up'])

# Press Enter to apply the changes
pyautogui.hotkey('enter')

# Print a message to the console
print("The second monitor has been turned off.")
