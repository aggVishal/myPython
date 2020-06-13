#Image Gradient and Edge detection

import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('messi5.jpg',cv2.IMREAD_GRAYSCALE)

lap=cv2.Laplacian(img,cv2.CV_64F,ksize=3) #laplacian Gradient
lap=np.uint8(np.absolute(lap))

sobelX=cv2.Sobel(img,cv2.CV_64F,1,0)
sobelY=cv2.Sobel(img,cv2.CV_64F,0,1)
canny=cv2.Canny(img,100,200) # canny edge detection

sobelX=np.uint8(np.absolute(sobelX))
sobelY=np.uint8(np.absolute(sobelY))

mergeSobel=cv2.bitwise_or(sobelX,sobelY)

titles=['image','Laplacian Gradient','sobelX','sobelY','mergeSobel','canny']
images=[img,lap,sobelX,sobelY,mergeSobel,canny]
for i in range(len(images)):
    plt.subplot(2,3,i+1) , plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()