# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 12:55:15 2024

@author: rahul

@title: video operation
"""

import cv2
cap = cv2.VideoCapture("C:/Users/rahul/Desktop/e7 backup/vid/km_20230713_1080p_60f_20230713_214305.mp4")
print("cap",cap)

while True:
    ret,frame = cap.read()
    cv2.imshow("Frame",frame)
    k = cv2.waitKey(25)
    if k == ord("c") & 0xFF:
        break
cap.release()
cv2.destroyAllWindows()