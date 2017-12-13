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
import workEllipse
import JedLength



def main():
    
    #import sys
    #Folder of cropped images
    #lambdaFolder='Test_data/47'
    #scarFolder=*sys.argv[1]
    #cokeFolder=*sys.argv[2]
    st=['32/sticker/','47/sticker/','51/sticker/','52/sticker/','62/sticker/']
    sc=['32/scar/','47/scar/','51/scar/','52/scar/','62/scar/']
    c=['32/can/','47/can/','51/can/','52/can/','62/can/']
    st=['new/sticker/']
    sc=['new/scar/']
    # c=['62/can/']
    for n in range(5):
        canFolder=c[n]
        stickerFolder=st[n]
        scarFolder=sc[n]
        # scarFolder='51/scar/'
        
        scar = []
        for (dirpath, dirnames, filenames) in walk(scarFolder): #value that should be used: 'folderName'
            scar.extend(filenames)

        # can = []
        # for (dirpath, dirnames, filenames) in walk(canFolder):
        #     can.extend(filenames)
        
        sticker = []
        for (dirpath, dirnames, filenames) in walk(stickerFolder):
            sticker.extend(filenames)    

        scar.sort()
        sticker.sort()
        folderLength=len(scar)
        
        Final=np.ones([folderLength,4])

        Script_Run = np.load('ScriptRun.npy')    #for saving purposes
        Script_Run = Script_Run+1

        np.save('ScriptRun.npy',Script_Run)
        # os.makedirs('auto_length/'+str(scar_length)+'_run' + str(Script_Run))
        os.makedirs('Output' + str(Script_Run))
        j = 0
        for i in range(0,folderLength):
            print(scar[i])
            print(sticker[i])
            finalScar=imread(scarFolder+scar[i])
            finalSticker=imread(stickerFolder+sticker[i])
            #scar_lenght_pixels, scar_avg_intensity = kmeansT.main(scarFolder+f[i])
            ax1 = plt.subplot(2,3,1)
            ax2 = plt.subplot(2,3,2)
            ax3 = plt.subplot(2,3,3)
            ax4 = plt.subplot(2,3,4)
            ax5 = plt.subplot(2,3,5)
            ax6 = plt.subplot(2,3,6)


            scar_length_pixels, cannyK_scar = get_feature.length(finalScar, Script_Run, j, 3, ax1)
            j += 1
            red_diff_sticker, red_img_stic = redExtractor.main('sticker',cv2.imread(stickerFolder+sticker[i]),6000)
            red_img_stic[red_img_stic==0] = 255
            red_img_stic[red_img_stic!=255] = 2
            # red_dif_can, red_img_can = redExtractor.main('can',cv2.imread(canFolder+can[i]),9000)

            circle_length_pixels, imK_stic = get_feature.length(red_img_stic, Script_Run, j, 2, ax2)
            circle_Jed = JedLength.PixelScaleCan(red_img_stic,0,i,ax3)
            # coke_Jed = JedLength.PixelScaleCan(red_img_can,1,i,ax4)
            scar_Jed = JedLength.PixelScaleCan(cannyK_scar,3,i,ax5)
            # print(circle_length_pixels )
            # elipse = workEllipse.getLength(red_img_stic)
            # print(elipse,'\n')
            j += 1
            # avg_red = get_feature.red(finalScar)
            # red_diff_can = redExtractor.main('can',cv2.imread(canFolder+can[i]))
            # red_diff_sticker = redExtractor.main('sticker',cv2.imread(stickerFolder+sticker[i]))
            #circle_lenght_pixels, circle_avg_intensity = kmeansT.main(circleFolder+f[i])
            # Final[i,0]=length
            # Final[i,1]=avg_red
            # Final[i,2]=red_diff_can
            # Final[i,3]=red_diff_sticker
            pixels_1mm_circle = circle_length_pixels/2000
            pixels_1mm_circle_Jed = circle_Jed/2000

            actual_length_circle_mm = pixels_1mm_circle*scar_length_pixels
            actual_length_circle_mm_Jed = pixels_1mm_circle_Jed*scar_length_pixels

            actual_H = pixels_1mm_circle*scar_Jed
            actual_D = pixels_1mm_circle_Jed*scar_Jed

            # scar_coke= coke_Jed*scar_Jed
            x = [0,1]
            y = [0,0]
            ax6.plot(x,y, label = 'matt H '+ str(round(actual_length_circle_mm,1)))
            ax6.plot(x,y, label = 'matt D '+str(round(actual_length_circle_mm_Jed,1)))
            ax6.plot(x,y, label = 'Jed H '+ str(round(actual_H,1)))
            ax6.plot(x,y, label = 'Jed D '+str(round(actual_D,1)))
            # ax6.plot(x,y, label = 'coke ' + str(round(scar_coke,1)))
            ax6.legend(loc="upper right")
            plt.savefig('Output' + str(Script_Run) + '/image_' + str((i+1)))
            plt.close()
        
        # print('Scar length, Scar Red, can red difference, sticker red difference',Final)
    

    
    
    

if __name__ == "__main__":
    main()




