import time

import urllib3.util
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from has_down_load import has_save_to_cloud

options = webdriver.EdgeOptions()
# 只能打开一个edge浏览器，除非重新复制一份出来
options.add_argument(r"user-data-dir=C:\Users\sututu\AppData\Local\Microsoft\Edge\User Data")
driver = webdriver.Edge(options=options)

save_list = []
saved_list = []


def find_gallery_herf(model_name, n):
    global saved_list
    saved_list = has_save_to_cloud(model_name)
    n = 1 if n <= 1 else n
    for page_num in range(n, 1000):
        if page_num == 1:
            str_url = "https://www.hdmisx.com/tag/" + model_name
        else:
            str_url = "https://www.hdmisx.com/tag/" + model_name + "/page/" + str(page_num)

        url = urllib3.util.parse_url(str_url)
        print(url)
        driver.get(str(url))
        class_posts_gallerys = driver.find_elements(By.CLASS_NAME, "posts-gallery-content")
        gallery_num = len(class_posts_gallerys)
        print("本页面套图共计:", gallery_num)
        # save_list.append(str_url + "\t" * 2 + str(gallery_num))
        list_gallery_href = []
        for class_posts_gallery in class_posts_gallerys:
            tag_a = class_posts_gallery.find_element(By.TAG_NAME, "a")
            href = tag_a.get_attribute("href")
            list_gallery_href.append(href)

        for a in list_gallery_href:
            print("套图详细链接:", a)
            find_source(a)
            print("- " * 50)

        # save_list.append("- " * 50)
        time.sleep(2)

        if (gallery_num < 12):
            "已经没有图了..."
            break

    driver.quit()


def find_source(href):
    driver.get(href)

    title = driver.find_element(By.CLASS_NAME, "title").text
    if title in saved_list:
        print("已经保存到云了")
        return
    class_down_price = driver.find_element(By.CLASS_NAME, "down-price")
    vip = class_down_price.find_element(By.TAG_NAME, "span").text
    if vip=="注册会员":
        class_down_ordinary = driver.find_element(By.CLASS_NAME, "down-ordinary")
        try:
            tag_a = class_down_ordinary.find_element(By.TAG_NAME, "a")
            download_page = tag_a.get_attribute("href")
            print("下载链接:", download_page)
            driver.get(download_page)
        except Exception as e:
            print("目前没有提供下载链接...")
            return

        try:
            # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, yes_button)))
            class_msg = driver.find_element(By.CLASS_NAME, "msg")
            baidu_link_pwd = class_msg.find_element(By.TAG_NAME, "input").get_attribute("value")
            baidu_link = class_msg.find_element(By.TAG_NAME, "a").get_attribute("href")
            driver.get(baidu_link)
            print("百度网盘链接地址:", baidu_link)
            print("密码:", baidu_link_pwd)
            yes_button = '//*[@id="submitBtn"]/a/span/span'
            WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, yes_button)))
            driver.find_element(By.ID, "accessCode").send_keys(baidu_link_pwd)
            driver.find_element(By.XPATH, yes_button).click()
        except Exception as e:
            print("密码已经输过了")
        save_cloud(title=title)


def save_cloud(url=None, title=None):
    if url is not None:
        driver.get(url)
    try:
        # 等待页面出现()
        print("开始转存文件....")
        time.sleep(5)
        save_button = '//*[@id="layoutMain"]/div[1]/div[1]/div/div[3]/div/div/div[2]/a[1]/span/span'
        # WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, "icon icon-save-disk")))

        # 点击保存到云盘按钮
        driver.find_element(By.XPATH, save_button).click()
        # 点击最近保存路径
        # element = driver.find_element(By.XPATH, '//*[@id="fileTreeDialog"]/div[3]')
        time.sleep(2)  # 等待2秒弹窗出现
        element = driver.find_element(By.CLASS_NAME, 'save-path-item')
        element.click()
        cloud_path = element.get_attribute("title")
        # cloud_path = driver.find_element(By.CLASS_NAME, 'save-path-item').text
        print("选择最近路径:", cloud_path)

        # 点击确定
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="fileTreeDialog"]/div[4]/a[2]/span/span').click()
        print("存到了百度云盘:", cloud_path)
        save_list.append(title)
    except Exception as e:
        print(e)
    save_to_txt(model_name)


def save_to_txt(model_name):
    txt = model_name + ".txt"
    with open(txt, 'a', encoding="utf-8") as f:
        for t in save_list:
            if t in saved_list:
                pass
            else:
                f.write(t)
                f.write("\n")


if __name__ == '__main__':
    model_name = "梦心月"
    find_gallery_herf(model_name, 1)
    # url = 'https://www.hdmisx.com/wp-content/plugins/erphpdown/download.php?postid=224920&url=&key=1'
    # save_cloud(url)
