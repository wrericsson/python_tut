#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 15:46:20 2018

@author: wr
"""
import traceback
from enum import IntEnum
import sys
import os


class coffeeExceptionType(IntEnum):
    TEACH_MODE_START = 0
    TEACH_MODE_STOP = 1
    ARM_VERTICAL_MOVE = 2
    ARM_LEVEL_MODE = 3
    ARM_FORWARD_MOVE = 4
    ARM_SET_RATE = 5
    ARM_SET_POSE_CURVE = 6
    ARM_SET_POSE_LINE = 7
    ARM_GET_POSE = 8
    ARM_MOVE_JOINTS = 9
    ARM_GET_JOINTS = 10
    GRIPPER_SET_SIZE = 11
    GRIPPER_GET_SIZE = 12
    SIGNAL_SYNC = 13
    SIGNAL_WAIT = 14
    SLEEP = 15
    DETECT_CUP = 16
    DETECT_MILKCUP = 17
    DETECT_LED1_ON = 18
    DETECT_LED2_ON = 19
    DETECT_LED1_STROBE = 20
    DETECT_LED2_STROBE = 21
    GRASP_MILKCUP = 22
    UNKNOWN = -1
 
class CoffeeException(Exception):  
    def __init__(self, length,coffeeExceptionType ,file):  
        Exception.__init__(self)  
        self.length = length 
        self.coffeeExceptionType = coffeeExceptionType  
          
  
try:  
    s = raw_input('input a string:')   
    if len(s) < 5:  
        raise CoffeeException(len(s),coffeeExceptionType.DETECT_LED2_STROBE,sys._getframe().f_lineno)  
        
except EOFError:  
    print '触发了EOF错误,按了Ctrl+d'  
    print traceback.format_exc()
except CoffeeException, x:  
    print '输入的字符串只有%d， %d ' % (x.length, x.coffeeExceptionType.value)  
     #print '输入的字符串只有%d， %d  %s, %s' % (x.length, x.coffeeExceptionType.value, x.line,x.file)  
except Exception:  
    print '不知道什么错误！'  
    print traceback.format_exc()
finally:  
    print '有没有异常都会执行这里！'
 
