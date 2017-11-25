#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 14:24:45 2017

@author: wr
"""

class ShapeFactory(object):
    '''工厂类'''

    def getShape(self):
      return self.shape_name

class Circle(ShapeFactory):

  def __init__(self):
    self.shape_name = "Circle"
  def draw(self):
    print('draw circle')

class Rectangle(ShapeFactory):
  def __init__(self):
    self.shape_name = "Retangle"
  def draw(self):
    print('draw Rectangle')

class Shape(object):
  '''接口类，负责决定创建哪个ShapeFactory的子类'''
  def create(self, shape):
    if shape == 'Circle':
      return Circle()
    elif shape == 'Rectangle':
      return Rectangle()
    else:
      return None


fac = Shape()
obj = fac.create('Circle')
obj.draw()
obj.getShape()

