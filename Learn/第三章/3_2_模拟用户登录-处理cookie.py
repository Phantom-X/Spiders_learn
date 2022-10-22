# -*-coding:utf-8-*-
"""
@project:Spiders
@Author: Phantom
@Time:2022/10/19 1:33
@开发环境：windows 10 + python3.7
@IDE：PyCharm2021.3.1
@Email: 2909981736@qq.com
"""
# 登录 -> 得到cookie
# 带着cookie去请求到书架url -> 暑假上的内容

# 必须得把上面两部操作连起来
# requests每次发送请求都是全新的，不保留cookie, 所以可以使用会话技术session进行请求
import requests

# 会话
session = requests.session()

# 1.登录
url = 'https://passport.17k.com/ck/user/login'
data = {'loginName': '15556271060',
        'password': 'pcw0107'}
resp = session.post(url, data=data)
resp.close()
# print(resp.text)
# print(resp.cookies)  # 查看cookie

# 2.拿书架数据
# 刚才的session中是有cookie的
bookresp = session.get('https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919')
print(bookresp.json())



# 不用session的方法:
header = {
    'Cookie': 'GUID=8ce7c912-c4db-4bc4-a87a-c3824b85ef35; sajssdk_2015_cross_new_user=1; Hm_lvt_9793f42b498361373512340937deb2a0=1666114477; c_channel=0; c_csc=web; __bid_n=183ec2c15a160b30c34207; accessToken=avatarUrl%3Dhttps%253A%252F%252Fcdn.static.17k.com%252Fuser%252Favatar%252F05%252F05%252F83%252F99118305.jpg-88x88%253Fv%253D1666114636000%26id%3D99118305%26nickname%3D%25E4%25B9%25A6%25E5%258F%258B2435AU29d%26e%3D1681667489%26s%3D38104cb48debeda1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2299118305%22%2C%22%24device_id%22%3A%22183ec295cbd49f-09014ee923bcfc-7b555476-1327104-183ec295cbe10cb%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%228ce7c912-c4db-4bc4-a87a-c3824b85ef35%22%7D; Hm_lpvt_9793f42b498361373512340937deb2a0=1666116469'
}
resp = requests.get('https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919', headers=header)
resp.close()
print(resp.json())