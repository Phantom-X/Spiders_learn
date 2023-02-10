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

# 有序序列
allts = []
with open('./difficultvideo/index2.m3u8', mode='r') as f:
    for line in f:
        line = line.strip()
        if line.startswith('#'):
            continue
        allts.append(line.rsplit('/', 1)[1])

# 已经爬出来的无序序列
alreadyts = os.listdir('./difficultvideo/ts')

# 遍历无序序列，查找在有序序列中的坐标位置，重命名
for i in range(len(alreadyts)):
    address = allts.index(alreadyts[i])
    oldname = os.path.join('./difficultvideo/ts', alreadyts[i])
    newname = os.path.join('./difficultvideo/ts', str(address)+'龙族第0集.ts')
    os.rename(oldname, newname)
    print(i)

