# -*-coding:utf-8-*-
"""
@project:Spiders
@Author: Phantom
@Time:2023/1/12 23:18
@开发环境：windows 10 + python3.8
@IDE：PyCharm2021.3.1
@Email: 2909981736@qq.com
"""
import urllib.request, os, json
from lxml import etree
from requests_html import HTMLSession
import execjs, requests, random
import base64, codecs
from Crypto.Cipher import AES


def to_16(key):
    while len(key) % 16 != 0:
        key += '\0'
    return str.encode(key)


def AES_encrypt(text, key, iv):
    bs = AES.block_size
    pad2 = lambda s: s + (bs - len(s) % bs) * chr(bs - len(s) % bs)
    encryptor = AES.new(to_16(key), AES.MODE_CBC, to_16(iv))
    encrypt_aes = encryptor.encrypt(str.encode(pad2(text)))
    encrypt_text = str(base64.encodebytes(encrypt_aes), encoding='utf-8')
    return encrypt_text


def RSA_encrypt(text, pubKey, modulus):
    text = text[::-1]
    rs = int(codecs.encode(text.encode('utf-8'), 'hex_codec'), 16) ** int(pubKey, 16) % int(modulus, 16)
    return format(rs, 'x').zfill(256)


def set_user_agent():
    USER_AGENTS = [
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
        "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
        "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
        "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5"
    ]
    user_agent = random.choice(USER_AGENTS)
    return user_agent


# 获取i值的函数，即随机生成长度为16的字符串
get_i = execjs.compile(r"""
    function a(a) {
        var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
        for (d = 0; a > d; d += 1)
            e = Math.random() * b.length,
            e = Math.floor(e),
            c += b.charAt(e);
        return c
    }
""")


class WanYiYun():
    def __init__(self):
        self.playlist_url = 'https://music.163.com/playlist?id=2624438246'  # 歌单地址
        self.song_url = 'https://music.163.com/weapi/song/enhance/player/url?csrf_token='
        self.g = '0CoJUm6Qyw8W8jud'  # buU9L(["爱心", "女孩", "惊恐", "大笑"])的值
        self.b = "010001"  # buU9L(["流泪", "强"])的值
        # buU9L(Rg4k.md)的值
        self.c = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
        self.i = get_i.call('a', 16)  # 随机生成长度为16的字符串
        self.iv = "0102030405060708"  # 偏移量
        if not os.path.exists("d:/music"):
            os.mkdir('d:/music')
        self.headers = {'User-Agent': set_user_agent(),
                        'Referer': 'https://music.163.com/',
                        'Content-Type': 'application/x-www-form-urlencoded'
                        }

    # 由于歌单内容是通过JS生成的，所以此处运用requests_html这个库来实现JS渲染从而获得歌单
    def get_music_list(self):
        session = HTMLSession()
        response = session.get(self.playlist_url)
        html = etree.HTML(response.content.decode())
        song_list = html.xpath("//ul[@class='f-hide']/li/a")
        music_list = []
        for song in song_list:
            music_id = song.xpath('.//@href')
            music_name = song.xpath('.//text()')
            music_list.append({'id': music_id, 'name': music_name})
        return music_list

    def get_params(self, id):
        encText = str({'ids': "[" + str(id) + "]", 'br': 128000, 'csrf_token': ""})
        return AES_encrypt(AES_encrypt(encText, self.g, self.iv), self.i, self.iv)

    def get_encSecKey(self):
        return RSA_encrypt(self.i, self.b, self.c)

    def download(self):
        music_list = self.get_music_list()
        for music in music_list:
            music_id = music['id'][0].split('=')[1]
            music_name = music['name'][0]
            formdata = {'params': self.get_params(music_id),
                        'encSecKey': self.get_encSecKey()}
            response = requests.post(self.song_url, headers=self.headers, data=formdata)
            download_url = json.loads(response.content)["data"][0]["url"]
            if download_url:
                try:
                    # 根据音乐url地址，用urllib.request.retrieve直接将远程数据下载到本地
                    urllib.request.urlretrieve(download_url, 'd:/music/' + music_name + '.mp3')
                    print('Successfully Download:' + music_name + '.mp3')
                except:
                    print('Download wrong~')


if __name__ == '__main__':
    wanyiyun = WanYiYun()
    wanyiyun.download()
