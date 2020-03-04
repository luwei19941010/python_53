#-*-coding:utf-8-*-
# Author:Lu Wei
from urls import urlpatterns
from wsgiref.simple_server import make_server

def application(environ,start_responese):
    # print(environ)
    start_responese('200 ok',[('k1','v1'),('k2','v2')])
    path=environ['PATH_INFO']
    # print(path)
    for i in urlpatterns:
        # print(i)
        if path==i[0]:
            ret=i[1]()
            # print(ret)
            break
    else:
        ret=b'404 404 hhhh'
    return [ret]
httpd=make_server('127.0.0.1',8080,application)
print('Serving HTTP on port 8080...')
httpd.serve_forever()