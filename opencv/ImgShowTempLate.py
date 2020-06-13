import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('sample.jpg')
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)


titles=['image']
images=[img]
for i in range(len(images)):
    plt.subplot(2,3,i+1) , plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()