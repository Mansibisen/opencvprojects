import numpy as np
import cv2
img=cv2.imread('opencv-logo.png')
imggray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh=cv2.threshold(imggray,127,255,0)
_, contours, _=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
print('number of contours'+str(len(contours)))
print(contours[0])
cv2.drawContours(img,contours,-1,(0,255,0),3)



cv2.imshow('image',img)
cv2.imshow('grayimage',imggray)
cv2.waitKey(0)
cv2.destroyAllWindows()