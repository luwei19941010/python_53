#-*-coding:utf-8-*-
# Author:Lu Wei
#
import socket

server=socket.socket()
ip_port=('127.0.0.1',8001)
server.bind(ip_port)
server.listen()

while 1:
    conn,addr=server.accept()
    from_client_msg=conn.recv(1024)
    print(from_client_msg.decode('utf-8'))
    conn.send(b'HTTP/1.1 200 ok\r\n\r\n')
    # conn.send(b'hello girl')
    with open('01momo.html',mode='rb') as f:
        data=f.read()
    conn.send(data)
    conn.close()

