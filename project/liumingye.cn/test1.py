# -*-coding:utf-8-*-
"""
@project:Spiders
@Author: Phantom
@Time:2023/1/12 10:15
@开发环境：windows 10 + python3.8
@IDE：PyCharm2021.3.1
@Email: 2909981736@qq.com
"""
# from selenium import webdriver
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# ca = DesiredCapabilities.CHROME
# ca["goog:loggingPrefs"] = {"performance": "ALL"}
# driver = webdriver.Chrome(desired_capabilities=ca)
# driver.get("https://tools.liumingye.cn/music/#/playlist/d7807039303?name=华语金曲千禧年前的旋律")
# logs = driver.get_log("performance")
# print(logs)
import time
from seleniumwire.webdriver import ActionChains
from seleniumwire import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://tools.liumingye.cn/music/#/playlist/d7807039303?name=华语金曲千禧年前的旋律")
time.sleep(10)
# driver.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div/div/div/div/div[4]/div[1]/div/div[4]/div/svg[@stroke-linecap='butt']").click()
# time.sleep(3)
# driver.find_element(By.XPATH, '/html/body/div[6]/div/div[2]/div[2]/div/div/div[1]/div/span').click()
# time.sleep(8)
def get_request_headers():
    """
    获取所有加载的url
    """
    print('获取所有加载的url：')
    for request in driver.requests:
        print(request.url)
    driver.quit()


get_request_headers()
