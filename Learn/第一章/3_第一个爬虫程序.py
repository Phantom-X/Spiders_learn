# -*-coding:utf-8-*-
"""
@project:Spiders
@Author: Phantom
@Time:2022/10/7 20:20
@开发环境：windows 10 + python3.7
@IDE：PyCharm2021.3.1
@Email: 2909981736@qq.com
"""
# 爬虫 通过编写程序来获得互联网上的资源
# 用程序模拟浏览器 输入一个网址 从该网址中获取到资源或内容
from urllib.request import urlopen

url = "http://www.baidu.com"
resp = urlopen(url)
# decode解码 字节转utf-8
# print(resp.read().decode("utf-8"))
with open("mybaidu.html", mode="w", encoding="utf-8") as f:
    f.write(resp.read().decode())
    f.close()
print("ok")
