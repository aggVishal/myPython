#insert lines, rectangles,etc in a image
import cv2
import numpy as np

# img=cv2.imread('sample.jpg',1)
img=np.zeros([512,512,3],np.uint8)

img=cv2.line(img,(0,0),(600,300),(255,0,0),5)
img=cv2.rectangle(img,(0,0),(200,300),(0,255,0),5)
img=cv2.circle(img,(300,300),100,(0,0,255),-1)
font=cv2.FONT_HERSHEY_COMPLEX
img=cv2.putText(img,'Vishal',(100,100),font,4,(255,255,255),5,cv2.LINE_AA)

cv2.imshow('Image_name',img)
cv2.waitKey(0)
cv2.destroyAllWindows()