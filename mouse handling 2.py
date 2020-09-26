import cv2
import numpy as np



def click_event(event,x,y,flags,param):
    if event ==cv2.EVENT_LBUTTONDOWN :
        '''cv2.circle(img,(x,y),3,(0,255,0),-1)
        points.append((x,y))
        if len(points)>=2:
            cv2.line(img,points[-1],points[-2],(255,0,0),2)
        cv2.imshow('image',img)'''
        blue=img[x,y,0]
        red=img[x,y,1]
        green=img[x, y, 2]

        cv2.circle(img,(x,y),3,(255,0,255),-1)
        mycolor = np.zeros((512, 512, 3), np.uint8)
        mycolor[:]=[blue,red,green]

        cv2.imshow('image2',mycolor)


img=cv2.imread('lena.jpg')
#img=np.zeros((512,512,3),np.uint8)
cv2.imshow('image',img)
points=[]
cv2.setMouseCallback('image',click_event)


cv2.waitKey(0)
cv2.destroyAllWindows()





