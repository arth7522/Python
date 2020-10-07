import pyautogui
import time

try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr)
        time.sleep(1/5)
except KeyboardInterrupt:
    print('\nDone.')
