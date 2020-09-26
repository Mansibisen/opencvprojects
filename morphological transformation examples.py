#morphologicsl transformation are some simple operations based on the image shape ,normally performed on binary images
#kernal is generally a shape which we are going to apply on image

import cv2
from matplotlib import pyplot as pyp
import numpy as np

#img=cv2.imread('smarties.png',cv2.IMREAD_GRAYSCALE)
img2=cv2.imread('j5.png')
#_,mask= cv2.threshold(img,200,255,cv2.THRESH_BINARY_INV)
kernel=np.ones((2,2),np.uint8)
dillation=cv2.dilate(img2,kernel,iterations=3)
errosion=cv2.erode(img2,kernel,iterations=6)
opening=cv2.morphologyEx(img2,cv2.MORPH_OPEN,kernel)
closing=cv2.morphologyEx(img2,cv2.MORPH_CLOSE,kernel)
mg=cv2.morphologyEx(img2,cv2.MORPH_GRADIENT,kernel)
tophat=cv2.morphologyEx(img2,cv2.MORPH_TOPHAT,kernel)
#tittles=['original img','mask','dillation','errosion','opening','closing','tophat','mg']
tittles=['original img','dillation','errosion','opening','closing','tophat','mg']
#images=[img,mask,dillation,errosion,opening,closing,mg,tophat]
images=[img2,dillation,errosion,opening,closing,mg,tophat]
for i in range(7):
    pyp.subplot(3,4,1+i) ,pyp.imshow(images[i],'gray')
    pyp.xticks([]),pyp.yticks([])
    pyp.title(tittles[i])

pyp.show()