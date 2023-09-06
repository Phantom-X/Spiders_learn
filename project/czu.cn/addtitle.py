# -*-coding:utf-8-*-
"""
@project:Spiders
@Author: Phantom
@Time:2023/3/2 13:17
@开发环境：windows 10 + python3.8
@IDE：PyCharm2021.3.1
@Email: 2909981736@qq.com
"""
import requests
import csv
from lxml import etree
import xlwings as xw
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.47',
    'Connection': 'close'
}

xlsx = []
with open('1.csv', mode='r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for line in reader:
        resp = requests.get(line[0], headers=header)
        resp.encoding = 'utf-8'
        page = etree.HTML(resp.text)
        title = page.xpath('/html/body/div[4]/div/div[2]/div/div[2]/h1/text()')
        xlsx.append([title[0], line[0]])


app = xw.App(visible=False, add_book=False)

wb1 = app.books.add()
sheet1 = wb1.sheets['sheet1']
sheet1.range('A1').value = xlsx
wb1.save(r'target.xlsx')
wb1.close()
app.quit()