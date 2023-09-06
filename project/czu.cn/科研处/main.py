# -*-coding:utf-8-*-
"""
@project:Spiders
@Author: Phantom
@Time:2023/3/2 13:36
@开发环境：windows 10 + python3.8
@IDE：PyCharm2021.3.1
@Email: 2909981736@qq.com
"""
import requests
from lxml import etree
import xlwings as xw
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.47',
}

urls = ['https://kyc.czu.cn/771/list.htm', 'https://kyc.czu.cn/769/list.htm', 'https://kyc.czu.cn/770/list.htm']

allnews = []
for u in urls:
    for i in range(1, 21):
        try:
            url = u.replace('list', f'list{i}')
            resp = requests.get(url, headers=header)
            if resp.status_code == 200:
                resp.encoding = 'urf-8'
                page = etree.HTML(resp.text)
                temp = page.xpath('/html/body/div[3]/div[1]/div[2]/div[1]/table//a/@href')
                allnews.extend(temp)
                resp.close()
            else:
                continue
        except:
            continue

print(len(allnews))
allnews.remove("/_redirect?siteId=28&columnId=771&articleId=60809")
allnews.remove("/2017/1205/c771a53765/page.htm")

target = []
for i, a in enumerate(allnews):
    print(i)
    url = 'https://kyc.czu.cn' + a
    print(url)
    resp = requests.get(url, headers=header)
    resp.encoding = 'utf-8'
    page = etree.HTML(resp.text)
    resp.close()
    contentlist = page.xpath('/html/body/div[3]/table/tr[2]/td/div/div//span/text()')
    content = ''.join(contentlist)
    if ('申报书' in content) or ('教学成果奖' in content):
        title = page.xpath('/html/body/div[3]/table/tr[2]/td/h1/span/span/text()')
        target.append([title[0], url])

app = xw.App(visible=False, add_book=False)
wb1 = app.books.add()
sheet1 = wb1.sheets['sheet1']
sheet1.range('A1').value = target
wb1.save(r'科研处.xlsx')
wb1.close()
app.quit()
