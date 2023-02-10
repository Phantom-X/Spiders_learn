# -*-coding:utf-8-*-
"""
@project:Spiders
@Author: Phantom
@Time:2023/1/6 0:16
@开发环境：windows 10 + python3.8
@IDE：PyCharm2021.3.1
@Email: 2909981736@qq.com
"""
import csv
import xlwings as xw
import requests
from bs4 import BeautifulSoup
from lxml import etree, html
from lxml.etree import _Element
import html as HTML
from bs4 import BeautifulSoup

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
# print(producturls)

csvlist1 = []
csvlist2 = []
csvimg = []
for p in producturls:
    resp = requests.get(p, headers=headers)
    tree = etree.HTML(resp.text)
    resp.close()
    name = tree.xpath('/html/body/div[3]/div/div[1]/div[1]/div[2]/h1/text()')[0].strip()
    info = tree.xpath('/html/body/div[3]/div/div[1]/div[1]/div[3]')[0]
    content = html.tostring(info)
    content = HTML.unescape(content.decode()).replace('<div class="product_con">', '').replace('</div>', '').strip()
    soup = BeautifulSoup(content, 'lxml')
    imgs = soup.find_all('img')
    contentimg = []
    for img in imgs:
        contentimg.append(host + img.get('src').strip())
    csvlist1.append([name, content])
    csvimg.append(contentimg)
    info = info.xpath('.//span/text()')
    csvlist2.append([name, " ".join(info)])

with open("csvlist1.csv", mode="w", encoding='utf-8', newline='') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerows(csvlist1)

with open("csvlist2.csv", mode="w", encoding='utf-8', newline='') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerows(csvlist2)

with open("csvimg.csv", mode="w", encoding='utf-8', newline='') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerows(csvimg)

app = xw.App(visible=False, add_book=False)

wb1 = app.books.add()
wb2 = app.books.add()
sheet1 = wb1.sheets['sheet1']
sheet1.range('A1').value = csvlist1
sheet2 = wb2.sheets['sheet1']
sheet2.range('A1').value = csvlist2
wb1.save(r'csvlist1.xlsx')
wb2.save(r'csvlist2.xlsx')
wb1.close()
wb2.close()
app.quit()
