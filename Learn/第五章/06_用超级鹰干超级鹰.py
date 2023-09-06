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
from selenium.webdriver.support.select import Select
from chaojiying_Python.chaojiying import Chaojiying_Client

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

web = Chrome(options=options)
web.get("http://www.chaojiying.com/user/login/")
sleep(1)
img = web.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div[1]/form/div/img').screenshot_as_png  # 图片截屏
chaojiying = Chaojiying_Client('phantom', 'pcw12345678', '944868')
dic = chaojiying.PostPic(img, 1902)
verify_code = dic['pic_str']
sleep(1)
# 向页面中填入用户名密码验证码
web.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div[1]/form/p[1]/input').send_keys('phantom')
web.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div[1]/form/p[2]/input').send_keys('pcw12345678')
web.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div[1]/form/p[3]/input').send_keys(verify_code)
sleep(1)
# 点击登录
web.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div[1]/form/p[4]/input').click()