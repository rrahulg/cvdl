import cv2
import numpy as np

img1 = cv2.imread("../../e7 backup/img/2023-06-15-16-47-22-079.jpg")
img1 = cv2.resize(img1, (500, 700))
img2 = cv2.imread("../../e7 backup/img/2023-05-21-19-07-15-411.jpg")
img2 = cv2.resize(img2, (500, 700))
cv2.imshow("img1", img1)
cv2.imshow("img2", img2)


def blend():
    pass

img = np.zeros([400,400,3])
cv2.namedWindow('win')
cv2.createTrackbar('alpha','win',1,100,blend)

switch = '0: OFF \n1: ON'
cv2.createTrackbar(switch,'win',0,1,blend)
while True:
    s = cv2.getTrackbarPos(switch,'win')
    a = cv2.getTrackbarPos('alpha','win')
    n = float(a/100)
    print(n)
    
    if s==0:
        dst = img[:]
    else:
        dst = cv2.addWeighted(img1,1-n,img2,n,0)
        cv2.putText(dst,str(a),(20,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,125,255),2)
    cv2.imshow('dst',dst)
    k = cv2.waitKey(1) 
    if k == 27:
        break


cv2.waitKey(1)
cv2.destroyAllWindows()
