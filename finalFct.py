import numpy as np
import cv2
import matplotlib.pyplot as plt
from scipy.misc import imread
from scipy import ndimage as ndi
import redExtractor 
from os import walk








def main():
    
    #import sys
    #Folder of cropped images
    lambdaFolder='Test_data/47'
    #scarFolder=*sys.argv[1]
    #cokeFolder=*sys.argv[2]
    #stickerFolder=*sys.argv[3]
    
    
    f = []
    for (dirpath, dirnames, filenames) in walk(lambdaFolder): #value that should be used: 'Test_data/47'
        f.extend(filenames)
        break
    #print(f)
    #print(lambdaFolder+'/'+f[0])
    folderLength=len(f)
    
    Final=np.ones([1,folderLength])
    for i in range(0,folderLength):
        #a=kmeansT.main(lambdaFolder+'/'+f[i])
        b=redExtractor.main(lambdaFolder+'/'+f[i])
        Final[0,i]=b
    print(Final)
    

    
    
    

if __name__ == "__main__":
    main()




