# -*-coding:utf-8-*-
"""
@project:Spiders
@Author: Phantom
@Time:2022/10/18 1:42
@开发环境：windows 10 + python3.7
@IDE：PyCharm2021.3.1
@Email: 2909981736@qq.com
"""
from lxml import etree

tree = etree.parse("b.html")
# result = tree.xpath('/html/body/ul/li/a/text()')
# result = tree.xpath('/html/body/ul/li[1]/a/text()')  # xpath的顺序从1开始数 []索引

# result = tree.xpath("/html/body/ol/li/a[@href='dapao']/text()")  # [@xxx=xxx] 属性的筛选

# print(result)


# ol_li_list = tree.xpath('/html/body/ol/li')
# for li in ol_li_list:
#     # 从每一个li中提前到文字信息
#     result1 = li.xpath("./a/text()")  # 在li中继续去查找， 相对查找  ./表示当前节点
#     print(result1)
#     result2 = li.xpath("./a/@href")  # /@属性 拿到属性值
#     print(result2)


# print(tree.xpath("/html/body/ul/li/a/@href"))

# F12, 找到想获得的元素，右键复制xpath
print(tree.xpath("/html/body/div[1]/text()"))
