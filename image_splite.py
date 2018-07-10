#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 17:37:38 2018

@author: wr
"""

import os
from PIL import Image
import numpy as np


def splitimage(src, rownum, colnum, dstpath):
    img = Image.open(src)
    w, h = img.size
    imlist = []
    if rownum <= h and colnum <= w:
        print('Original image info: %sx%s, %s, %s' % (w, h, img.format, img.mode))
        if (w != 1920 or h != 1080):
            print "error:input jpeg size is uncorrect"
            exit()
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
                #
                if ((num == row * col / 4 - 1) or num == 0 or (num == (col - 1)) or (num == row * col - 1)) or (
                            num == (row - 1) * (col)):
                    #   img.crop(box).save(os.path.join(os.path.abspath(os.path.dirname(__file__)), basename + '_' + str(num) + '.' + ext), ext)
                    im = np.array(np.array(img.crop(box)).flatten(), 'f')
                    imlist.append(im)
                num = num + 1
    else:
        print('illegle input arguments！')
    return imlist


def calculate_diff(src, row, col, dest):
    center_location_index = 2
    if os.path.isfile(src):

        if (src == '') or os.path.exists(src):

            if row > 0 and col > 0:
                imagearray = splitimage(src, row, col, src)
                imagearray_comp = splitimage(dest, row, col, dest)
                norm_list = []
                for i in range(len(imagearray)):
                    # im = imagearray[i] # 打开一幅图像，获取其大小#
                    # m,n = im.shape[0:2] # 获取图像的大小
                    # imnbr = len(imagearray) # 获取图像的数目
                    # print m,n,imnbr
                    # print imagearray[0]
                    # print len(imagearray)

                    # X = np.vstack((imagearray_comp[i], imagearray[i]))
                    norm_list.append(np.linalg.norm(imagearray[i] - imagearray[center_location_index]))
                    # print np.cov(X)
                    # print np.cov(imagearray[0],imagearray[0])
                return norm_list
            else:
                print('parameters is unavailble！')
        else:
            print('output folder is not exist: %s  ！' % dstpath)
    else:
        print('output file is not exist %s ！' % src)


if __name__ == '__main__':
    row = 9
    col = 16
    src = "2.jpeg"
    dest = "6.jpeg"
    diff = calculate_diff(src, row, col, dest)
    print diff
