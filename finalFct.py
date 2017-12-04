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
import os





def main():
    
    #import sys
    #Folder of cropped images
    #lambdaFolder='Test_data/47'
    #scarFolder=*sys.argv[1]
    #cokeFolder=*sys.argv[2]
    

    stickerFolder='47/sticker/'
    scarFolder='47/scar/'
    canFolder='47/can/'
    
    # scarFolder='51/scar/'
    
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

    Script_Run = np.load('ScriptRun.npy')    #for saving purposes
    Script_Run = Script_Run+1
    np.save('ScriptRun.npy',Script_Run)
    # os.makedirs('auto_length/'+str(scar_length)+'_run' + str(Script_Run))
    os.makedirs('Output' + str(Script_Run))
    j = 0
    for i in tqdm(range(0,folderLength)):
        finalScar=imread(scarFolder+scar[i])
        finalSticker=imread(stickerFolder+sticker[i])
        #scar_lenght_pixels, scar_avg_intensity = kmeansT.main(scarFolder+f[i])

        scar_length_pixels = get_feature.length(finalScar, Script_Run, j, 3)
        j += 1
        red_diff_sticker, red_img_stic = redExtractor.main('sticker',cv2.imread(stickerFolder+sticker[i]))
        red_img_stic[red_img_stic==0] = 255
        red_img_stic[red_img_stic!=255] = 2
        circle_length_pixels = get_feature.length(red_img_stic, Script_Run, j, 2)
        j += 1
        # avg_red = get_feature.red(finalScar)
        # red_diff_can = redExtractor.main('can',cv2.imread(canFolder+can[i]))
        # red_diff_sticker = redExtractor.main('sticker',cv2.imread(stickerFolder+sticker[i]))
        #circle_lenght_pixels, circle_avg_intensity = kmeansT.main(circleFolder+f[i])
        # Final[i,0]=length
        # Final[i,1]=avg_red
        # Final[i,2]=red_diff_can
        # Final[i,3]=red_diff_sticker
        pixels_1mm_circle = circle_length_pixels/20
        actual_length_circle_mm = pixels_1mm_circle*scar_length_pixels
        print(actual_length_circle_mm)
    
    
    # print('Scar length, Scar Red, can red difference, sticker red difference',Final)
    

    
    
    

if __name__ == "__main__":
    main()




