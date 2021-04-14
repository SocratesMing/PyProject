# 将加密分享的文件保存到自己云盘的目录下
import time
from selenium.common import exceptions
def extract(driver, src_url, share_password):
    driver.get(src_url)
    try:
        getpwd = driver.find_element_by_id("accessCode")  #("esDEV5")
        getpwd.send_keys(share_password)
        getButton = driver.find_element_by_link_text("提取文件")
        getButton.click()
        time.sleep(10)

    except exceptions.NoSuchElementException:
        print("已经打开，不需要密码")

    finally:

        # savetodisk = driver.find_element_by_link_text("保存到网盘")
        # savetodisk.click()
        # time.sleep(5)
        # # AA 为指定的自己网盘保存路径
        # selectdir = driver.find_element_by_xpath("//span[@node-path='/图片/anran']")
        # selectdir.click()
        # enter = driver.find_element_by_link_text("确定")
        # enter.click()
        # time.sleep(2)
        savetodisk = driver.find_element_by_link_text("保存到网盘")
        savetodisk.click()
        time.sleep(5)

        while 1:
            start = time.time()
            try:
                # AA 为指定的自己网盘保存路径
                driver.find_element_by_xpath("//span[@node-path='/图片']").click()
                time.sleep(1)
                driver.find_element_by_xpath("//span[@node-path='/图片/anran']").click()
                driver.find_element_by_link_text("确定").click()
                time.sleep(2)
                end = time.time()
                break
            except:
                print("还未定位到元素!")

        print('定位耗费时间：' + str(end - start))



# src_url = "https://pan.baidu.com/share/init?surl=aupD46MfsTgUg5SZZJ2WfA"
src_url = "https://pan.baidu.com/share/init?surl=INjvsl3LukPOJEp8Besa_w"
share_password =  "ibts"

# extract(driver = driver,src_url = src_url,share_password= share_password)