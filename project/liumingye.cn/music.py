# -*-coding:utf-8-*-
"""
@project:Spiders
@Author: Phantom
@Time:2023/1/12 11:18
@开发环境：windows 10 + python3.8
@IDE：PyCharm2021.3.1
@Email: 2909981736@qq.com
"""
import requests
import time
from seleniumwire import webdriver
from selenium.webdriver.chrome.options import Options
import json

playlisturl = 'https://test.quanjian.com.cn/m/api/search/playlist'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}

option = Options()
option.add_experimental_option('excludeSwitches', ['enable-automation'])
option.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(options=option)
driver.get("https://tools.liumingye.cn/music/#/playlist/d7807039303?name=华语金曲千禧年前的旋律")
time.sleep(6)


def get_playlist():
    """
    获取播放列表
    """
    html = ''
    _t = ''
    token = ''
    for request in driver.requests:
        # print(request.url)
        if playlisturl in request.url:
            data = eval(request.body.decode('utf-8'))
            _t = str(data['_t'])
            token = data['token']
            # print(_t, token)
            playlist = request.response.body
            html = html + playlist.decode('utf-8')
    jsonlist = json.loads(html)
    l = jsonlist['data']['list']
    name_id = list(map(lambda x: (x['name'], x['id']), l))
    return name_id, _t, token


def Download_music(name_id, _t, token):
    for ni in name_id:
        url = f'https://test.quanjian.com.cn/m/api/link?id={ni[1]}&quality=128&_t={_t}&token={token}'
        print(url)
        driver.get(url)
        time.sleep(100)
        text = driver.page_source
        print(text)
        break


def main():
    name_id, _t, token = get_playlist()
    Download_music(name_id, _t, token)
    driver.quit()


if __name__ == '__main__':
    main()
