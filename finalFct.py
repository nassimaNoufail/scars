import numpy as np
import cv2
import matplotlib.pyplot as plt
from scipy.misc import imread
from scipy import ndimage as ndi
import redExtractor 
from os import walk
import kmeansT
import get_feature
np.set_printoptions(threshold=np.inf)
from tqdm import tqdm






def main():
    
    #import sys
    #Folder of cropped images
    #lambdaFolder='Test_data/47'
    #scarFolder=*sys.argv[1]
    #cokeFolder=*sys.argv[2]
    

    stickerFolder='47/sticker/'
    scarFolder='47/scar/'
    canFolder='47/can/'
    
    
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
    
    Final=np.ones([folderLength,4])
    
    for i in tqdm(range(0,folderLength)):
        finalScar=imread(scarFolder+scar[i])
        finalSticker=imread(stickerFolder+sticker[i])
        #scar_lenght_pixels, scar_avg_intensity = kmeansT.main(scarFolder+f[i])
        scar_length_pixels = get_feature.length(finalScar)
        avg_red = get_feature.red(finalScar)
        red_diff_can, red_img_can = redExtractor.main('can',cv2.imread(canFolder+can[i]))
        red_diff_sticker, red_img_stic = redExtractor.main('sticker',cv2.imread(stickerFolder+sticker[i]))
        circle_length_pixels = get_feature.length(red_img_stic)
        #circle_lenght_pixels, circle_avg_intensity = kmeansT.main(circleFolder+f[i])
        Final[i,0]=scar_length_pixels
        Final[i,1]=avg_red
        Final[i,2]=red_diff_can
        Final[i,3]=red_diff_sticker
        pixels_1mm_circle = circle_length_pixels/20
        actual_length_circle_mm = pixels_1mm_circle*scar_length_pixels
        print(actual_length_circle_mm)
    
    
    print('Scar length, Scar Red, can red difference, sticker red difference \n',Final)
    

    
    
    

if __name__ == "__main__":
    main()



