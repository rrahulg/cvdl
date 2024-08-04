# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 11:58:59 2024

@author: rahul
"""

import cv2

img1 = cv2.imread("C:/Users/rahul/Downloads/pexels-photo-11883262.jpeg",-1) 
"""
parameters for imread('location','colorcchannel','unchanged')
colorchannel:
    0: grayscale image
    1: bgr image
unchanged:
    -1: increases the saturation of image
"""
img1 = cv2.resize(img1, (500,700))#width,height
print(img1)
cv2.imshow("original",img1)
cv2.waitKey() #time in milliseconds
cv2.destroyAllWindows()