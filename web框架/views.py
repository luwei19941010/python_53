#-*-coding:utf-8-*-
# Author:Lu Wei

from showdata import showdata
from jinja2 import Template

def html():
    userinfo_data=showdata()
    # print(userinfo_data)
    with open('templates/jinjaweb.html',mode='r',encoding='utf-8') as f:
        data=f.read()
        tem=Template(data)
        data=tem.render({'userinfo':userinfo_data})
        # print(data)
        data=data.encode('utf-8')

        return data
html()

def css():
    with open('static/css/test.css','rb') as f:
        data=f.read()
    return data

def js():
    with open('static/js/test.js','rb') as f:
        data = f.read()
    return data

def jpg():
    with open('static/img/1.jpg', 'rb') as f:
        data = f.read()
    return data

def ico():
    with open('static/img/22.ico', 'rb') as f:
        data = f.read()
    return data