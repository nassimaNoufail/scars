import numpy as np
import cv2
import matplotlib.pyplot as plt
from scipy.misc import imread



def main():#choice,img

    
    img=cv2.imread('47/scar/13.png') # 'can/14.png' is a good example of image
    choice='can'
    thres=5000
    
    if choice =='can':
        trueColour=244
    elif choice =='sticker':
        trueColour=255 #don't really know what to put, to be discussed   
    
    windowSize=400
    
    
    
    
    #Plots the original image:
    #'''    
    #cv2.namedWindow('original',cv2.WINDOW_NORMAL)
    #cv2.resizeWindow('original', windowSize,windowSize)
    cv2.imshow('original',img)
    #cv2.imwrite('badScar1before.png',img)
    #'''
    
    TR,TC,unused=np.shape(img)
    totalSize=np.size(img[:,:,1])
    redImg,nonZ=redExtract(img,TR,TC,thres)
    print('ratio=',nonZ/totalSize)
    
    
    #Plots the image with only red:
    #'''    
    #cv2.namedWindow('red extracted',cv2.WINDOW_NORMAL)
    #cv2.resizeWindow('red extracted', windowSize,windowSize)
    cv2.imshow('red extracted',redImg)
    #cv2.imwrite('badScar1after.png',redImg)
    #'''
    
    total=np.count_nonzero(redImg[:,:,2])
    
    mean0=np.sum(redImg[:,:,2])/total  #  mean of red pixels
    
    #Plots image with increased red
    '''
    for i in range(0,TR):
        for j in range(0,TC):
            if redImg[i,j,2]!=0:
                if redImg[i,j,2]+(trueColour-mean0)>255:
                    redImg[i,j,2]=255
                else:
                    redImg[i,j,2]+=(trueColour-mean0)     
                      
    
    cv2.namedWindow('red increased',cv2.WINDOW_NORMAL)
    cv2.resizeWindow('red increased', windowSize,windowSize)
    cv2.imshow('red increased',redImg)
    '''
    
    meanFinal=np.sum(redImg[:,:,2])/total
                    
    differenceInRed=trueColour-mean0
    print('red=',round(mean0))
    return round(differenceInRed),img
    

def redExtract(image,TR,TC,thres):
    differM=np.zeros([TR,TC])
    for i in range(0,TR):
        for j in range(0,TC):
            differM[i,j]=RGB([int(image[i,j,2]),int(image[i,j,1]),int(image[i,j,0])])
            
    for i in range(0,TR):
        for j in range(0,TC):
            if differM[i,j]<thres:
                image[i,j,:]=0
            
        
    total=np.count_nonzero(image[:,:,2])   
    return image,total    
              
def RGB(vec):
    R,G,B=vec
    if R-G<0 or R-B<0:
        result=-abs((R-G)*(R-B))   #this corrects the problem where both were negative hence result was positive
    else:
        result=(R-G)*(R-B)
    return result

if __name__ == "__main__":
    main()