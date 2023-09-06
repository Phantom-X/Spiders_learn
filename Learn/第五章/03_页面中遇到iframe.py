# -*-coding:utf-8-*-
"""
@project:Spiders
@Author: Phantom
@Time:2023/2/11 15:37
@开发环境：windows 10 + python3.8
@IDE：PyCharm2021.3.1
@Email: 2909981736@qq.com
"""
from time import sleep

from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 页面中遇到iframe
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

web = Chrome(options=options)
web.get("http://www.91xie.com/vodplay/877-4-1/")
sleep(1)
# 处理iframe的话，必须先拿到iframe.然后切换视角到iframe，再然后才可以拿数据
iframe1 = web.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div[1]/iframe')
web.switch_to.frame(iframe1)
iframe2 = web.find_element(By.XPATH, '//*[@id="iframe"]')
web.switch_to.frame(iframe2)
video = web.find_element(By.XPATH, '/html/body/div[1]/div[2]/video')
print(video.get_attribute('src'))
# 切回默认页面
web.switch_to.default_content()
