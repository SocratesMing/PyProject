import time

import urllib3.util
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from record import has_save_to_cloud

options = webdriver.EdgeOptions()
# 只能打开一个edge浏览器，除非重新复制一份出来
options.add_argument(r"user-data-dir=C:\Users\sututu\AppData\Local\Microsoft\Edge\User Data")
driver = webdriver.Edge(options=options)

save_list = []
saved_list = []

class atuo_save_to_cloud:

    def __init__(self, model_name, cloud_path, page_num) -> None:
        self.model_name = model_name
        self.cloud_path = cloud_path
        self.page_num = page_num

    def execute(self):
        self.__find_gallery_herf()

    def __find_gallery_herf(self):
        """
        :param model_name: 模特名称
        :param n: 从第几页开始
        :return:
        """

        saved_list.extend(has_save_to_cloud(model_name))
        n = 1 if self.page_num <= 1 else self.page_num
        for page_num in range(n, 1000):
            if page_num == 1:
                str_url = "https://www.hdmizz.com/tag/" + model_name
            else:
                str_url = "https://www.hdmizz.com/tag/" + model_name + "/page/" + str(page_num)

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
                self.__find_source(a)
                print("- " * 50)

            # save_list.append("- " * 50)
            time.sleep(2)

            if (gallery_num < 12):
                "已经没有图了..."
                break
        driver.quit()

    def __find_source(self, href):
        """
        查找链接
        :param href:
        :return:
        """
        driver.get(href)

        title = driver.find_element(By.CLASS_NAME, "title").text
        if title in saved_list:
            print(title, "已经保存到云了")
            return
        self.title=title
        class_down_price = driver.find_element(By.CLASS_NAME, "down-price")
        vip = class_down_price.find_element(By.TAG_NAME, "span").text
        if vip == "注册会员":
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
            self.__save_cloud()

    def __save_cloud(self, url=None):
        """
        保存到百度云
        :param url: 链接
        :param title: 标题
        :return:
        """
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

            # 百度没选择的路径了
            element = driver.find_element(By.CLASS_NAME, 'save-path-item')
            element.click()
            cloud_path = element.get_attribute("title")
            # cloud_path = driver.find_element(By.CLASS_NAME, 'save-path-item').text
            print("选择最近路径:", cloud_path)

            # 点击确定
            time.sleep(2)
            # driver.find_element(By.CLASS_NAME, "g-button-right").click()
            driver.find_element(By.XPATH, '//*[@id="fileTreeDialog"]/div[4]/a[2]').click()
            # for element in elements:
            #     print(element.text)
            #     if element.text == "确定":
            #         element.click()
            print("存到了百度云盘:", cloud_path)
            self.__save_to_txt()
        except Exception as e:
            print(e)

    def __save_to_txt(self):
        """
        把转存到百度云的图写入到txt文件中
        :param model_name:
        :return:
        """
        txt = self.model_name + ".txt"
        with open(txt, 'a', encoding="utf-8") as f:
            if self.title in saved_list:
                pass
            else:
                f.write(self.title + "\n")
                print(self.title,"保存到",txt)


if __name__ == '__main__':
    model_name = "安然anran"
    cloud_path = "/anran"
    cloud = atuo_save_to_cloud(model_name, cloud_path, 1)
    cloud.execute()
