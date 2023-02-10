# -*-coding:utf-8-*-
"""
@project:Spiders
@Author: Phantom
@Time:2023/1/10 15:06
@开发环境：windows 10 + python3.8
@IDE：PyCharm2021.3.1
@Email: 2909981736@qq.com
"""
import requests

url = "http://cx.strzol.com/c.aspx?code=27821Q10071R0S"

resp = requests.get(url)
print(resp.text)