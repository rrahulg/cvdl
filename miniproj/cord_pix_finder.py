import cv2




def mouse_event(event, x, y, flags, param):
    print('event: ',event)
    print("x: ", x)
    print("y: ", y)
    print("flags: ", flags)
    print("params: ", param)
    font = cv2.FONT_HERSHEY_PLAIN
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,',',y)
        cord = ". "+str(x) + ', ' + str(y)
        cv2.putText(img,cord,(x,y),font,1,(255,255,255),2)
        
    if event == cv2.EVENT_RBUTTONDOWN:
        b = img[y,x,0]
        g = img[y,x,1]
        r = img[y,x,2]
        
        color_bgr = ". "+str(b) + ', ' + str(g) + ', ' + str(r)
        cv2.putText(img,color_bgr,(x,y),font,1,(0,0,254),2)



cv2.namedWindow(winname='res')
img = cv2.imread('C:/Users/rahul/Downloads/pexels-photo-11883262.jpeg')
img = cv2.resize(img,(500,700))
cv2.setMouseCallback('res', mouse_event)


while True:
    cv2.imshow('res',img)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cv2.destroyAllWindows()
    