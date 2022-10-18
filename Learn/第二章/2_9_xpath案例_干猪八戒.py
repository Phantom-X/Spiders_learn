# -*-coding:utf-8-*-
"""
@project:Spiders
@Author: Phantom
@Time:2022/10/18 2:12
@开发环境：windows 10 + python3.7
@IDE：PyCharm2021.3.1
@Email: 2909981736@qq.com
"""
# 拿到页面源代码
# 提取和解析数据
import csv

import requests
from bs4 import BeautifulSoup
from lxml import etree, html
import html as HTML

# 获得源码
url = 'https://luoyang.zbj.com/search/service/?kw=saas'
resp = requests.get(url)
resp.close()

# 解析
page = etree.HTML(resp.text)

# 拿到每一个服务商的div
divs = page.xpath(f'//*[@id="__layout"]/div/div[3]/div/div[3]/div[4]/div[1]/div')
modulelist = []
for div in divs:
    price = div.xpath("./div/div[3]/div[1]/span/text()")[0].strip("￥")
    title = "saas".join(div.xpath("./div/div[3]/a/text()"))
    com_name = div.xpath("./div/a/div[2]/div[1]/div/text()")[0]

    # xpath对象转成BeautifulSoup可以处理的对象
    temp = html.tostring(div.xpath("./div/div[2]/a/div[2]")[0])
    temp = str(temp, encoding="utf-8")
    temp = HTML.unescape(temp)
    soup = BeautifulSoup(temp, 'lxml')
    location = soup.find_all('div', class_="tabstwo")[1].find_all('span')[1].text
    modulelist.append([title, price, com_name, location])

with open("saas_price.csv", mode="w", encoding='utf-8') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerows(modulelist)

