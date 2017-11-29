import numpy as np
import cv2
import matplotlib.pyplot as plt






img = cv2.imread('cokeCan.jpg')
image=cv2.imread('cokeCan.jpg')
print([img[149,149,0],img[149,149,1],img[149,149,2]])
#cv2.imshow('image',img)
trueColour=244
TR,TC,unused=np.shape(img)
redImg=redExtract(img,TR,TC)

cv2.imshow('red',redImg)
total=np.count_nonzero(redImg[:,:,0])

'''
mean1=sum(sum(redImg(:,:,1)))/total;
mean2=sum(sum(redImg(:,:,2)))/total;
mean3=sum(sum(redImg(:,:,3)))/total;

figure
imshow(gim)

gim(:,:,1)=gim(:,:,1)+(trueColour-mean1);
figure
imshow(gim)
'''


def redExtract(image,TR,TC):
    differM=np.zeros([TR,TC])
    for i in range(0,TR):
        for j in range(0,TC):
            differM[i,j]=RGB([int(image[i,j,2]),int(image[i,j,1]),int(image[i,j,0])])
            
    for i in range(0,TR):
        for j in range(0,TC):
            if differM[i,j]<9000:
                image[i,j,:]=0
    return image    
              
def RGB(vec):
    R,G,B=vec
    result=(R-G)*(R-B)
    return result