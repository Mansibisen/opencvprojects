#watch the video
# HSV is used to seperate image illuminance from color information . it is used when we need very varaiaton with color
'''import cv2
import numpy as np
def nothing():
    pass
#cv2.namedWindow('tracking')


while (1):
    img=cv2.imread('workit.png')
    hav=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    l_b=np.array([110,50,50])
    u_b=np.array([130,255,255])
    mask=cv2.inRange(hav, l_b, u_b)
    res=cv2.bitwise_and(img,img,mask=mask)
    cv2.imshow('image', img)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    k=cv2.waitKey(1)&0xFF
    if k==27:
        break

cv2.destroyAllWindows()'''
import cv2
import numpy as np
def nothing(x):
    pass

cap=cv2.VideoCapture(0)
cv2.namedWindow('tracking')
cv2.createTrackbar('LH','tracking',0,255,nothing)
cv2.createTrackbar('LS','tracking',0,255,nothing)
cv2.createTrackbar('LV','tracking',0,255,nothing)
cv2.createTrackbar('UH','tracking',255,255,nothing)
cv2.createTrackbar('US','tracking',255,255,nothing)
cv2.createTrackbar('UV','tracking',255,255,nothing)


while (1):
    #img=cv2.imread('aree.png')
    _, img=cap.read()
    hav=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    l_h=cv2.getTrackbarPos('LH','tracking')
    l_s=cv2.getTrackbarPos('LS', 'tracking')
    l_v=cv2.getTrackbarPos('LV', 'tracking')
    u_h=cv2.getTrackbarPos('UH', 'tracking')
    u_s=cv2.getTrackbarPos('US', 'tracking')
    u_v=cv2.getTrackbarPos('UV', 'tracking')


    l_b=np.array([l_h,l_s,l_v])
    u_b=np.array([u_h,u_s,u_v])
    mask=cv2.inRange(hav, l_b, u_b)
    res=cv2.bitwise_and(img,img,mask=mask)
    cv2.imshow('image', img)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    k=cv2.waitKey(1)&0xFF
    if k==27:
        break
cap.release()
cv2.destroyAllWindows()

