# -*-coding:utf-8-*-
"""
@project:Spiders
@Author: Phantom
@Time:2023/1/12 13:44
@开发环境：windows 10 + python3.8
@IDE：PyCharm2021.3.1
@Email: 2909981736@qq.com
"""
import csv
import json

import requests
import time

from selenium.webdriver.common.by import By
from seleniumwire import webdriver
from selenium.webdriver.chrome.options import Options
from seleniumwire.webdriver import ActionChains

playlisturl = 'https://test.quanjian.com.cn/m/api/search/playlist'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}

option = Options()
option.add_experimental_option('excludeSwitches', ['enable-automation'])
option.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(options=option)


def getmusiclist():
    html = ''
    for request in driver.requests:
        if playlisturl in request.url:
            playlist = request.response.body
            html = html + playlist.decode('utf-8')
            if playlist == None:
                continue
            else:
                break
    jsonlist = json.loads(html)
    l = jsonlist['data']['list']
    namelist = list(map(lambda x: x['name'], l))
    return namelist


def get_musicurl():
    urllist = []
    for request in driver.requests:
        if '.mp3' in request.url:
            urllist.append(request.url)
    return urllist


# 'https://test.quanjian.com.cn/m/api/link?id={ni[1]}&quality=128&_t={_t}&token={token}'


def main():
    driver.get("https://tools.liumingye.cn/music/#/playlist/d7807039303?name=华语金曲千禧年前的旋律")
    time.sleep(30)
    namelist = getmusiclist()
    # print(namelist)
    for i in range(200, 307):
        if namelist[i] == "春夏秋冬 A Balloon's Journey":
            continue
        ActionChains(driver).double_click(driver.find_element(By.XPATH,
                                                              f"/html/body/div[1]/div/div/main/div/div/div/div/div[4]/div[{i + 1}]/div/div[2]/span[contains(text(),'{namelist[i]}')]")).perform()
        time.sleep(14)

    urllist = get_musicurl()
    with open('music.csv', mode='w', encoding='utf-8', newline='') as f:
        csvwriter = csv.writer(f)
        for u in urllist:
            csvwriter.writerow([u])
    driver.quit()
    print(urllist)


if __name__ == '__main__':
    main()
