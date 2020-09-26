'''it is a segmentation  technique used to seperate an  object from its background
it involves comparing each pixel with previously defined threhold value
input get diveded into 2
more than tnhreshold
lower than threshold'''


'''import cv2
img=cv2.imread('gradient.png')
_,th1=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
_,th2=cv2.threshold(img,16,255,cv2.THRESH_BINARY_INV)
_,th3=cv2.threshold(img,200,255,cv2.THRESH_TRUNC)
_,th4=cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
_,th5=cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)
cv2.imshow('img',img)
cv2.imshow('th1',th1)
cv2.imshow('th2',th2)
cv2.imshow('th3',th3)
cv2.imshow('th4',th4)
cv2.imshow('th5',th5)
cv2.waitKey(0)
cv2.destroyAllWindows()'''

#adaptive thresholding :- where thresholding is calculated for smaller regionm
import cv2
import numpy as np
img=cv2.imread('sudoku.png',0)
th1=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2);
th2=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2);
cv2.imshow('image',img)
cv2.imshow('th1',th1)
cv2.imshow('th2',th2)
cv2.waitKey(0)
cv2.destroyAllWindows()
