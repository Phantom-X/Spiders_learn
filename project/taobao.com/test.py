# -*-coding:utf-8-*-
"""
@project:Spiders
@Author: Phantom
@Time:2022/12/24 17:55
@开发环境：windows 10 + python3.8
@IDE：PyCharm2021.3.1
@Email: 2909981736@qq.com
"""
import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")
speaker.Speak(f"主人，结算提交成功,我已帮你抢到商品啦，请及时支付")
