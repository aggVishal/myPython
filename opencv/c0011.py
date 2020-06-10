#TrackBar_example 2
import cv2 as cv
import numpy as np

def nothing(x):
    print(x)


cv.namedWindow('image')

cv.createTrackbar('CP','image',0,400,nothing)

cv.createTrackbar('switch','image',0,1,nothing)

while(1):
    img=cv.imread('sample.jpg')        
    k=cv.waitKey(1)&0xFF
    if k==27:
        break
    pos=cv.getTrackbarPos('CP','image')   
    font=cv.FONT_HERSHEY_COMPLEX
    cv.putText(img,str(pos),(50,50),font,2,(0,0,255),1) 
    S=cv.getTrackbarPos('switch','image')

    if S==1:
        img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    cv.imshow('image',img)

cv.destroyAllWindows()
