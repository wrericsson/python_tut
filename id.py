#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 15:14:24 2017

@author: wr
"""


from os import popen
#获取计算机名
def getname():
    print(popen('hostname').read().strip('\n'))
 
def main():
    getname()
    status = []
    status.append({"type": 0, "status": 1})
    status.append({"type": 1, "status": 1})
    status.append({"type": 2, "status": 1})
    status.append({"type": 3, "status": 1})
    status.append({"type": 4, "status": 1})
    status.append({"type": 5, "status": 1})

    for i in range(len(status)):
        if status[i]['type'] == 4:
            status[i]['status'] = -1
    print status
    
if __name__ == "__main__":
    main()