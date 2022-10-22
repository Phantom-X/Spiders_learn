# -*-coding:utf-8-*-
"""
@project:Spiders
@Author: Phantom
@Time:2022/10/19 17:05
@开发环境：windows 10 + python3.7
@IDE：PyCharm2021.3.1
@Email: 2909981736@qq.com
"""
import requests

# 视频url请求源地址
url = 'https://www.pearvideo.com/video_1734406'
# contId
contId = url.split("_")[1]

# UA和防盗链反爬
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.47',
    # 防盗链：溯源请求地址
    'Referer': url
}
# 视频信息请求url
videoStatus = f'https://www.pearvideo.com/videoStatus.jsp?contId={contId:}&mrd=0.1704261060035379'
resp = requests.get(videoStatus, headers=header)
resp.close()

dic = resp.json()
srcUrl = dic['videoInfo']['videos']['srcUrl']
systemTime = dic['systemTime']
# 拼接真实视频url
videourl = srcUrl.replace(systemTime, f'cont-{contId:}')

# 下载视频
with open("3_3.mp4", mode='wb') as f:
    resp = requests.get(videourl)
    resp.close()
    f.write(resp.content)
