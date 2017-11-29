import numpy as np
import cv2
import matplotlib.pyplot as plt
from scipy.misc import imread



def main():
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
    
    
    
    
    
    imageArray=['cokeCan.jpg',
                'Test_data/47/47_3.png','54_UF_TW_SMALL.jpg']
    imageNb=len(imageArray)
    '''
    for i in range(0,imageNb):
        myPlot1=plt.subplot(1,2,i+1)
        myPlot1.axis('off') 
        img=plt.imread(imageArray[i])
        plt.imshow(img)
    '''    
      

    trueColour=244
    
    '''
    for i in range(0,imageNb):
        img=plt.imread(imageArray[i])
        TR,TC,unused=np.shape(img)
        redImg=redExtract(img,TR,TC)
        
        myPlot2=plt.subplot(1,2,i+1)
        myPlot2.axis('off') 
        plt.imshow(redImg)
    '''
    img=plt.imread(imageArray[2])
    TR,TC,unused=np.shape(img)
    redImg=redExtract(img,TR,TC)
    
    plt.subplot(1,2,1), plt.imshow(plt.imread(imageArray[2]))#### replace with img to see error
    plt.axis('off') 
    
    plt.subplot(1,2,2), plt.imshow(redImg)
    plt.axis('off')
    
    
    
    
    #total=np.count_nonzero(redImg[:,:,0])
def redExtract(image,TR,TC):
    differM=np.zeros([TR,TC])
    for i in range(0,TR):
        for j in range(0,TC):
            differM[i,j]=RGB([int(image[i,j,0]),int(image[i,j,1]),int(image[i,j,2])])
            
    for i in range(0,TR):
        for j in range(0,TC):
            if differM[i,j]<10000:
                image[i,j,:]=0
    return image    
              
def RGB(vec):
    R,G,B=vec
    result=(R-G)*(R-B)
    return result

if __name__ == "__main__":
    main()



