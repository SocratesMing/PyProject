import time
from selenium import webdriver

# option = webdriver.ChromeOptions()
driver = webdriver.Edge("./msedgedriver.exe")  # Optional argument, if not specified will search path.
driver.get('https://www.baidu.com/');
# time.sleep(5)
driver.get('https://www.hdmixx.com/taotu/xiurenwang/xiuren?tag=%E5%AE%89%E7%84%B6Maleah');
time.sleep(5) # Let the user actually see something!
# search_box = driver.find_element_by_name('q')
# search_box.send_keys('ChromeDriver')
# search_box.submit()
# time.sleep(5) # Let the user actually see something!
# driver.quit()