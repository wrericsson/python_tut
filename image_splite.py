#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 17:37:38 2018

@author: wr
"""

import os
from PIL import Image
import numpy as np
from pylab import *


row = 2
col = 2
src = "./1.jpeg"
def splitimage(src, rownum, colnum, dstpath):
    img = Image.open(src)
    w, h = img.size
    imlist = []
    if rownum <= h and colnum <= w:
        print('Original image info: %sx%s, %s, %s' % (w, h, img.format, img.mode))
        print('开始处理图片切割, 请稍候...')

        s = os.path.split(src)
        if dstpath == '':
            dstpath = s[0]
        fn = s[1].split('.')
        basename = fn[0]
        ext = fn[-1]

        num = 0
        rowheight = h // rownum
        colwidth = w // colnum
        for r in range(rownum):
            for c in range(colnum):
                box = (c * colwidth, r * rowheight, (c + 1) * colwidth, (r + 1) * rowheight)
                #img.crop(box).save(os.path.join(os.path.abspath(os.path.dirname(__file__)), basename + '_' + str(num) + '.' + ext), ext)
                im = array(array(img.crop(box)).flatten(),'f')
                imlist.append(im)
                num = num + 1

        print('图片切割完毕，共生成 %s 张小图片。' % num)
    else:
        print('不合法的行列切割参数！')
    return imlist

if __name__=='__main__':
    
    if os.path.isfile(src):
        dstpath = "1.jpeg"
        if (dstpath == '') or os.path.exists(dstpath):
           
            if row > 0 and col > 0:
                imagearray = splitimage(src, row, col, dstpath)
                for i in range(len(imagearray)):
                    im = imagearray[i] # 打开一幅图像，获取其大小
         #           m,n = im.shape[0:2] # 获取图像的大小
          #          imnbr = len(imagearray) # 获取图像的数目
           #         print m,n,imnbr
                print imagearray[0]
                X = np.vstack((imagearray[0],imagearray[1]))  
                
                print np.cov(X)
                #print np.cov(imagearray[0],imagearray[0])
            else:
                print('无效的行列切割参数！')
        else:
            print('图片输出目录 %s 不存在！' % dstpath)
    else:
        print('图片文件 %s 不存在！' % src)