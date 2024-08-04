import cv2
import pyautogui as p
import numpy as np
import time


resolution = p.size()
file_name = input('enter filename or path ')
fps = 60
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output = cv2.VideoWriter(file_name,fourcc,fps,resolution)

cv2.namedWindow('LiveRecording',cv2.WINDOW_NORMAL)

while True:
    img = p.screenshot()
    f = np.array(img)
    f = cv2.cvtColor(f,cv2.COLOR_RGB2BGR)
    output.write(f)
    cv2.imshow('LiveRecording',f)
    if cv2.waitKey(1) == ord('c'):
        break
output.release()
cv2.destroyAllWindows()