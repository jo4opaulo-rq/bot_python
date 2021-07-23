import pyautogui
import time
pyautogui.PAUSE=2

pyautogui.press('win')
time.sleep(0.2)
pyautogui.write('spotify')
pyautogui.press('down')
pyautogui.press('enter')
time.sleep(5)
pyautogui.click(x=73, y=456)
time.sleep(1)
pyautogui.click(x=295, y=424)
