# -*-coding:utf-8-*-
"""
@project:Spiders
@Author: Phantom
@Time:2023/2/10 21:06
@开发环境：windows 10 + python3.8
@IDE：PyCharm2021.3.1
@Email: 2909981736@qq.com
"""
import os
import glob
import requests
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.37'
}

allts = []
with open('./difficultvideo/index2.m3u8', mode='r') as f:
    for line in f:
        line = line.strip()
        if line.startswith('#'):
            continue
        allts.append(line.rsplit('/', 1)[1])
print(len(allts))
alreadyts = os.listdir('./difficultvideo/ts')
print(len(alreadyts))
# print(list(set(allts)-set(alreadyts)))
nots = list(set(allts)-set(alreadyts))
for n in nots:
    url = 'https://v7.dious.cc/20220818/mTDCCEsh/1500kb/hls/' + n
    resp = requests.get(url, headers=headers)
    with open('./difficultvideo/ts/' + n, mode='wb') as f:
        f.write(resp.content)
    resp.close()
    print(f'下载{n}成功')
