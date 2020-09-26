'''import cv2
import numpy as np
img=np.zeros((512,512,3),np.uint8)
cv2.namedWindow('image')
def change(x):
    print(x)
cv2.createTrackbar('B','image',0,255,change)
cv2.createTrackbar('G','image',0,255,change)
cv2.createTrackbar('R','image',0,255,change)
switch='lawda'
cv2.createTrackbar(switch,'image',0,255,change)
while(1) :
    cv2.imshow('image',img)
    k=cv2.waitKey(1) & 0xFF
    if k==27:
        break
    b=cv2.getTrackbarPos('B','image')
    g=cv2.getTrackbarPos('G', 'image')
    r=cv2.getTrackbarPos('R', 'image')
    s = cv2.getTrackbarPos(switch, 'image')
    if s==0:
        img[:]=0
    if s==1:
        img[:]=[b,g,r]

    img[:]=[b,g,r]


cv2.destroyAllWindows()'''



import cv2
import numpy as np

cv2.namedWindow('image')
def change(x):
    print(x)
cv2.createTrackbar('B','image',10,400,change)

switch='lawda'
cv2.createTrackbar(switch,'image',0,1,change)
while(1) :
    img=cv2.imread('lena.jpg')
    pos=cv2.getTrackbarPos('B','image')
    font=cv2.FONT_HERSHEY_DUPLEX
    cv2.putText(img,str(pos),(12,234),font,5,(0,255,0),2)
    k=cv2.waitKey(1) & 0xFF
    if k==27:
        break

   
    s = cv2.getTrackbarPos(switch, 'image')
    if s==0:
        pass
    if s==1:
        img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cv2.imshow('image', img)



cv2.destroyAllWindows()





























