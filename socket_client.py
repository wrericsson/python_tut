#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue May 29 14:35:16 2018

@author: wr
"""
import json
import time
import socket
import threading
import signal
# import rospy
import sys
import traceback
import StringIO

# qcomm 821  ifaddress the default setting is :192.168.2.11
HOST = '127.0.0.1'
PORT = 7777
setTrackTarget = {"command": "setTrackTarget", "params": {"id": 0, "mode": 2, "control": "start"}}

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 定义socket类型，网络通信，TCP
s.connect((HOST, PORT))  # 要连接的IP与端口

while 1:
    buf = s.recv(1024)  # 把接收的数据定义为变量
    sio = StringIO.StringIO()
    sio.write(buf)
    # jsloads = json.loads(data)
    if buf != '':
        scmd = sio.getvalue().splitlines()
        slen = len(scmd)
        for i in range(slen):
            if len(scmd[i]) == 0:
                continue
            else:
                print scmd[i]
s.close()  # 关闭连接
