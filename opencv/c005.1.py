# More advanced mouse click events
import cv2
import numpy as np

drawing=False
mode=True
xi,yi=-1,-1

def click_event(event,x,y,flags,param ):
    global drawing,mode,xi,yi
    if event==cv2.EVENT_LBUTTONDOWN:
        drawing=True
        xi,yi=x,y

    elif event==cv2.EVENT_MOUSEMOVE:
        if drawing==True:
            if mode==True:
                cv2.rectangle(img,(xi,yi),(x,y),(0,0,255),-1)
            else:
                cv2.circle(img,(x,y),5,(0,255,255),-1)
    
    elif event==cv2.EVENT_LBUTTONUP:
        drawing=False
        if mode==True:
            cv2.rectangle(img,(xi,yi),(x,y),(0,0,255),-1)
        else:
            cv2.circle(img,(x,y),5,(0,255,255),-1)
   


img=np.zeros((720,720,3),np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',click_event)

while(1):
    cv2.imshow('image',img)
    k= cv2.waitKey(1) & 0xFF
    if k==ord('m'):
        mode=not mode
    elif k==27:
        break    

cv2.destroyAllWindows()