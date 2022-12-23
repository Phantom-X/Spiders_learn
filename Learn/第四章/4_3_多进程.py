# -*-coding:utf-8-*-
"""
@project:Spiders
@Author: Phantom
@Time:2022/10/23 2:15
@开发环境：windows 10 + python3.8
@IDE：PyCharm2021.3.1
@Email: 2909981736@qq.com
"""
from multiprocessing import Process
import time


def func():
    for i in range(10000):
        print("子进程", i)


if __name__ == '__main__':
    # start = time.time()
    p = Process(target=func)
    p.start()
    for i in range(10000):
        print("主进程", i)
    # print(time.time()-start)
