import time
import pyautogui
from datetime import datetime
from pynput.keyboard import Controller, Key
from ids import ids
from playsound import playsound

keyboard = Controller()

isStarted = False

target = input("Enter the pre-set key you wish to enter:")
for i in ids:
    if i[0] == target:
        print("You picked " + target + ".")
        meet_id = i[1]
        password = i[2]
        print("Entering " + target + "'s meeting room.")
        pyautogui.press('esc',interval=0.1)
        time.sleep(0.2)
        pyautogui.press('win',interval=0.1)
        pyautogui.write('zoom')
        pyautogui.press('enter',interval=0.5)
        time.sleep(7)
        print("Ensuring Zoom is online......It may take up to 7 seconds.")
        x, y = pyautogui.locateCenterOnScreen('joinButton.png', confidence=0.9)
        pyautogui.click(x, y)
        pyautogui.press('enter',interval=1)
        print("Entering meeting room: " + target)
        print("Zoom ID: " + meet_id)
        pyautogui.write(meet_id)
        pyautogui.press('enter',interval=1)
        time.sleep(3)
        pyautogui.press('enter',interval=1)
        print("Password: " + password)
        pyautogui.write(password)
        print("Entering, please wait......")
        pyautogui.press('enter',interval = 1)
        isStarted = True