# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 10:48:35 2018

@author: ashra
"""
import cv2
import numpy
img=cv2.imread('melgy1.jpg',0)
h =img.shape[0] #rows
w= img.shape[1] #colume
y=input('select a way zooming or shrinking \n')
y=y.lower()
if y=='zooming':
 d=input('zooming select a a way row or column \n')
 d=d.lower()
 if d=='row':
    f=numpy.ones((h*2,w))
    j=0
    for i in range (h) :
        f[j,:]=img[i,:]
        j+=1
        f[j,:]=img[i,:]
        j+=1
    cv2.imshow('image',numpy.uint8(f))
 elif d=='column':
     f=numpy.ones((h,w*2))
     j=0
     for i in range (w):
         f[:,j]=img[:,i]
         j+=1
         f[:,j]=img[:,i]
         j+=1
     cv2.imshow('image',numpy.uint8(f))
 else:
     print('invaild input')
elif y=='shrinking':
   z=input('shrinking select a a way row or column \n')
   z=z.lower()
   if z=='row':
    f=numpy.ones((int(h/2),w))
    j=0
    for i in range (0,h,2) :
        f[j,:]=img[i,:]
        j=j+1
    cv2.imshow('image',numpy.uint8(f))
   elif z=='column':
     f=numpy.ones((h,int(w/2)))
     j=0
     for i in range (0,w,2):
         f[:,j]=img[:,i]
         j=j+1
     cv2.imshow('image',numpy.uint8(f))
   else:
     print('invaild input')
else:
    print('invaild input')
cv2.waitKey(0)
cv2.destroyAllWindows()