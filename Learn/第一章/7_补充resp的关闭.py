# -*-coding:utf-8-*-
"""
@project:Spiders
@Author: Phantom
@Time:2022/10/10 1:29
@开发环境：windows 10 + python3.7
@IDE：PyCharm2021.3.1
@Email: 2909981736@qq.com
"""
import requests

# 抓包中的XHR一般表示二次请求(请求数据)

url = 'https://movie.douban.com/j/chart/top_list'

# url太长, 重新封装参数
params = {
    'type': '24',
    'interval_id': '100:90',
    'action': '',
    'start': 0,
    'limit': 20
}

# 伪装请求设备
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.37'
}

resp = requests.get(url, params=params, headers=headers)
print(resp.request.url)
# print(resp.request.headers)
print(resp.json())

# 关掉resp
resp.close()
