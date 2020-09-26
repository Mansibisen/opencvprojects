import cv2
import numpy as np
apple=cv2.imread('apple.jpg')
orange=cv2.imread('orange.jpg')
print(apple.shape)
print(orange.shape)
apple_orange=np.hstack((apple[:,:256],orange[:,256:]))
#gaussian pyramid of apple
layer=apple.copy()
gp=[layer]
for i in range(6):
    layer=cv2.pyrDown(layer)
    gp.append(layer)

#gaussian pyramid of orange
layer2=orange.copy()
gp2=[layer2]
for i in range(6):
    layer2=cv2.pyrDown(layer2)
    gp2.append(layer2)

# laplacian pyramid of apple
layer=gp[5]
lp=[layer]
for i in range(5,0,-1):
    gaussian_extended=cv2.pyrUp(gp[i])
    result=cv2.subtract(gp[i-1], gaussian_extended)
    cv2.imshow(str(i),result)
# laplacian pyramid of orange
layer2=gp2[5]
lp1=[layer2]
for i in range(5,0,-1):
    gaussian_extended=cv2.pyrUp(gp2[i])
    result=cv2.subtract(gp2[i-1], gaussian_extended)
    cv2.imshow(str(i),result)

#adding both the i ages at each level
apple_orange_add=[]
n=0

for apple_lap,orange_lap in zip(gp,gp2):
    n+=1
    cols,rows,ch=apple_lap.shape
    result=np.hstack((apple_lap[:,0:int(cols/2)],orange_lap[:,int(cols/2):0]))
    apple_orange_add.append(result)
# reconstruct
apple_orange_reconstruct=apple_orange_add[0]
for i in range(1,6):
    apple_orange_reconstruct=cv2.pyrUp(apple_orange_reconstruct)
    apple_orange_reconstruct=cv2.add(apple_orange_add[i] ,apple_orange_reconstruct)


cv2.imshow('apple',apple)
cv2.imshow('orange',orange)
cv2.imshow('apple_orange',apple_orange)
cv2.imshow(' apple_orange_reconstruct', apple_orange_reconstruct)
cv2.waitKey(0)
cv2.destroyAllWindows()