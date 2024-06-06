import pyautogui
import time

pyautogui.press("win")
time.sleep(1)
pyautogui.write("note")
time.sleep(0.5)
pyautogui.press("enter")
time.sleep(0.5)
pyautogui.write("ok")
time.sleep(1)
pyautogui.hotkey("alt", "f4", "fn")
time.sleep(0.5)
pyautogui.press("tab")
time.sleep(0.5)
pyautogui.press("enter")
