#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 18:42:51 2018

@author: wr
"""

import json


test_dict = {'bigberg': [7600, {1: [['iPhone', 6300], ['Bike', 800], ['shirt', 300]]}]}

with open('objectdetect_config.json', 'r') as load_f:

    load_dict = json.load(load_f)
    print(load_dict)
    print "+++++++++++++++++++++++"

print "========================================="

with open("record.json","w") as dump_f:
    json.dump(load_dict,dump_f)
    

print "========================================="
with open('record.json', 'r') as load_d:
    a_dict = json.load(load_d)
    print(a_dict)
    
