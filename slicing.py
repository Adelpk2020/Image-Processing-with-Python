# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 10:40:30 2018

@author: ashra
"""

import cv2
import numpy
img=cv2.imread('melgy.jpg',0)
h=img.shape[0]
w=img.shape[1]
for i in range (h):
    for j in range (w):
        if img[i,j]>=100 and img[i,j]<=150:
            img[i,j]=255
cv2.imshow('window',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
            