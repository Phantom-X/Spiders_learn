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

# 参数配置
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
options.add_argument('--headless')  # 无头模式
options.add_argument('--disable-gpu')

web = Chrome(options=options)
web.get("https://www.endata.com.cn/BoxOffice/BO/Year/index.html")
sleep(2)

# # 定位下拉列表
# sel_el = web.find_element(By.XPATH, '//*[@id="OptionDate"]')
# # 对元素进行包装，包装成下拉菜单
# sel = Select(sel_el)
# # 让浏览器进行调整选项
# for i in range(len(sel.options)):  # i就是每一个下拉框选项的索引位置
#     sel.select_by_index(i)  # 按照索引进行切换
#     sleep(2)
#     table = web.find_element(By.XPATH, '//*[@id="TableList"]/table')
#     print(table.text)
#     print("================================================================")
#
# web.close()

# 如何拿到页面代码(经过数据加载以及js执行之后的结果的html内容)
print(web.page_source)
