# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 09:31:23 2018

@author: ashra
"""
#do a trackbar with cv2.Namedwindo
import cv2
import numpy
def Update(value):
    img=cv2.imread('melgy.jpg',0)
    print (value)
    h=img.shape[0]
    w=img.shape[1]
    for i in range (h):
     for j in range (w):
      if img[i,j]>=value:
         img[i,j]=255
      elif img[i,j]<value:
        img[i,j]=0
    cv2.imshow('window',numpy.uint8(img))
   
    
# window
cv2.namedWindow('window',cv2.WINDOW_AUTOSIZE)
# Trackbar 
Slider = cv2.createTrackbar('Threshold','window',0,255,Update)
# Initialise first view as the normal image


cv2.waitKey(0)
cv2.destroyAllWindows()
#cv2.Nameddwindow    
    