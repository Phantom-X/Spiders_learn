# -*-coding:utf-8-*-
"""
@project:Spiders
@Author: Phantom
@Time:2023/1/3 14:10
@开发环境：windows 10 + python3.8
@IDE：PyCharm2021.3.1
@Email: 2909981736@qq.com
"""
import glob
import os

'''
思路:
    1.拿到主页面的页面源代码，找到iframe
    2.从iframe的页面源代码中拿到m3u8文件。
    3.下载第一层m3u8文件 -> 下载第二层m3u8文件(视频存放路径)
    4.下载视频
    5.下载秘钥，进行解密操作
    6.合并所有ts文件为一个mp4文件
'''

import requests
import asyncio
import aiohttp
import aiofiles
from Crypto.Cipher import AES

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.37'
}
firstm3u8url = 'https://v7.dious.cc/20220818/mTDCCEsh/index.m3u8'


def main(url):
    resp = requests.get(url, headers=headers)
    with open('./difficultvideo/index1.m3u8', mode='w') as f:
        f.write(resp.text)
    resp.close()


def twom3u8():
    with open('./difficultvideo/index1.m3u8', mode='r') as f:
        for line in f:
            line = line.strip()  # 去掉空白，空格，换行符
            if line.startswith("#"):
                continue
            twourl = 'https://v7.dious.cc/' + line
            resp = requests.get(twourl, headers=headers)
            with open('./difficultvideo/index2.m3u8', mode='w') as t:
                t.write(resp.text)
            resp.close()


# 异步协程爬取ts
async def download_ts(url, name, session):
    # print('downloading')
    async with session.get(url, headers=headers) as resp:
        async with aiofiles.open(f'./difficultvideo/ts/{name}', mode='wb') as f:
            await f.write(await resp.content.read())
    print(f'下载{name}成功')


async def aio_downloadts(root):
    tasks = []

    # 解决这个问题：aiohttp.client_exceptions.ServerDisconnectedError: Server disconnected Task exception was never retrieved
    timeout = aiohttp.ClientTimeout(total=600)  # 将超时时间设置为600秒
    connector = aiohttp.TCPConnector(limit=70)  # 将并发数量降低
    # connector = aiohttp.TCPConnector(force_close=True)  # 禁用 HTTP keep-alive

    async with aiohttp.ClientSession(connector=connector, timeout=timeout) as session:  # 提前准备好session
        async with aiofiles.open('./difficultvideo/index2.m3u8', mode='r') as f:
            async for line in f:
                line = line.strip()  # 去掉空白，空格，换行符
                if line.startswith("#"):
                    continue
                tsurl = root + line
                task = asyncio.create_task(download_ts(tsurl, line.rsplit('/', 1)[1], session))
                tasks.append(task)
            await asyncio.wait(tasks)


# 解密
def download_key(url):
    resp = requests.get(url, headers=headers)
    with open('./difficultvideo/key.key', mode='w') as f:
        f.write(resp.text)
    resp.close()
    return resp.text


# 异步协程解密
async def dec_ts(filename, key):
    aes = AES.new(key.encode('utf-8'), IV=b'0000000000000000', mode=AES.MODE_CBC)
    async with aiofiles.open(f'./difficultvideo/ts/{filename}', mode='rb') as f1, \
            aiofiles.open(f'./difficultvideo/already_dec_ts/{filename}', mode='wb') as f2:
        bs = await f1.read()  # 从原文件读取内容
        await f2.write(aes.decrypt(bs))  # 把解密好的内容写入文件
    print(f'{filename}文件处理完毕')


async def aio_dec(key):
    tslist = os.listdir('./difficultvideo/ts')
    # print(tslist)
    await asyncio.wait(list(map(lambda x: asyncio.create_task(dec_ts(x, key)), tslist)))


# 合并
def merge_ts():
    # mac:cat 1.ts 2.ts 3.ts -> xxx.mp4
    # windows:copy /b 1.ts+2.ts+3.ts xxx.mp4

    '''
    # ts太多，，以下方法不可用
    tslist = [f'{i}龙族第0集.ts' for i in range(len(os.listdir('./difficultvideo/already_dec_ts')))]
    s = "+".join(tslist)
    print(os.getcwd())
    os.chdir('./difficultvideo/already_dec_ts')
    print(os.getcwd())
    os.system(f'copy /b {s} 龙族第0集.mp4')
    '''
    tslist = [f'./difficultvideo/already_dec_ts/{i}龙族第0集.ts' for i in
              range(len(os.listdir('./difficultvideo/already_dec_ts')))]
    with open('./difficultvideo/龙族第0集.mp4', mode='wb') as f1:
        for ts in tslist:
            with open(ts, mode='rb') as f2:
                f1.write(f2.read())


if __name__ == '__main__':
    # 爬取
    # main(firstm3u8url)
    # twom3u8()
    # loop1 = asyncio.get_event_loop()
    # loop1.run_until_complete(aio_downloadts('https://v7.dious.cc'))

    # 解密
    # keyurl = 'https://v7.dious.cc' + '/20220818/mTDCCEsh/1500kb/hls/key.key'
    # key = download_key(keyurl)
    # loop2 = asyncio.get_event_loop()
    # loop2.run_until_complete(aio_dec(key))

    # 合并
    merge_ts()
