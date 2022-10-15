# -*-coding:utf-8-*-
"""
@project:Spiders
@Author: Phantom
@Time:2022/10/10 11:31
@开发环境：windows 10 + python3.7
@IDE：PyCharm2021.3.1
@Email: 2909981736@qq.com
"""
import glob
import random
from xgmn import photo_n
import requests

user_agent_list = [
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15"
]

headers = {
    'User-Agent': 'Mozilla/5.0',
    'Connection': 'close'
}
num = len(glob.glob('.\photo\*.jpg'))

photon = photo_n(c=1, n0=16, n1=19)
for n in photon:

    headers['User-Agent'] = random.choice(user_agent_list)
    url = f'http://www.tpxl.com/datacache/pic_{n:}.js'
    try:
        resp = requests.get(url, headers=headers)
        data = resp.text
        # 关掉resp
        resp.close()

        data = eval(data.replace(f'success_jsonpCallback{n:}', ''))
        # print(data[0]['url'].replace("\\", ''))
        # print(len(data))
        for i in range(len(data)):
            url = 'http:' + data[i]['url'].replace("\\", '')
            headers['User-Agent'] = random.choice(user_agent_list)
            r = requests.get(url=url, headers=headers)
            with open(f'.\photo\phpto{num:}.jpg', 'wb') as f:
                f.write(r.content)
                print(f'第{num:}张')
            r.close()
            num += 1
    except:
        continue
