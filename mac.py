#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 18:15:50 2018

@author: wr
"""

#encoding=utf-8
__author__ = 'kevinlu1010@qq.com'
from abc import ABCMeta, abstractmethod
import sys

led_group = [[(300, 180, 340, 220), (300, 240, 340, 280)],
             [(230, 220, 250, 240), (270, 220, 290, 240), (310, 220, 330, 240), (350, 220, 370, 240),
              (390, 220, 410, 240), (430, 220, 450, 240), (470, 220, 490, 240), (510, 220, 530, 240)]]



if __name__=='__main__':
    print led_group[1][5]
   