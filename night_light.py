import pyautogui
import pydirectinput
from pywinauto import Application
pyautogui.PAUSE = 1.0

# Press the key combination "Win"
pyautogui.hotkey('win')

# Type Night Light
pydirectinput.typewrite('night')

# Open Night Light
pyautogui.hotkey('enter')

# Press the down arrow key twice to select "PC screen only"
pyautogui.press(['tab', 'tab', 'tab'])

# Press Enter to apply the changes
pyautogui.hotkey('enter')

# Close the Night light settings window
pyautogui.hotkey('alt', 'f4')

# Print a message to the console
print("Night Light is on and the settings window is closed")