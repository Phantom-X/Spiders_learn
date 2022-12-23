# -*-coding:utf-8-*-
"""
@project:Spiders
@Author: Phantom
@Time:2022/12/23 16:19
@开发环境：windows 10 + python3.8
@IDE：PyCharm2021.3.1
@Email: 2909981736@qq.com
"""

# https://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"4306063500"}  => 所有章节的名称（名称，cid）

# https://dushu.baidu.com/api/pc/getChapterContent?data={"book_id":"4306063500","cid":"4306063500|1569782244","need_bookinfo":1}
import time

import requests
import aiohttp
import asyncio
import aiofiles
import json

'''
1.同步操作：拿到所有章节cid 
2.异步操作：下载所有章节内容
'''


async def aiodownload(cid, book_id, title):
    data = {
        "book_id": book_id,
        "cid": f"{book_id}|{cid}",
        "need_bookinfo": 1
    }
    data = json.dumps(data)
    url = f'https://dushu.baidu.com/api/pc/getChapterContent?data={data}'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            dic = await resp.json()
            async with aiofiles.open('./西游记/'+title+'.txt', mode='w', encoding='utf-8') as f:
                await f.write(dic['data']['novel']['content'])
    # print(title)





async def getCatalog(url, book_id):
    resp = requests.get(url)
    resp.close()
    title_cids = list(map(lambda x: [x['cid'], x['title']], resp.json()['data']['novel']['items']))
    await asyncio.wait(list(map(lambda x: asyncio.create_task(aiodownload(x[0], book_id, x[1])), title_cids)))


if __name__ == '__main__':
    book_id = '4306063500'
    url = 'https://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"' + book_id + '"}'
    t1 = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(getCatalog(url, book_id))
    print(time.time() - t1)
