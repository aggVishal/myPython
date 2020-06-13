# Find and Draw Contours
import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('logo.png')
imgray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)



titles=['image','imgray']
images=[img,imgray]
for i in range(len(images)):
    plt.subplot(2,1,i+1) , plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()