# -*-coding:utf-8-*-
"""
@project:Spiders
@Author: Phantom
@Time:2023/2/10 23:26
@开发环境：windows 10 + python3.8
@IDE：PyCharm2021.3.1
@Email: 2909981736@qq.com
"""
# 让程序连接到浏览器 . 让浏览器来完成各种复杂的操作，我们只接受最终的结果
# selenium:自动化测试工具
# 可以打开浏览器，模拟人操作浏览器
# 可以从selenium中直接提取网页上的各种信息
from selenium import webdriver
from selenium.webdriver import Chrome

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
# 创建浏览器对象
web = Chrome(options=options)
# 打开一个网址
web.get('https://www.baidu.com')

print(web.title)

# web.close()

