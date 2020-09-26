import cv2
import numpy as np

img=cv2.imread('lena.jpg')
'''
cv2.imshow('image',img)
pd1=cv2.pyrDown(img)
pd2=cv2.pyrDown(pd1)
ud2=cv2.pyrUp(pd2)
cv2.imshow('pd1',pd1)
cv2.imshow('pd2',pd2)
cv2.imshow('ud2',ud2)'''
layer=img.copy()
gp=[layer]
for i in range(6):
    layer=cv2.pyrDown(layer)
    gp.append(layer)
    #cv2.imshow(str(i),layer)
#laplacian images
layer=gp[5]
lp=[layer]
for i in range(5,0,-1):
    gausian_extended=cv2.pyrUp(gp[i])
    laplacian=cv2.subtract(gp[i-1], gausian_extended)
    cv2.imshow(str(i),laplacian)


cv2.waitKey(0)
cv2.destroyAllWindows()