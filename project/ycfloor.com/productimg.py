# -*-coding:utf-8-*-
"""
@project:Spiders
@Author: Phantom
@Time:2023/1/6 12:59
@开发环境：windows 10 + python3.8
@IDE：PyCharm2021.3.1
@Email: 2909981736@qq.com
"""
import os

import requests
from lxml import etree, html
from lxml.etree import _Element

urls = ['http://www.ycfloor.com/product.html', 'http://www.ycfloor.com/product_2.html']
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.42'}

producturls = []
for url in urls:
    resp = requests.get(url, headers=headers)
    page = etree.HTML(resp.text)  # type:_Element
    resp.close()
    divs = page.xpath("/html/body/div[3]/div/div[1]/div[2]/div")  # type:_Element
    for div in divs:  # type:_Element
        link = div.xpath('./a/@href')[0].strip()
        # print(link)
        producturls.append(link)

host = 'http://www.ycfloor.com/'
for i in range(0, len(producturls)):
    producturls[i] = host + producturls[i]

for p in producturls:
    resp = requests.get(p, headers=headers)
    tree = etree.HTML(resp.text)
    resp.close()
    dirname = tree.xpath('/html/body/div[3]/div/div[1]/div[1]/div[2]/h1/text()')[0].strip()
    if '|' in dirname:
        dirname = dirname.replace('|', '')
    os.mkdir(f'./image/{dirname}')
    a = tree.xpath('/html/body/div[3]/div/div[1]/div[1]/div[1]/div[1]/a/@href')
    for i in a:
        link = host+i
        imgname = link.rsplit("/", 1)[1]
        img = requests.get(link, headers=headers)
        with open(f'./image/{dirname}/{imgname}' , mode='wb') as f:
            f.write(img.content)
            resp.close()

