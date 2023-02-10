# -*-coding:utf-8-*-
"""
@project:Spiders
@Author: Phantom
@Time:2023/1/6 10:55
@开发环境：windows 10 + python3.8
@IDE：PyCharm2021.3.1
@Email: 2909981736@qq.com
"""
import csv
import requests

with open('csvimg.csv', mode='r') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        for url in row:
            name = url.rsplit("/", 2)[1]+'/'+url.rsplit("/", 2)[2]
            print(name)
            resp = requests.get(url)
            with open(f'img/{name}', mode='wb') as img:
                img.write(resp.content)
                resp.close()


