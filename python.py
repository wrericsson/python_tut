#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 14:30:11 2017

@author: wr
"""

# coding= utf-8
import json
import sys

if __name__ == '__main__':
    # 将python对象test转换json对象
    test = {"username":"测试","age":16}
    print type(test)
    python_to_json = json.dumps(test,ensure_ascii=False)
    print python_to_json
    print type(python_to_json)

    # 将json对象转换成python对象
    json_to_python = json.loads(python_to_json)
    print type(json_to_python)
    print json_to_python['username']
    print json_to_python['age']