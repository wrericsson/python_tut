#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue May 29 14:34:55 2018

@author: wr
"""
import socket  # socket模块
import commands  # 执行系统命令模块
import json


#qcomm 821  ifaddress the default setting is :192.168.2.11
# HOST = '127.0.0.1'
HOST = '10.60.198.85'
# PORT = 7778
PORT = 7777

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 定义socket类型，网络通信，TCP
s.bind((HOST, PORT))  # 套接字绑定的IP与端口
s.listen(1)  # 开始TCP监听,监听1个请求
setTrackTarget_0 = {"command": "setTrackTarget", "params": {"id": 0, "mode": 2, "control": "start"}}
setTrackTarget_1 = {"command": "setTrackTarget", "params": {"id": 0, "mode": 3, "control": "stop"}}
setTrackTarget_2 = {"command": "getAllPersonInfos", "params": {"looper": "continuous"}}
setTrackTarget_3 = {"command": "switchCamera", "params": {"location": "forward"}}
setTrackTarget_4 = {"command": "switchCamera", "params": {"location": "backward"}}
jsObj_0 = json.dumps(setTrackTarget_0)
jsObj_1 = json.dumps(setTrackTarget_1)
jsObj_2 = json.dumps(setTrackTarget_2)
jsObj_3 = json.dumps(setTrackTarget_3)
jsObj_4 = json.dumps(setTrackTarget_4)

while 1:
    conn, addr = s.accept()  # 接受TCP连接，并返回新的套接字与IP地址
    print 'Connected  by', addr  # 输出客户端的IP地址
    while 1:
        cmd = raw_input("Please input cmd:")  # 与人交互，输入命令

        if cmd == '0':
            conn.sendall(jsObj_0)
        elif cmd == '1':
            conn.sendall(jsObj_1)
        elif cmd == '2':
            conn.sendall(jsObj_2)
        elif cmd == '3':
            conn.sendall(jsObj_3)
        elif cmd == '4':
            conn.sendall(jsObj_4)
        else:
            continue
        response = conn.recv(1024)
        print response
conn.close()  # 关闭连接
