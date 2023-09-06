import csv

from lxml import etree

import requests

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.47',
    'Connection': 'close'
}

with open('1.txt', encoding='utf-8', mode='r') as f:
    url = f.read()
    urls = eval(url)

weixinurls = []
czuurls = []

# 但是可能会出现 InsecureRequestWarning 警告，
# 虽然不影响代码采集但是看着不舒服，可以加上下面两行：
import urllib3

urllib3.disable_warnings()

okurls = []
for u in urls:
    if 'mp.weixin.qq.com' in u:
        weixinurls.append(u)
    else:
        czuurls.append('https://www.czu.cn' + u)
cnt = 1
for czu in czuurls:
    try:
        resp = requests.get(czu, headers=header, verify=False)
        resp.encoding = 'utf-8'
        page = etree.HTML(resp.text)
        if resp.status_code == 200:
            contentlist = page.xpath('/html/body/div[4]/div/div[2]/div/div[2]/div/div/div//p/text()')
            content = str(contentlist)
            if ('申报书' in content) or ('教学成果奖' in content):
                print(cnt)
                # print(content)
                okurls.append([czu])
                cnt += 1
        resp.close()
    except:
        continue

with open('1.csv', mode='a', encoding='utf-8', newline='') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerows(okurls)
