import numpy as np
import cv2
img=cv2.imread('lena.jpg')
img2=cv2.imread('toy-wallpapers-hd-70771-9654546.png')
img=cv2.resize(img,(512,512))
img2=cv2.resize(img2,(512,512))
print(img.size)
print(img.shape)
print(img.dtype)
b,g,r=cv2.split(img)
img=cv2.merge((b,g,r))
#lawda=img[280:340,330:390]
#img[273:333,100:160]=lawda
#dst=cv2.add(img,img2);
dst=cv2.addWeighted(img,.4,img2,.9,.8);
cv2.imshow('image',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()