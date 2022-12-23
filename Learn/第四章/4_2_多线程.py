# -*-coding:utf-8-*-
"""
@project:Spiders
@Author: Phantom
@Time:2022/10/23 1:50
@开发环境：windows 10 + python3.8
@IDE：PyCharm2021.3.1
@Email: 2909981736@qq.com
"""

# 线程 进程
# 进程：资源单位，进程包含线程，每一个进程至少要有一个线程
# 线程：执行单位

# 启动程序默认都会有一个主线程

import time

# 单线程
# 14s
# def func():
#     for i in range(1000000):
#         print("func", i)
#
#
# if __name__ == '__main__':
#     start = time.time()
#     func()
#     for i in range(1000000):
#         print("main", i)
#     print(time.time()-start)


from threading import Thread  # 线程类


# 多线程 写法1
# 52.21s
# def func():
#     for i in range(1000000):
#         print("func", i)
#
#
# if __name__ == '__main__':
#     start = time.time()
#     t = Thread(target=func)  # 创建线程并给线程安排任务
#     t.start()  # 该线程状态成为可以开始工作状态，具体的执行时间由CPU决定
#
#     for i in range(1000000):
#         print("main", i)
#
#     print(time.time() - start)


# 多线程 写法2
# class MyThread(Thread):
#     def run(self):  # ->当线程可以执行之后，被执行的就是run方法
#         for i in range(1000):
#             print("子线程", i)
#
#
# if __name__ == '__main__':
#     start = time.time()
#     t = MyThread()
#     t.start()
#     for i in range(1000):
#         print("主线程", i)
#
#     print(time.time() - start)


# 多线程 写法3
# from multiprocessing.dummy import Pool as ThreadPool
#
# def func(s):
#     for i in range(1000000):
#         print("func", i)
#
# if __name__ == '__main__':
#     start = time.time()
#     t = ThreadPool(1)
#     t.map(func, "f")
#     t.close()
#     for i in range(1000000):
#         print("main", i)
#
#     print(time.time()-start)


# 创建多个线程
def func(name):
    for i in range(1000):
        print(name, i)


if __name__ == '__main__':
    start = time.time()
    t1 = Thread(target=func, args=("子线程1",))  # args必须是元组
    t1.start()
    t2 = Thread(target=func, args=("子线程2",))
    t2.start()
    print("时间: ", time.time() - start)
