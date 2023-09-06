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

# post请求方式参数不在url中，在表单数据中
url = 'https://fanyi.baidu.com/sug'

# post携带的参数
value = input('请输入要翻译的英文: ')
data = {
    'kw': value
}
resp = requests.post(url, data=data)
# 将响应内容直接处理成json格式数据(字典dict)
print(resp.json())
print(resp.json()['data'][0]['v'])
# 关掉resp
resp.close()
