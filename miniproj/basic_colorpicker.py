import cv2
import numpy as  np

img = np.zeros((300,512,3),np.uint8)
cv2.namedWindow('color picker')

s = "0:OFF \n 1:ON"
cv2.createTrackbar(s, 'color picker', 0, 1, lambda x: None)

cv2.createTrackbar('R', 'color picker', 0, 255, lambda x: None)
cv2.createTrackbar('G', 'color picker', 0, 255, lambda x: None)
cv2.createTrackbar('B', 'color picker', 0, 255, lambda x: None)

while True:
    cv2.imshow('color picker', img)
    if cv2.waitKey(1) & 0xFF == 27:
        break
    
    sp = cv2.getTrackbarPos(s, 'color picker')
    rp = cv2.getTrackbarPos('R', 'color picker')
    gp = cv2.getTrackbarPos('G', 'color picker')
    bp = cv2.getTrackbarPos('B', 'color picker')
    
    if sp == 0:
        img[:] = 0
    else:
        img[:] = [bp,gp,rp]
cv2.destroyAllWindows()

