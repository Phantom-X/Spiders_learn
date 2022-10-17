# -*-coding:utf-8-*-
"""
@project:Spiders
@Author: Phantom
@Time:2022/10/16 23:21
@开发环境：windows 10 + python3.7
@IDE：PyCharm2021.3.1
@Email: 2909981736@qq.com
"""
import csv
import requests
from bs4 import BeautifulSoup

f = open("菜价.csv", mode="w", encoding='utf-8')
csvwriter = csv.writer(f)


url = 'http://www.jnmarket.org/import/list-1_1.html'
resp = requests.get(url)
# print(resp.text)
resp.close()

# 解析数据
# 1.把页面源代码交给BeautifulSoup进行处理, 生成bs对象
page = BeautifulSoup(resp.text, 'html.parser')  # 指定html解析器
# 2.从bs对象查找数据
# find(标签, 属性=值)
# find_all(标签, 属性=值)
# table = page.find("table", class_="price-table")  # class是python关键字， 所以class_
table = page.find("table", attrs={'class': 'price-table'})  # 和上一行一个意思
# print(table)
# 拿到所有数据行
trs = table.find_all("tr")[1:]
# print(trs)
for tr in trs:
    tds = tr.find_all("td")  # 每行所有td
    rowdata = []
    for td in tds:
        # print(td.text, end=' ')  # .text表示拿到被标签标记的内容
        rowdata.append(td.text)
    print(rowdata)
    csvwriter.writerow(rowdata)
f.close()
print("over")
