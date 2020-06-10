# some more cv2  functions
import numpy
import cv2

img=cv2.imread('messi.jpg')
img2=cv2.imread('logo.png')

print(img.shape)
print(img.size)
print(img.dtype)
b,g,r=cv2.split(img)
img=cv2.merge((b,g,r))

# ball=img[280:340,330:390]
# img[273:333,100:160]=ball

ball=img[150:180,156:191]
img[150:180,231:266]=ball

img=cv2.resize(img,(512,512))
img2=cv2.resize(img2,(512,512))

dst=cv2.addWeighted(img,.8,img2,.2,0)
 
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
