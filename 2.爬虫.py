#-*-coding:utf-8-*-
# Author:Lu Wei
import requests

ret=requests.get('https://www.douban.com/',headers={
'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Mobile Safari/537.36'
})

with open('db.html',mode='w',encoding='utf-8') as f:
    f.write(ret.text)
# print(ret)