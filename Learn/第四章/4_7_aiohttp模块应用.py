# -*-coding:utf-8-*-
"""
@project:Spiders
@Author: Phantom
@Time:2022/12/23 12:05
@开发环境：windows 10 + python3.8
@IDE：PyCharm2021.3.1
@Email: 2909981736@qq.com
"""

# request.get() 同步操作 -> 异步操作
# pip install aiohttp

import asyncio
import time

import aiohttp

urls = [
    'https://www.umei.cc/d/file/20221223/a0d045377a859d04f9e67092da5da338.jpg',
    'https://www.umei.cc/d/file/20221223/01da1f4b26c24f0167a8abfae5d169cd.jpg',
    'https://www.umei.cc/d/file/20221223/9a5a0c92c5d0da424c80975297db78df.jpg'
]


async def aiodownload(url):
    imgname = url.rsplit("/", 1)[1]  # 逆序切割
    # req = aiohttp.ClientSession() <==> requests模块
    # requests.get(), requests.post()
    # req.get(), req.post()
    # 发送请求
    async with aiohttp.ClientSession() as session:  # 用with语句帮助我们自动close
        # 得到图片内容
        async with session.get(url) as resp:
            # resp.text() == resp.text  (before)
            # resp.content.read() == resp.content  (before)
            # 保存到文件
            with open(imgname, mode="wb") as f:
                f.write(await resp.content.read())
    print(imgname, "over")


async def main():
    await asyncio.wait(list(map(lambda x: asyncio.create_task(aiodownload(x)), urls)))


if __name__ == '__main__':
    t1 = time.time()
    # asyncio.run(main())
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    print(time.time()-t1)
