import numpy as np
import cv2
import matplotlib.pyplot as plt
from scipy.misc import imread



def main(choice,img,thres):#choice,img

    
    #cv2.imread('sticker/19.png') # 'can/14.png' is a good example of image
    #choice='sticker'
    
    
    if choice =='can':
        trueColour=244
    elif choice =='sticker':
        trueColour=255 #don't really know what to put, to be discussed   
    
    windowSize=400
    
    
    
    
    #Plots the original image:
    '''    
    cv2.namedWindow('original',cv2.WINDOW_NORMAL)
    cv2.resizeWindow('original', windowSize,windowSize)
    cv2.imshow('original',img)
    '''
    
    TR,TC,unused=np.shape(img)
    redImg=redExtract(img,TR,TC,thres)
    
    
    
    #Plots the image with only red:
    '''    
    cv2.namedWindow('red extracted',cv2.WINDOW_NORMAL)
    cv2.resizeWindow('red extracted', windowSize,windowSize)
    cv2.imshow('red extracted',redImg)
    '''
    
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
    
    return round(differenceInRed), redImg

def redExtract(image,TR,TC,thres):
    differM=np.zeros([TR,TC])
    
    for i in range(0,TR):
        for j in range(0,TC):
            differM[i,j]=RGB([int(image[i,j,2]),int(image[i,j,1]),int(image[i,j,0])])
            
    for i in range(0,TR):
        for j in range(0,TC):
            if differM[i,j]<thres:
                image[i,j,:]=0
            
        
    return image    
              
def RGB(vec):
    R,G,B=vec
    if R-G<0 or R-B<0:
        result=-abs((R-G)*(R-B))   #this corrects the problem where both were negative hence result was positive
    else:
        result=(R-G)*(R-B)
    return result

if __name__ == "__main__":
    main()



