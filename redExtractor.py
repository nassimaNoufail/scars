import numpy as np
import cv2
import matplotlib.pyplot as plt
from scipy.misc import imread



def main(img):

    
    
     # 'can/14.png' is a good example of image
    imageArray=['cokeCan.jpg',
                'Test_data/47/47_3.png','54_UF_TW_SMALL.jpg']
    imageNb=len(imageArray)
    
    trueColour=244
    windowSize=400
    
    #plot originals in subplot
    '''
    for i in range(0,imageNb):
        myPlot1=plt.subplot(1,2,i+1)
        myPlot1.axis('off') 
        img=plt.imread(imageArray[i])
        plt.imshow(img)
    '''    
      

    
    
    #plot red extracted in subplot
    '''
    for i in range(0,imageNb):
        img=plt.imread(imageArray[i])
        TR,TC,unused=np.shape(img)
        redImg=redExtract(img,TR,TC)
        
        myPlot2=plt.subplot(1,2,i+1)
        myPlot2.axis('off') 
        plt.imshow(redImg)
    '''
    
    
    #Plots the original image:
    '''    
    cv2.namedWindow('original',cv2.WINDOW_NORMAL)
    cv2.resizeWindow('original', windowSize,windowSize)
    cv2.imshow('original',img)
    '''
    TR,TC,unused=np.shape(img)
    redImg=redExtract(img,TR,TC)
    
    
    
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
    
    return differenceInRed

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

if __name__ == "__main__":
    main()



