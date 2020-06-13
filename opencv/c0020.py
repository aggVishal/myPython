#Histograms of a image
mport numpy as np
import cv2
from matplotlib import pyplot as plt

# img=np.zeros((200,200),np.uint8)
img=cv2.imread("smarties.jpg")
cv2.imshow("image",img)

plt.hist(img.ravel(),256,[0,256] )
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
