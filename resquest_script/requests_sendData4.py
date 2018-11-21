#!/usr/bin/python
# -*- coding: utf8 -*- 
#*************************************************************************
# File Name: requests_sendData4.py
# Author: huxianyong
# Mail: hxy123@163.com 
# Created Time: Tue 20 Nov 2018 06:10:57 PM CST
#************************************************************************

import json
import requests

url = "http://192.168.1.23:8000/API/"
#对嵌套部分进行json封装
login_data = json.dumps({
    "username": "while",
    "password": "123"

})

data = {
   "type": "user_login",
    "data": login_data,
    "token": ""
}

response = requests.post(url,data = data)
data = response.json()
print(data)