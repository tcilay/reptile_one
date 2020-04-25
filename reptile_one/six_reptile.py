#!/usr/bin/env python
# -- coding:utf-8 --
# -- author:tcilay -- 
# -- date:2020/4/22 --
import requests
from bs4 import BeautifulSoup
import time
import os
from datetime import datetime

url = "https://list.suning.com/0-420031-0.html"
html = requests.get(url)
html.encoding = 'utf-8'
bs_obj = BeautifulSoup(html.text, "html.parser")
li = bs_obj.find_all('img')
x = 0
path = datetime.now().strftime("%Y%m%d%H%M%S%f")
if os.path.exists(path) == 0:
    os.mkdir(path)
current_num = 0
for l in li:
    if 'src' in l.attrs:
        img_url = l.attrs['src']
        print(img_url)
        if "res.suning.cn" in img_url:
            continue
        img_url = "http://"+img_url[2:-13]
        print(img_url)
        img_b = requests.get(img_url).content
        s = path + "/" + str(x) + ".jpg"
        with open(s, 'wb') as f:
            f.write(img_b)
            print("正在下载第{}张图片", format(x))
            x += 1
        current_num += 1
    if current_num > 10:
        break
