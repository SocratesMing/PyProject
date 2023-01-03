import pyautogui
import time


def autoClickAction(n=10000,sleep=60):

    for d in range(1, n):
        print("------------------+")
        print("times:",d)
        time.sleep(sleep)
        size = pyautogui.size()
        pyautogui.FAILSAFE = False
        print(size)
        x = size.width / 2
        y = size.height / 2

        pyautogui.moveTo(x, y)
        position = pyautogui.position()
        print(position)

        pyautogui.click()

        for _ in range(4):
            print("============")
            pyautogui.moveTo(x+10, y, 1)
            print(pyautogui.position())

            time.sleep(1)
            pyautogui.moveTo(x-10, y, 1)
            print(pyautogui.position())


if __name__ == '__main__':
    autoClickAction(1000)
