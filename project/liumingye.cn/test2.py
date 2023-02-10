# -*-coding:utf-8-*-
"""
@project:Spiders
@Author: Phantom
@Time:2023/1/12 10:56
@开发环境：windows 10 + python3.8
@IDE：PyCharm2021.3.1
@Email: 2909981736@qq.com
"""
import requests



url = 'https://tools.liumingye.cn/music/#/playlist/d7807039303?name=华语金曲千禧年前的旋律'

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.76'}

resp = requests.get(url, headers=headers)
resp.encoding='utf-8'
print(resp.text)

resp.close()
