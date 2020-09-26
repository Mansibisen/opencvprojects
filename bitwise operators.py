import cv2
import numpy as np

img=cv2.imread('image1.png')
img1=np.zeros((512,512,3),np.uint8)
img=cv2.resize(img,(512,512))
img1=cv2.resize(img1,(512,512))
bitand=cv2.bitwise_and(img,img1)
bitxor=cv2.bitwise_xor(img,img1)
bitor=cv2.bitwise_or(img,img1)
bitnot=cv2.bitwise_not(img)

#cv2.imshow('bitxor',bitxor)
#cv2.imshow('bitor',bitor)
cv2.imshow('img',img)
cv2.imshow('bitand',bitand)
cv2.imshow('img1',img1)
#cv2.imshow('bitnot',bitnot)
cv2.waitKey(0)
cv2.destroyAllWindows()