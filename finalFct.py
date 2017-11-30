import numpy as np
import cv2
import matplotlib.pyplot as plt
from scipy.misc import imread
from scipy import ndimage as ndi
import redExtractor 
from os import walk








def main():
    
    import sys
    #Folder of cropped images
    lambdaFolder=*sys.argv[1]
    scarFolder=*sys.argv[2]
    cokeFolder=*sys.argv[3]
    stickerFolder=*sys.argv[4]
    
    f = []
    for (dirpath, dirnames, filenames) in walk(lambdaFolder): #value that should be used: 'Test_data/47'
        f.extend(filenames)
        break
    
    folderLength=len(scarFolder)
    
    for i in range(0,folderLength):
        a=kmeansT.main(scarFolder[i])
        b=redExtractor.main(cokeFolder[i])
        Final[i]=[a,b]
    
    

    
    
    

if __name__ == "__main__":
    main()




