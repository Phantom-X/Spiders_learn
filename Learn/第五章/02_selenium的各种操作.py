# -*-coding:utf-8-*-
"""
@project:Spiders
@Author: Phantom
@Time:2023/2/10 23:42
@开发环境：windows 10 + python3.8
@IDE：PyCharm2021.3.1
@Email: 2909981736@qq.com
"""
from time import sleep

from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

web = Chrome(options=options)
web.get("https://www.lagou.com")
sleep(2)
# 找到某个元素 点击它
el = web.find_element(By.XPATH, '//*[@id="changeCityBox"]/ul/li[3]/a')
el.click()
sleep(1)
# 找到输入框，输入python => 输入回车/点击搜索按钮
web.find_element(By.XPATH, '/html/body/div[7]/div[1]/div[1]/div[1]/form/input[1]').send_keys("python", Keys.ENTER)
sleep(1)
div_list = web.find_elements(By.XPATH, '/html/body/div/div[2]/div/div[2]/div[3]/div/div[1]/div')
for div in div_list:
    job_name = div.find_element(By.XPATH, './div[1]/div[1]/div[1]/a[1]').text
    job_money = div.find_element(By.XPATH, './div[1]/div[1]/div[2]/span').text
    print(job_name, job_money)

