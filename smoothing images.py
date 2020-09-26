import cv2
import numpy as np
from matplotlib import pyplot as plt
#img=cv2.imread('opencv-logo.png')
img=cv2.imread('lena.jpg')

img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
kernel=np.ones((5,5),np.float32)/25
dst=cv2.filter2D(img,-1,kernel)
blur=cv2.blur(img,(5,5))
gblur=cv2.GaussianBlur(img,(5,5),-1)
mblur=cv2.medianBlur(img,5)
blateral=cv2.bilateralFilter(img,9,75,75)
tittles=['img','dst','blur','gblur','mblur','blateral']
images=[img,dst,blur,gblur,mblur,blateral]
for i in range(6):
    plt.subplot(3,2,1+i),plt.imshow(images[i],'gray')
    plt.yticks([]),plt.xticks([])
    plt.title(tittles[i])


plt.show()