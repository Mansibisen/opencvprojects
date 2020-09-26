import cv2
import numpy as np

#img=cv2.imread('lena.jpg',1)
img=np.zeros([512,512,3],np.uint8)
img=cv2.line(img,(0,0),(255,255),(255,0,0),5)
img=cv2.arrowedLine(img,(0,123),(255,255),(134,0,0),12)
img=cv2.rectangle(img,(0,0),(235,235),(234,45,67),-1)
font=cv2.FONT_HERSHEY_DUPLEX

img=cv2.putText(img,'mansi',(0,100),font,3,(0,255,0),4,cv2.LINE_AA)


cv2.imshow('image',img)
cv2.waitKey(3000)

cv2.destroyAllWindows()