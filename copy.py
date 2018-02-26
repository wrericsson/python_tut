#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 13:07:48 2017

@author: wr
"""

import os
import sys
import time
import json
import random
import copy
from subprocess import PIPE, Popen
import commands

def cmdline(command):
    """
    Run command through subProcess.Popen and return the result
    """
    print command
    process = Popen(
        args=command,
        stdout=PIPE,
        shell=True
    )
    return process.communicate()[0]


def filter(filter):
    cam_filterlist = []
    cams_namelist = commands.getoutput("ls /dev/video*").strip().split('\n')
    #print cams_namelist
    for cam_name in cams_namelist:
        print cam_name
        info = cmdline("udevadm info --query=all --name=" + cam_name)
        if info.find(filter) != -1:
            cam_filterlist.append(cam_name)
            print "camera list :",cam_filterlist
    return cam_filterlist
        
        
delta = 10
pos = [-20, -0.2400, 0.1600, 1.5700, 0.0002, 0.0001]
print "pos :" ,pos
newpos = copy.copy(pos)
poslist = [copy.copy(pos),copy.copy(pos),copy.copy(pos),copy.copy(pos)]
#poslist[0][0] = poslist[0][0] +0.06
#poslist[1][0] = poslist[1][0] +0.12
#poslist[2][0] = poslist[2][0] +0.18
#poslist[3][0] = poslist[3][0] +0.24
for item in range(len(poslist)):
   # item[0]  = item[0]  + 10
   poslist[item][0] += item * delta
   if  not int(poslist[item][0]):
       print "test",poslist[item]
filter(filter = "ID_VENDOR_ID=05a3")

#print poslist
    

