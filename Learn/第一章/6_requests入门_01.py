# -*-coding:utf-8-*-
"""
@project:Spiders
@Author: Phantom
@Time:2022/10/10 0:28
@开发环境：windows 10 + python3.7
@IDE：PyCharm2021.3.1
@Email: 2909981736@qq.com
"""
import requests
query = input('输入搜索内容: ')
# get请求方式参数直接拼在url中
url = f'https://www.sogou.com/web?query={query:}'

# 伪装请求设备
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.37'
}
resp = requests.get(url, headers=headers)
# 请求状态码
print(resp)
# 请求方式
print(resp.request)
# 响应内容转换成text返回
print(resp.text)
# 返回cookie
print(resp.cookies)
# 响应内容字符集
print(resp.encoding)

# 关掉resp
resp.close()