# -*-coding:utf-8-*-
"""
@project:Spiders
@Author: Phantom
@Time:2022/10/17 0:40
@开发环境：windows 10 + python3.7
@IDE：PyCharm2021.3.1
@Email: 2909981736@qq.com
"""
# 1.拿到主页面源代码, 然后提取到子页面的url
# 2.通过href拿到子页面的内容, 从子页面中找到图片下载地址 img->src
# 3.下载图片
import re
import requests
from bs4 import BeautifulSoup

numstr = ''
url = f"https://www.umei.cc/meinvtupian/xingganmeinv/index{numstr:}.htm"
resp = requests.get(url)
resp.encoding = 'utf-8'
resp.close()
# print(resp.text)

page = BeautifulSoup(resp.text, "html.parser")
item = page.find("div", class_="item_list infinite_scroll")
title_list = item.find_all("div", class_="title")
# print(title_list)
chile_url = []
for t in title_list:
    chile_url.append("https://www.umei.cc" + t.find("a").get('href'))  # 通过get可以拿到属性值
# print(chile_url)

photo_list = []
num = 1
for n, curl in enumerate(chile_url):
    print(f"------------------第{n + 1:}个套图--------------------")
    for i in range(1, 90):
        try:
            url = curl
            if i != 1:
                url = url.replace('.htm', f'_{i:}.htm')
            resp = requests.get(url)
            resp.encoding = 'utf-8'
            resp.close()
            page = BeautifulSoup(resp.text, "html.parser")
            photo = page.find("div", class_="big-pic").find("img").get("src")
            img_resp = requests.get(photo)
            with open(f"2_7_photo/00000{num:}.jpg", mode="wb") as f:
                f.write(img_resp.content)  # .content拿到字节
                print(f"第{num:}张")
                num += 1
            img_resp.close()
        except:
            break
print("save over")
