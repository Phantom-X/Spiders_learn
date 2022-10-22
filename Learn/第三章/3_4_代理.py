# -*-coding:utf-8-*-
"""
@project:Spiders
@Author: Phantom
@Time:2022/10/19 20:00
@开发环境：windows 10 + python3.7
@IDE：PyCharm2021.3.1
@Email: 2909981736@qq.com
"""
# 代理原理 通过第三方的一个机器IP去发送请求

import requests
import time as t

# 准备好代理IP(网上找): 222.214.191.225:9999    39.106.16.117:80
proxies = {
    'http': 'http://112.74.104.232:8888'
}

resp = requests.get("http://www.baidu.com", proxies=proxies)
resp.encoding = 'utf-8'
print(resp.text)
resp.close()