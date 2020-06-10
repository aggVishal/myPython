#Put date and time in a video
import cv2
import numpy as np
import datetime

cap=cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# cap.set(3,3000)        # 3 represents CAP_PROP_FRAME_WIDTH
# cap.set(4,3000)        # 4 represents CAP_PROP_FRAME_HEIGHT

while(cap.isOpened()):
    ret,frame=cap.read()
    if ret==True:
        font=cv2.FONT_HERSHEY_COMPLEX
        text='width: '+str(cap.get(3)) + ' Height: '+ str(cap.get(4))
        dateandtime=str(datetime.datetime.now())

        frame=cv2.putText(frame,dateandtime,(10,50),font,1,(0,255,255),2,cv2.LINE_AA)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
    else:
        break


cap.release()
cv2.destroyAllWindows()