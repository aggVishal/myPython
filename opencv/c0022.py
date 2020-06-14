# Face detection using Haar Cascade
import numpy as np
import cv2

face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade=cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')

# img=cv2.imread('lena.jpg')
cap=cv2.VideoCapture(0)

while cap.isOpened():
    _,img=cap.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    faces=face_cascade.detectMultiScale(gray,1.1,4)

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
        eyes=eye_cascade.detectMultiScale(img)
        
        for(xe,ye,we,he) in eyes:
            cv2.rectangle(img,(xe,ye),(xe+we,ye+he),(255,0,0),2)
    
    cv2.imshow('img',img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cap.release()


