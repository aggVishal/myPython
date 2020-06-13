# Find and Draw Contours

import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('lena.jpg')
imgray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh=cv2.threshold(imgray,127,255,0)

contours,hierarchy= cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
print(len(contours))

cv2.drawContours(img,contours,-1,(0,255,255),2)

titles=['image','imgray']
images=[img,imgray]
for i in range(len(images)):
    plt.subplot(1,2,i+1) , plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()