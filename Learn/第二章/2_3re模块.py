# -*-coding:utf-8-*-
"""
@project:Spiders
@Author: Phantom
@Time:2022/10/16 13:43
@开发环境：windows 10 + python3.7
@IDE：PyCharm2021.3.1
@Email: 2909981736@qq.com
"""
import re
'''
# findall: 匹配字符串中所有的符合正则式的内容 返回列表
lst = re.findall(r"\d+", "我的电话是：10086, 女朋友电话是10010")
print(lst)

# finditer: 匹配字符串中所有的符合正则式的内容 返回迭代器 循环迭代器，.group拿到内容
it = re.finditer(r"\d+", "我的电话是：10086, 女朋友电话是10010")
for i in it:
    print(i.group())

# search 找到一个结果就返回 返回的结果是match对象 拿数据需要.group()
s = re.search(r"\d+", "我的电话是：10086, 女朋友电话是10010")
print(s.group())

# match从头匹配
s1 = re.match(r"\d+", "10086, 女朋友电话是10010")
print(s1.group())
'''

'''
# 预加载正则表达式
obj = re.compile(r"\d+")
ret = obj.finditer("我的电话是：10086, 女朋友电话是10010")
for it in ret:
    print(it.group())
'''


s = """
<div class='jay'><span id='1'>张三</span></div>
<div class='tom'><span id='2'>李四</span></div>
<div class='java'><span id='3'>王五</span></div>
<div class='python'><span id='4'>李六</span></div>
"""

objs = re.compile(r"<div class='.*?'><span id='.*?'>(.*?)</span></div>", re.S)  # re.S作用是让.能匹配换行符
res = objs.findall(s)
print(res)

# (?P<分组名字>正则) 可以单独从正则匹配的内容中进一步提取内容
objt = re.compile(r"<div class='.*?'><span id='(?P<id>\d+)'>(?P<res>.*?)</span></div>", re.S)  # re.S作用是让.能匹配换行符
ret = objt.finditer(s)
for it in ret:
    print(it.group("res"))
    print(it.group("id"))

