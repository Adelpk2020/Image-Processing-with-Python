# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 09:53:36 2018

@author: ashra
"""

import cv2
import matplotlib.pyplot as plt
import numpy 


img=cv2.imread('melgy.jpg',0)
h=img.shape[0]
w=img.shape[1]

biggest = numpy.amax(img)
x= [biggest]
for i in range(biggest):
    x.append(0)
for i in range (h):
    for j in range (w):
        x[img[i][j]]+=1
f=numpy.zeros((256,1000))
h=f.shape[0]
w=f.shape[1]
for i in range (len(x)):
        f[i,0:x[i]]=255
plt.imshow(f)
plt.show(f)  