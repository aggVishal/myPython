# Geometrical Shape detector
import cv2
import numpy as np
from matplotlib import pyplot as plt

im=cv2.imread('shapes.jpg')
img=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
_,thresh=cv2.threshold(img,240,255,cv2.THRESH_BINARY)
contours,_=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

for contour in contours:
    approx=cv2.approxPolyDP(contour,0.01*cv2.arcLength(contour,True),True)
    cv2.drawContours(img,[approx],0,(0,0,0),5)
    x=approx.ravel()[0]
    y=approx.ravel()[1]
    if len(approx)==3:
        cv2.putText(im,"Triangle",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,.5,(0,0,0),1)
    elif len(approx)==4:
        x,y,w,h = cv2.boundingRect(contour)
        ratio=float(w)/h
        if ratio>=.95 and ratio<=1.05:
            cv2.putText(im,"Square",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,.5,(0,0,0),1)
        else:
            cv2.putText(im,"Rectangle",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,.5,(0,0,0),1)
    elif len(approx)==5:
        cv2.putText(im,"Pentagon",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,.5,(0,0,0),1)
    elif len(approx)==10:
        cv2.putText(im,"Star",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,.5,(0,0,0),1)
    else :
        cv2.putText(im,"Polygon",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,.5,(0,0,0),1)
    
    

titles=['image']
images=[im]
for i in range(len(images)):
    plt.subplot(1,1,i+1) , plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()