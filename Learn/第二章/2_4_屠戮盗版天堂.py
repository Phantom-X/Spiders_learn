# -*-coding:utf-8-*-
"""
@project:Spiders
@Author: Phantom
@Time:2022/10/16 17:39
@开发环境：windows 10 + python3.7
@IDE：PyCharm2021.3.1
@Email: 2909981736@qq.com
"""
# 1.定位2022新品资源
# 2.从2022新品资源提取到子页面链接地址
# 3.请求子页面链接地址，拿到我们想要的下载地址
import re
import requests

domain = "https://m.dytt8.net/index2.htm"
resp = requests.get(domain, verify=True)  # verify = False 去掉安全验证
resp.encoding = 'gb2312'  # 指定字符集

obj1 = re.compile(r'2022新片精品.*?<table.*?>(?P<table>.*?)</table>', re.S)
obj2 = re.compile(r"<tr>.*?最新电影下载</a>]<a href='(?P<url>.*?)'>.*?</tr>", re.S)
obj3 = re.compile(r'◎译　　名　(?P<movie>.*?)<br />.*?<a target="_blank" href="(?P<download>.*?)">', re.S)
ret = obj1.finditer(resp.text)
resp.close()
child_url_list = []
for it in ret:
    table = it.group("table")
# print(table)
    ret2 =obj2.finditer(table)
    for itt in ret2:
        # 拼接子页面url地址：
        child_url = domain.replace('/index2.htm', '') + itt.group('url')
        child_url_list.append(child_url)
        print(child_url)

for url in child_url_list:
    child_resp = requests.get(url)
    child_resp.encoding = 'gb2312'
    # print(child_resp.text)
    ret3 = obj3.search(child_resp.text)
    print(ret3.group('movie'))
    print(ret3.group('download'))
