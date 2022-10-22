# -*-coding:utf-8-*-
"""
@project:Spiders
@Author: Phantom
@Time:2022/10/20 0:08
@开发环境：windows 10 + python3.7
@IDE：PyCharm2021.3.1
@Email: 2909981736@qq.com
"""

'''为什么要解密参数:
        直接用加密过后的参数post是可以爬取到的，
        但是每一首歌就得需要一组加密参数，
        就不能批量爬取了，但是如果知道真实参数和解密过程，
        那只要批量获取每个歌曲的id(在url里)，就可以批量爬取了
'''


# js逆向
# 1.找到未加密的参数                      # window.asrsea(参数, xxx,xxx,xxx); 加密函数
# 2.想办法把参数加密(必须参考网易的加密逻辑)  params->encText,encSecKey->encSecKey
# 3.请求到网易, 拿到评论信息

# pip install pycryptodome
import zlib

from Crypto.Cipher import AES
from base64 import b64encode
import json
import requests

url = 'https://music.163.com/weapi/comment/resource/comments/get?csrf_token='

# 请求方式 POST

# 真实参数
data = {
    'csrf_token': "",
    'cursor': "-1",
    'offset': "0",
    'orderType': "1",
    'pageNo': "1",  # 第几条数据
    'pageSize': "20",
    'rid': "R_SO_4_27646205",  # 某个音乐
    'threadId': "R_SO_4_27646205"
}

# 处理加密过程
e = '010001'
f = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
g = '0CoJUm6Qyw8W8jud'
i = 'r7lx0HxFc3Yj4iM2'


def get_encSecKey():
    return "008ca50e02084bccb2301b8dbd3552dfdb1cd7ad927e416559ae3998f8f286fa4e67b5db8f3b7753f71e5ef7560be9c1fa88eb66f5680fb94df7d717821c0d43a158a75c5de0f03fb0d965fa51427cd61d8e6ca8adba708f1546e239056b69deabb61ee8b29f2eadb062d6ba4359c023ef9be2914c2336ce60c61767759f4ef1"


def get_params(data):  # 默认收到字符串
    first = enc_params(data, g)
    second = enc_params(first, i)
    return second


def to_16(data):
    pad = 16 - len(data) % 16
    data += chr(pad) * pad
    return data


def enc_params(data, key):  # 加密过程
    iv = "0102030405060708"
    data = to_16(data)
    aes = AES.new(key=key.encode('utf-8'), IV=iv.encode("utf-8"), mode=AES.MODE_CBC)  # 声明aes对象
    bs = aes.encrypt(data.encode('utf-8'))  # 加密  加密内容长度必须是16的倍数,
    return str(b64encode(bs), 'utf-8')  # 转化成字符串返回


# window.asrsea=d;  window.asrsea就是d函数
"""
    function a(a=16) {  # 随机的16位字符串
        var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
        for (d = 0; a > d; d += 1)  # 循环16次
            e = Math.random() * b.length, # 随机数 1.2345
            e = Math.floor(e),  # 取小于e最大整数 1
            c += b.charAt(e);  # 取字符串e位置 'b'
        return c
    }
    function b(a, b) {  a是要加密的内容
        var c = CryptoJS.enc.Utf8.parse(b)  # b是密钥
          , d = CryptoJS.enc.Utf8.parse("0102030405060708")
          , e = CryptoJS.enc.Utf8.parse(a)  # a是数据
          , f = CryptoJS.AES.encrypt(e, c, {  # c是加密密钥
            iv: d,  # 偏移量
            mode: CryptoJS.mode.CBC  # CBC模式加密
        });
        return f.toString()
    }
    function c(a, b, c) {  # c函数里面不产生随机数
        var d, e;
        return setMaxDigits(131),
        d = new RSAKeyPair(b,"",c),
        e = encryptedString(d, a)
    }
    function d(d, e, f, g) {  d:数据, e:010001, f:很长的固定字符串, g:0CoJUm6Qyw8W8jud 密钥
        var h = {}  # 空对象 
          , i = a(16);  # 16位随机值, 把i设置成定值  
        return h.encText = b(d, g),  # g是密钥
        h.encText = b(h.encText, i),  # 返回的就是params  # i也是密钥
        h.encSecKey = c(i, e, f),     # 返回的是encSecKey e和f是定死的  只要再把i固定,得到的key一定是固定的
        h
    }
    
    encText：
    两次加密：
    数据+g -> b
                -> 第一次加密结果+i 
                        -> b = encText = params
"""

resp = requests.post(url, data={
    # 这里data用json.dumps转换成字符串
    "params": get_params(json.dumps(data)),
    "encSecKey": get_encSecKey()
})
print(resp.text)
resp.close()
