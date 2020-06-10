#How to read, write, show video from camera 
import cv2
import numpy as np

cap=cv2.VideoCapture(0)
fourcc=cv2.VideoWriter_fourcc('X','V','I','D')
out=cv2.VideoWriter('output.avi',fourcc,20,(640,480))

while(cap.isOpened()):
    ret,frame=cap.read()
    if ret==True:
        out.write(frame)
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame',gray)
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
    else:
        break


cap.release()
out.release()
cv2.destroyAllWindows()
