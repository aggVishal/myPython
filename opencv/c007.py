#Color window
import cv2
import numpy as np

def click_event(event,x,y,flags,param ):
    if event==cv2.EVENT_LBUTTONDOWN:
        blue=img[x,y,0]
        green=img[x,y,1]
        red=img[x,y,2]
        
        print(x,',',y)
        cv2.circle(img,(x,y),3,(0,0,255),-1)
        colorImg=np.zeros((512,512,3),np.uint8)
        colorImg[:]=[blue,green,red]
        cv2.imshow('colorImg',colorImg)

# img=np.zeros((512,512,3),np.uint8)
img=cv2.imread('sample.jpg')
cv2.imshow('image',img)
cv2.setMouseCallback('image',click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()