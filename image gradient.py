import cv2
import numpy as np
from matplotlib import pyplot as plt
#  in laplacian image borders are seen
#img=cv2.imread('messi5.jpg',cv2.IMREAD_GRAYSCALE)
img=cv2.imread('sudoku.png',cv2.IMREAD_GRAYSCALE)
lap=cv2.Laplacian(img,cv2.CV_64F,ksize=3)
lap=np.uint8(np.absolute(lap))
sobelX=cv2.Sobel(img,cv2.CV_64F,1,0)
sobelY=cv2.Sobel(img,cv2.CV_64F,0,1)
sobelX=np.uint8(np.absolute(sobelX))
sobelY=np.uint8(np.absolute(sobelY))
sobelcombined=cv2.bitwise_or(sobelX,sobelY)

titles=['image','lap','sobelX','sobelY','sobelcombined']
images=[img,lap,sobelX,sobelY,sobelcombined]
for i in range(5):
    plt.subplot(3,2,i+1),plt.imshow(images[i],'gray')
    plt.xticks([]),plt.yticks([])
    plt.title(titles[i])


plt.show()