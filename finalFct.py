import numpy as np
import cv2
import matplotlib.pyplot as plt
from scipy.misc import imread
from scipy import ndimage as ndi
import redExtractor 
from os import walk
import kmeansT
np.set_printoptions(threshold=np.inf)







def main():
    
    #import sys
    #Folder of cropped images
    #lambdaFolder='Test_data/47'
    #scarFolder=*sys.argv[1]
    #cokeFolder=*sys.argv[2]
    

    stickerFolder='sticker/'
    scarFolder='scar/'
    canFolder='can/'
    
    
    scar = []
    for (dirpath, dirnames, filenames) in walk(scarFolder): #value that should be used: 'folderName'
        scar.extend(filenames)

    can = []
    for (dirpath, dirnames, filenames) in walk(canFolder):
        can.extend(filenames)
    
    sticker = []
    for (dirpath, dirnames, filenames) in walk(stickerFolder):
        sticker.extend(filenames)    

    
    folderLength=len(scar)
    
    Final=np.ones([1,folderLength])
    
    for i in range(0,folderLength):
        #scar_lenght_pixels, scar_avg_intensity = kmeansT.main(scarFolder+f[i])
        red_diff = redExtractor.main(canFolder+can[i])
        #circle_lenght_pixels, circle_avg_intensity = kmeansT.main(circleFolder+f[i])
        Final[0,i]=red_diff

        #pixels_1mm_circle = circle_lenght_pixels/20
        #actual_length_circle_mm = pixels_1mm_circle*scar_lenght_pixels

    print(Final)
    

    
    
    

if __name__ == "__main__":
    main()




