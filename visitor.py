#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 17:40:41 2017

@author: wr
"""

#!/usr/bin/python
#coding:utf8
'''
Visitor
'''
class Node(object):
    print 'class node'
 
class Armleft(Node):
    print 'Armleft'
 
class ArmRight(Node):
    print 'ArmRight'
 

 
class Excute(object):
    def excute(self, node, *args, **kwargs):
        func = None
        for cls in node.__class__.__mro__:
            func_name = 'Ext'+cls.__name__
            print func_name + ' *__*'
            func = getattr(self, func_name, None)
            if func:
                break
       # print meth;
        if not func:
            func = self.GenericArm
        return func(node, *args, **kwargs)
 
    def GenericArm(self, node, *args, **kwargs):
        print('GenericArm '+node.__class__.__name__)
 
    def ExtArmleft(self, node, *args, **kwargs):
        print('ExtArmleft '+node.__class__.__name__)

    def ExtArmRight(self, node, *args, **kwargs):
        print('ExtArmRight '+node.__class__.__name__)
        return 1
 
a = Armleft()
b = ArmRight()

excuter = Excute() 
excuter.excute(a)
print excuter.excute(b)