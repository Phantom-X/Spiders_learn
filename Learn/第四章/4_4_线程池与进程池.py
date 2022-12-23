# -*-coding:utf-8-*-
"""
@project:Spiders
@Author: Phantom
@Time:2022/10/23 14:53
@开发环境：windows 10 + python3.8
@IDE：PyCharm2021.3.1
@Email: 2909981736@qq.com
"""
# 线程池：一次性开辟多个线程，直接给线程池提交任务，线程任务的调度交给线程池来完成
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from time import time


def func(name):
    for i in range(1000):
        print(name, i)


if __name__ == '__main__':
    start = time()
    # 创建线程池
    with ThreadPoolExecutor(50) as t:
        for i in range(100):
            t.submit(func, name=f"线程{i}")
    # 等待线程池中的任务全部执行完毕，才继续执行（守护线程）
    print("123")
    print(time() - start)

# from multiprocessing.dummy import Pool as ThreadPool
#
# # 多线程
# start = time()
# pool = ThreadPool(100)
# pool.map(func, ("线程n",))
# pool.close()
# print(time() - start)
