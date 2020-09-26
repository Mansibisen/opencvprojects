# diff-gray-blur-threshold-dilated-countour
import cv2
import numpy as np
cap=cv2.VideoCapture('vtest.avi')
ret,frame1=cap.read()
ret,frame2=cap.read()
while cap.isOpened():
    diff=cv2.absdiff(frame1,frame2)
    gray=cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
    blur=cv2.GaussianBlur(gray,(5,5),0)
    _,thresh=cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
    dilated=cv2.dilate(thresh,None,iterations=3)
    _,contours,_=cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    for i in contours:
        (x,y,w,h)=cv2.boundingRect(i)
        if cv2.contourArea(i)<300:
            continue
        else:
            cv2.rectangle(frame1,(x,y),(x+h,y+w),(0,255,0),3)
            cv2.putText(frame1,'status:{}'.format('movement'),(10,20),cv2.FONT_HERSHEY_COMPLEX,3,(255,0,0),3)

    cv2.imshow('feed',frame1)
    frame1=frame2
    ret,frame2=cap.read()
    if cv2.waitKey(40)==27:
        break
cv2.destroyAllWindows()
cap.release()