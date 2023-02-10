import re


import base64
import io

import requests
from flask import Flask, render_template, request, jsonify
import json
from pathlib import Path

# 传入__name__实例化Flask
app = Flask(__name__)


@app.route('/chatgpt/', methods=['POST'])
# 响应POST消息的预测函数
def get_prediction():
    response = request.get_json()
    value = response['message']
    url = 'https://v1.gptapi.cn'
    print(value)
    data = json.dumps({
        "message": value
    })

    headers = {
        # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.37',
        'Content-Type': 'application/json',
    }

    resp = requests.post(url, data=data, headers=headers)
    # 将响应内容直接处理成json格式数据(字典dict)
    print(resp.text)
    return json.dumps(resp.text)


@app.after_request
def add_headers(response):
    # 允许跨域
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    return response


if __name__ == '__main__':
    app.run(debug=True, host='localhost')
