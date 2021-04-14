import time, os
from selenium import webdriver
from selenium.webdriver.common.by import By

writeN = 0


def saveData2Txt(modelName, pageStart, pageStop, data = ""):
    data = data + '\n'
    txtName = modelName + "_Page" + str(pageStart) + "_" + str(pageStop) + ".txt"
    txtpath = os.path.join(".", modelName, txtName)
    global writeN
    if writeN == 0:
        with open(txtpath, "w", encoding="utf-8") as f:
            f.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "\n" * 3)
        writeN += 1
    else:
        with open(txtpath, "a+", encoding="utf-8") as f:
            f.write(data)


def savePicToDisk(modelLink='https://www.hdmixx.com/tag/%E5%AE%89%E7%84%B6Maleah', pgstart=1, pgstop=2,
                  modelName="anran"):
    option = webdriver.ChromeOptions()
    option.add_argument("user-data-dir=C:/Users/sutut/AppData/Local/Google/Chrome/User Data")
    driver = webdriver.Chrome("./chromedriver.exe",
                              options=option)  # Optional argument, if not specified will search path.

    filePath = os.path.join(".", modelName)  # 创建保存数据文件夹
    if modelName not in os.listdir():
        os.mkdir(filePath)

    saveData2Txt(modelName, pgstart, pgstop)#生成文件

    galleryArr = []
    succ = 0
    fail = 0
    for x in range(pgstart, pgstop+1):
        if x == 0:
            driver.get(modelLink)
            gallery1 = driver.find_elements(By.CSS_SELECTOR, ".posts-gallery-content > h2 > a")
            galleryArr.append([u.get_property("href") for u in gallery1])

        else:
            driver.get(modelLink + '/page/' + str(x + 1))
            gallery2 = driver.find_elements(By.CSS_SELECTOR, ".posts-gallery-content > h2 > a")
            galleryArr.append([u.get_property("href") for u in gallery2])

    print("共有下载项：", str(sum([len(g) for g in galleryArr])))

    for page in range(len(galleryArr)):
        dd = "= " * 10 + " " * 5 + "Page_" + str(pgstart+page) + " " * 5 + " =" * 10 + "\n"
        saveData2Txt(modelName, pgstart, pgstop, dd)

        for link in galleryArr[page]:

            start = time.time()
            print(link)
            driver.get(link)
            title = driver.find_element_by_class_name("title").text
            try:
                driver.find_element_by_link_text("进入下载页面").click()
                time.sleep(3)
                driver.switch_to.window(driver.window_handles[1])
                print("进入到下载项页面2".ljust(10) + "  ---> ", driver.current_url)
            except:
                print("没有下载链接")
                d2 = str(link).ljust(40) + " " * 5 + str(title) + " " * 5 + "保存文件失败"
                saveData2Txt(modelName, pgstart, pgstop, d2)
                fail += 1
                print("SUCCESS:" + str(succ), "FAIL:" + str(fail))
                continue

            try:
                driver.find_element_by_link_text("点击下载").click()
            except:
                print("<点击下载> 按钮没有加载出来")
                time.sleep(1)
                d2 = str(link).ljust(40) + " " * 5 + str(title) + " " * 5 + "保存文件失败"
                saveData2Txt(modelName, pgstart, pgstop, d2)
                fail += 1
                print("SUCCESS:" + str(succ), "FAIL:" + str(fail))
                continue

            share_password = driver.find_element_by_id("code").get_property("value")
            driver.switch_to.window(driver.window_handles[2])
            print("进入到百度云页面3".ljust(10) + "  ---> ", driver.current_url)
            time.sleep(3)

            try:
                getpwd = driver.find_element_by_id("accessCode")  # ("esDEV5")
                time.sleep(2)
                # print("密码 --- ", share_password)
                getpwd.send_keys(share_password)
                getButton = driver.find_element_by_link_text("提取文件")
                getButton.click()
                time.sleep(5)
            except Exception as e:
                print("已经打开，不需要密码")

            try:
                time.sleep(2)
                savetodisk = driver.find_element_by_link_text("保存到网盘")
                savetodisk.click()
                time.sleep(3)
                # AA 为指定的自己网盘保存路径
                driver.find_element_by_xpath("//span[@node-path='/图片']").click()
                time.sleep(1)
                driver.find_element_by_xpath("//span[@node-path='/图片/%s']" % modelName).click()
                driver.find_element_by_link_text("确定").click()
                time.sleep(2)
                timeuse = time.time() - start
                print('保存文件成功!', "用时", timeuse, " S")
                d2 = str(link).ljust(40) + " " * 5 + str(title) + " " * 5 + "保存文件成功"
                saveData2Txt(modelName, pgstart, pgstop, d2)
                succ += 1
                # break

            except Exception as e:
                print("页面3未定位到元素!")
                time.sleep(2)
                d2 = str(link).ljust(40) + " " * 5 + str(title) + " " * 5 + "保存文件失败"
                saveData2Txt(modelName, pgstart, pgstop, d2)
                print('保存文件失败! 链接为：', link)
                fail += 1
                print("SUCCESS:" + str(succ), "FAIL:" + str(fail))

                continue

            driver.close()
            driver.switch_to.window(driver.window_handles[1])
            driver.close()
            time.sleep(1)
            driver.switch_to.window(driver.window_handles[0])
            print("SUCCESS:" + str(succ), "FAIL:" + str(fail))

            print("= " * 40)

        print("运行完成 SUCCESS:" + str(succ), "FAIL:" + str(fail))


modelLink = "https://www.hdmixx.com/tag/%E7%8E%8B%E9%9B%A8%E7%BA%AF"
pageStart = 8
pageStop = 9
modelName = "王雨纯"
savePicToDisk(modelLink, pageStart, pageStop, modelName)
