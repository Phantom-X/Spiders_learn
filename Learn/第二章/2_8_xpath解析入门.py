# -*-coding:utf-8-*-
"""
@project:Spiders
@Author: Phantom
@Time:2022/10/18 0:56
@开发环境：windows 10 + python3.7
@IDE：PyCharm2021.3.1
@Email: 2909981736@qq.com
"""
# xpath 是在XML文档中搜索内容的一门语言
# html是xml的一个子集
# 靠结点之间的关系查找的, 如父与子，兄弟结点

# 安装lxml模块
# xpath解析

from lxml import etree

xml = """
<book>
    <id>1</id>
    <name>野花遍地香</name>
    <price>1.23</price>
    <nick>臭豆腐</nick>
    <author>
        <nick id="10086">周大强</nick>
        <nick id="10010">周芷若</nick>
        <nick class="joy">周杰伦</nick>
        <nick class="jolin">蔡依林</nick>
        <div>
            <nick>热热热热热1</nick>
        </div>
        <span>
            <nick>热热热热热2</nick>
            <div>
                <nick>热热热热热3</nick>
            </div>
        </span>
    </author>
    
    <partner>
        <nick id="ppc">胖胖陈</nick>
        <nick id="ppbc">胖胖不陈</nick>
    </partner>
</book>
"""
# parser = etree.XMLParser(encoding='utf-8')
tree = etree.XML(xml)
# result = tree.xpath("/book")  # /表示层级关系， 第一个/是根节点
# result = tree.xpath("/book/name")
# result = tree.xpath("/book/name/text()")  # text() 拿文本
# result = tree.xpath("/book/author//nick/text()")  # // 表示所有后代
# result = tree.xpath("/book/author/*/nick/text()")  # * 表示任意节点 通配符
result = tree.xpath("/book//nick/text()")  # * 表示任意节点 通配符
print(result)
