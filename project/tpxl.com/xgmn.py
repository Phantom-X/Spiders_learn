# -*-coding:utf-8-*-
"""
@project:Spiders
@Author: Phantom
@Time:2022/10/10 12:14
@开发环境：windows 10 + python3.7
@IDE：PyCharm2021.3.1
@Email: 2909981736@qq.com
"""
import random

import requests


def photo_n(c=1, n0=1, n1=1):
    if c > 4 or c < 1 or n0 < 1 or n1 < 1:
        return 'Error'
    cdict = {1: 'xgmn', 2: 'qcmn', 3: 'wmtp', 4: 'mxxz'}
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
    urllist = []
    for i in range(n0, n1 + 1):
        headers['User-Agent'] = random.choice(user_agent_list)
        url = f'http://www.tpxl.com/ajax_lists/{c:}/{i:}/'
        resp = requests.get(url=url, headers=headers)
        datalist = resp.json()['data']
        for j in range(len(datalist)):
            urllist.append(datalist[j]['url'])
        resp.close()

    urllist = list(map(lambda x: x.replace(f'http://www.tpxl.com/{cdict[c]:}/', ''), urllist))
    urllist = list(map(lambda x: int(x.replace('.html', '')), urllist))
    return urllist


if __name__ == '__main__':
    photon = photo_n(c=1, n0=16, n1=19)
    print(photon)
