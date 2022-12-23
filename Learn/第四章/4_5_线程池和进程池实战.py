# -*-coding:utf-8-*-
"""
@project:Spiders
@Author: Phantom
@Time:2022/10/28 23:48
@开发环境：windows 10 + python3.7
@IDE：PyCharm2021.3.1
@Email: 2909981736@qq.com
"""
# 1.考虑如何提取单个页面数据
# 2.上线程池，多个页面同时爬取
import time

import requests
from lxml import etree
from lxml.etree import _Element
import csv
from concurrent.futures import ThreadPoolExecutor
from multiprocessing.dummy import Pool as ThreadPool

f = open("data.csv", mode="w", encoding="utf-8", newline="")
csvwriter = csv.writer(f)


def download_one_page(url):
    # 拿到页面源代码
    resp = requests.get(url)
    # 后边加（html的）type可以解决没有提示的问题
    html = etree.HTML(resp.text)  # type:_Element
    resp.close()
    table = html.xpath("/html/body/div/div[4]/div/div[2]/div[2]/table")[0]
    # [position()>=1]可以规定数据范围
    trs = table.xpath("./tbody/tr[position()>=1]")
    # print(len(trs))
    # 将每一行数据保存到csv
    for tr in trs:
        txt = tr.xpath("./td/text()")

        # map或生成器替换一些多余字符
        # txt = list(map(lambda x: x.replace("\n", ""), txt))
        # txt = list((item.replace("\n", "") for item in txt))
        csvwriter.writerow(txt)
    print(url, "提取完毕！")


if __name__ == '__main__':

    # for i in range(1, 10913):  # 单线程效率低下
    #     download_one_page(f"http://www.jnmarket.org/import/list-1_{i:}.html")

    # 线程池
    with ThreadPoolExecutor(50) as t:
        for i in range(1, 200):
            t.submit(download_one_page, f"http://www.jnmarket.org/import/list-1_{i:}.html")
    print("全部爬取完毕！")

    # # 另一种线程池(速度快)
    # start = time.time()
    # pool = ThreadPool(50)
    # urls = tuple()
    # for i in range(1, 200):
    #     urls += (f"http://www.jnmarket.org/import/list-1_{i:}.html",)
    # pool.map(download_one_page, urls)
    # pool.close()
    # print("全部爬取完毕！")
    # print(time.time() - start)
