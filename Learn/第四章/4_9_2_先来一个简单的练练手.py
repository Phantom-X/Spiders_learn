# -*-coding:utf-8-*-
"""
@project:Spiders
@Author: Phantom
@Time:2022/12/23 21:35
@开发环境：windows 10 + python3.8
@IDE：PyCharm2021.3.1
@Email: 2909981736@qq.com
"""

'''
找到m3u8文件，下载
读取m3u8文件，下载视频
合并视频
'''
import requests

# 下载m3u8
# m3u8_url = 'https://v6.cdtlas.com/20220806/RXTYqmTO/hls/index.m3u8'
# resp = requests.get(m3u8_url)
# with open("哲仁王后.m3u8", mode="wb") as f:
#     f.write(resp.content)
# resp.close()

# 解析m3u8文件
n = 1
with open("simplevideo/哲仁王后.m3u8", mode="r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()  # 去掉空白，空格，换行符
        if line.startswith("#"):
            continue
        # print(line)
        # 下载视频片段
        resp = requests.get(line)
        f1 = open(f"simplevideo/{n}.ts", mode="wb")
        f1.write(resp.content)
        f1.close()
        resp.close()
        print(f"{n}.ts over")
        n += 1

