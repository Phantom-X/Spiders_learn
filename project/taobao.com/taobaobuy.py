# -*-coding:utf-8-*-
"""
@project:Spiders
@Author: Phantom
@Time:2022/12/24 11:16
@开发环境：windows 10 + python3.8
@IDE：PyCharm2021.3.1
@Email: 2909981736@qq.com
"""
import datetime

now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")

buytime = "2022-12-24 12:00:00.00000000"
webtool = webdriver.Chrome()

webtool.get("https://www.taobao.com")
time.sleep(3)
webtool.find_element(By.LINK_TEXT, "亲，请登录").click()

print("扫码登录")
time.sleep(10)
webtool.get("https://cart.taobao.com/cart.htm")
time.sleep(3)

while True:
    try:
        if webtool.find_element(By.ID, "J_Order_s_2213193048078_1"):
            webtool.find_element(By.ID, "J_Order_s_2213193048078_1").click()  #
            break
    except:
        print("找不到按钮")

while True:
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    print(now)
    if now > buytime:
        while True:
            try:
                if webtool.find_element(By.LINK_TEXT, "结 算"):
                    print("here")
                    webtool.find_element(By.LINK_TEXT, "结 算").click()
                    print("ok")
            except:
                continue
        while True:
            try:
                if webtool.find_element(By.LINK_TEXT, "提交订单"):
                    webtool.find_element(By.LINK_TEXT, "提交订单").click()
                    print("付款")
            except:
                print(f"主人，结算提交成功,我已帮你抢到商品啦,请及时支付订单")
                speaker.Speak(f"主人，结算提交成功,我已帮你抢到商品啦，请及时支付")
                break
        time.sleep(0.01)
