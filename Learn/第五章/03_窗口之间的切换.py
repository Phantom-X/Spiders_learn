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

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

web = Chrome(options=options)
web.get("https://www.lagou.com")
sleep(1)
# 找到某个元素 点击它
el = web.find_element(By.XPATH, '/html/body/div[10]/div[1]/div[2]/div[2]/button[4]')
el.click()
sleep(1)
web.find_element(By.XPATH, '/html/body/div[7]/div[1]/div[1]/div[1]/form/input[1]').send_keys("python", Keys.ENTER)
sleep(1)
btn = web.find_element(By.XPATH,
                       '/html/body/div/div[2]/div/div[2]/div[3]/div/div[1]/div[1]/div[1]/div[1]')
btn.click()

# 如何进入到新窗口中进行提取
# 注意，在selenium的眼中，新窗口默认是不切换过来的.
web.switch_to.window(web.window_handles[-1])  # web.window_handles[-1]最后一个窗口（右边）

# 在新窗口中提取内容
job_detail = web.find_element(By.XPATH, '//*[@id="job_detail"]/dd[2]/div').text
print(job_detail)

# 关掉子窗口
web.close()
# 变更窗口视角
web.switch_to.window(web.window_handles[0])  # web.window_handles[0]

