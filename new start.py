import cv2
import numpy as np
from matplotlib import pyplot as plt
#import matplotlib.pyplot as plt
#img=cv2.imread('lena.jpg')
#cv2.imshow('image',img)
#img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

#plt.imshow(img)
#plt.xticks([]),plt.yticks([])
#plt.show()



#cv2.waitKey(0)
#cv2.destroyAllWindows()

img=cv2.imread('gradient.png')
_,th1=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
_,th2=cv2.threshold(img,16,255,cv2.THRESH_BINARY_INV)
_,th3=cv2.threshold(img,200,255,cv2.THRESH_TRUNC)
_,th4=cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
_,th5=cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)
tittles=['original image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images=[img,th1,th2,th3,th4,th5]

for i in range(6):
    plt.subplot(2,3,1+i),plt.imshow(images[i],'gray')
    plt.title(tittles[i])
    plt.xticks([]),plt.yticks([])
plt.show()