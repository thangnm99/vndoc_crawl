import pyautogui
import keyboard

str = ''
while True:
    str += keyboard.read_key()
    if keyboard.read_key() == 'esc':
        break
    if keyboard.read_key() == '/':
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save(r'scrshot.png')

print(str)