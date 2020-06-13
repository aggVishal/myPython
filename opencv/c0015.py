#   Smoothing or Bluring

#1. Homogeneous filter
#2. Blur method or averaging
#2. Gaussian filter (for removing high freq noise)
#3. Median filter (salt and pepper filter)
#4. Bilateral Filter (filtering while keeping edges sharp)

import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('sample.jpg')
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

kernal=np.ones((5,5),np.float32)/25

HF=cv2.filter2D(img,-1,kernal)  # for Homogeneous Filter (kernal is divied by 25 in formula)
blur=cv2.blur(img,(5,5))  #Blur method
gau=cv2.GaussianBlur(img,(5,5),0)  # Gaussian Filter
median=cv2.medianBlur(img,5) #median filter
bilateralfilter=cv2.bilateralFilter(img,9,75,75) # Bilateral Filter

titles=['image','Homogeneous','Blur','Gaussian','Median Blur','bilateralfilter']
images=[img,HF,blur,gau,median,bilateralfilter ]
for i in range(len(images)):
    plt.subplot(2,3,i+1) , plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()