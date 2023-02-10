# -*-coding:utf-8-*-
"""
@project:Spiders
@Author: Phantom
@Time:2022/12/29 15:35
@开发环境：windows 10 + python3.8
@IDE：PyCharm2021.3.1
@Email: 2909981736@qq.com
"""
import requests

url = 'http://gx.roots.315mao.com/index/index/index?id=78'
resp = requests.get(url)
print(resp.text)