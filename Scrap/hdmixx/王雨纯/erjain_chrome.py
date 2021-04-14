import time, os
from selenium import webdriver
from selenium.webdriver.common.by import By
import win32api
import win32con

writeN = 0


def savePicToDisk(n=5):
    count = 1
    option = webdriver.ChromeOptions()
    option.add_argument("user-data-dir=C:/Users/sutut/AppData/Local/Google/Chrome/User Data")
    driver = webdriver.Chrome("./chromedriver.exe",
                              options=option)  # Optional argument, if not specified will search path.
    driver.get("http://user.hqwx.com/uc/material/groupDetail?id=2355&type=0")

    nextpage = driver.find_element(By.CSS_SELECTOR, ".uc2018-ziliao-page>.n")

    for x in range(n):
        if x != 0:
            nextpage.click()
            time.sleep(5)
        linklist = driver.find_elements(By.CSS_SELECTOR, ".title3>a")

        for u in linklist:
            u.click()
            time.sleep(2)
            driver.switch_to.window(driver.window_handles[1])
            time.sleep(1)

            win32api.keybd_event(17, 0, 0, 0)  # ctrl按下
            win32api.keybd_event(83, 0, 0, 0)  # ctrl按下
            time.sleep(1)
            win32api.keybd_event(83, 0, win32con.KEYEVENTF_KEYUP, 0)  # ctrl按下
            win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)  # ctrl按下
            win32api.keybd_event(0x0D, 0, 0, 0)
            time.sleep(1)
            win32api.keybd_event(0x0D, 0, win32con.KEYEVENTF_KEYUP, 0)
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            time.sleep(1)
            print("下载第 "+str(count)+"个PDF")
            count+=1


savePicToDisk()
