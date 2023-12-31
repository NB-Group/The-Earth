import requests
from bs4 import BeautifulSoup
import re
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def get_url():
    url = "http://nmc.cn/publish/satellite/FY4A-true-color.htm"
    # 发送GET请求
    response = requests.get(url)
    soup = "error"
    if response.status_code == 200:
        soup = response.text

        # 找到第一个出现的data-id
        data_id_match = soup.find("data-id")
        soup = soup[data_id_match + 1:]
        index = soup.find("\"")
        soup = soup[:index]
        print(soup.replace(" alt=", "").replace("ata-id=", "") + ".JPG")
    else:
        print(f"请求失败，状态码: {response.status_code}")
    return soup.replace(" alt=", "").replace("ata-id=", "") + ".JPG"


if __name__ == '__main__':
    app.run(port=8000)
