# -*-coding:utf-8-*-
"""
@project:Spiders
@Author: Phantom
@Time:2022/10/16 23:42
@开发环境：windows 10 + python3.7
@IDE：PyCharm2021.3.1
@Email: 2909981736@qq.com
"""
import requests
import csv
url = "http://www.xinfadi.com.cn/getCat.html"

data = {
    'prodCatid': '1186'
}
resp = requests.post(url, data=data)
resp.close()
price_json = resp.json()['list']
f = open('xinfadi_price.csv', mode='a', encoding='utf-8')
csvwriter = csv.writer(f)
csvwriter.writerow(price_json[0].keys())
for n in price_json:
    for k in n.keys():
        if n[k] is None:
            n[k] = 'None'
    csvwriter.writerow(n.values())
f.close()
print("ok")
