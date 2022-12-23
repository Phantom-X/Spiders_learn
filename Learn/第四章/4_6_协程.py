# -*-coding:utf-8-*-
"""
@project:Spiders
@Author: Phantom
@Time:2022/10/29 1:05
@开发环境：windows 10 + python3.8
@IDE：PyCharm2021.3.1
@Email: 2909981736@qq.com
"""

import time
#
#
# def func():
#     print("黎明")
#     time.sleep(3)  # 让当前的线程处于阻塞状态。CPU这时没在这工作
#     print("真的黎明")
#
#
# if __name__ == '__main__':
#     func()

# input()  程序也处于阻塞状态
# request.get(url)  在网络请求返回数据之前，程序也处于阻塞状态
# 一般情况下，程序处于IO操作时，线程都会处于阻塞状态

# 协程: 当程序处于IO操作时，可以选择性的切换到其他任务上
# 在微观上是一个任务一个任务的进行切换，切换条件一般就是IO操作
# 在宏观上,我们能看到的其实就是多个任务一起执行
# 多任务异步操作

# 上面的一切,都是在单线程条件下


# python 编写协程的程序
import asyncio


# async def func():
#     print("你好,我叫xxx")
#
#
# if __name__ == '__main__':
#     g = func()  # 此时的func函数是一个异步协程函数, 此时函数执行得到的是一个协程对象
#     # print(g)
#     asyncio.run(g)  # 协程函数运行需要asyncio模块的支持


# async def func1():
#     print("你好,我叫蔡徐坤1")
#     # time.sleep(3)  # 当程序出现了同步操作时,异步就中断了  requests.get()也是同步
#     await asyncio.sleep(3)
#     print("全民制作人大家好,我叫蔡徐坤1")
#
#
# async def func2():
#     print("你好,我叫蔡徐坤2")
#     # time.sleep(2)
#     await asyncio.sleep(2)
#     print("全民制作人大家好,我叫蔡徐坤2")
#
#
# async def func3():
#     print("你好,我叫蔡徐坤3")
#     # time.sleep(4)
#     await asyncio.sleep(4)
#     print("全民制作人大家好,我叫蔡徐坤3")
#
#
# if __name__ == '__main__':
#     f1 = func1()
#     f2 = func2()
#     f3 = func3()
#     tasks = [f1, f2, f3]
#     t1 = time.time()
#     # 一次性启动多个任务(协程)
#     asyncio.run(asyncio.wait(tasks))
#     print(time.time()-t1)


# 优化代码版:
# async def func1():
#     print("你好,我叫蔡徐坤1")
#     await asyncio.sleep(3)
#     print("全民制作人大家好,我叫蔡徐坤1")
#
#
# async def func2():
#     print("你好,我叫蔡徐坤2")
#     await asyncio.sleep(2)
#     print("全民制作人大家好,我叫蔡徐坤2")
#
#
# async def func3():
#     print("你好,我叫蔡徐坤3")
#     await asyncio.sleep(4)
#     print("全民制作人大家好,我叫蔡徐坤3")
#
#
# async def main():
#     # 第一种写法
#     # f1 = func1()
#     # await f1  # await挂起操作放在协程对象前面
#     # ...
#     # 第二种写法(推荐)
#     tasks = [func1(), func2(), func3()]
#     await asyncio.wait(tasks)
#
#
# if __name__ == '__main__':
#     t1 = time.time()
#     asyncio.run(main())
#     print(time.time() - t1)


# 模拟爬虫
async def download(url):
    print("准备开始下载")
    await asyncio.sleep(2)  # 网络请求
    print("下载完成")


async def main():
    urls = [
        "www.baidu.com",
        "www.bilibili.com",
        "www.163.com"
    ]

    # python3.8以后版本，协程对象要先包装成task对象再丢进 await asyncio.wait, 使用asyncio.create_task()包装
    await asyncio.wait(list(map(lambda x: asyncio.create_task(download(x)), urls)))

if __name__ == '__main__':
    t1 = time.time()
    asyncio.run(main())
    print(time.time()-t1)

