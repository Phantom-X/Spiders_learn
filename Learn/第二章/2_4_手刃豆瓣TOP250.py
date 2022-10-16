# -*-coding:utf-8-*-
"""
@project:Spiders
@Author: Phantom
@Time:2022/10/16 14:23
@开发环境：windows 10 + python3.7
@IDE：PyCharm2021.3.1
@Email: 2909981736@qq.com
"""
# 拿到页面源代码
# 通过re来提取有效信息

import requests
import re
import csv
for n in range(10):
    url = f"https://movie.douban.com/top250?start={n*25:}"
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.42'}
    resp = requests.get(url, headers=headers)
    page_content = resp.text
    resp.close()

    # 解析数据
    obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<title>.*?)'
                     r'</span>.*?<p class="">(?P<director>.*?)&nbsp;.*?<br>(?P<year>.*?)&nbsp;/&nbsp;(?P<country>.*?)&nbsp;/&nbsp;(?P<type>.*?)</p>.*?<span'
                     r' class="rating_num" property="v:average">(?P<score>.*?)</span>'
                     r'.*?<span>(?P<person>.*?)</span>', re.S)
    # 开始匹配
    result = obj.finditer(page_content)

    f = open("data.csv", mode="a", encoding='utf-8')
    csvwriter = csv.writer(f)
    for it in result:
        # print(it.group('title'))
        # print(it.group('director').strip())
        # print(it.group('characters').strip())
        # print(it.group('country'))
        # print(it.group('type').strip())
        # print(it.group('score'))
        # print(it.group('year').strip())
        # print(it.group('person'))
        dic = it.groupdict()
        dic['director'] = dic['director'].strip()
        dic['type'] = dic['type'].strip()
        dic['year'] = dic['year'].strip()
        csvwriter.writerow(dic.values())

    f.close()
print('over!')
