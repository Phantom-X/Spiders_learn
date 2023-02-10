# -*-coding:utf-8-*-
"""
@project:Spiders
@Author: Phantom
@Time:2023/1/6 13:32
@开发环境：windows 10 + python3.8
@IDE：PyCharm2021.3.1
@Email: 2909981736@qq.com
"""
import os

import requests
from lxml import etree

urls = ['http://www.ycfloor.com/photo/photo-87-342.html', 'http://www.ycfloor.com/photo/photo-27-890.html',
        'http://www.ycfloor.com/photo/photo-11-527.html']
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.42'}
host = 'http://www.ycfloor.com/'

for url in urls:
    resp = requests.get(url, headers=headers)
    tree = etree.HTML(resp.text)
    resp.close()
    dirname = tree.xpath('/html/body/div[3]/div/div[1]/div[1]/h2/span/text()')[0]
    os.mkdir(f'./案例/{dirname}')
    a = tree.xpath('/html/body/div[3]/div/div[1]/div[2]/div[1]/a/@href')
    for i in a:
        link = host + i
        imgname = link.rsplit("/", 1)[1]
        img = requests.get(link, headers=headers)
        with open(f'./案例/{dirname}/{imgname}', mode='wb') as f:
            f.write(img.content)
            resp.close()
