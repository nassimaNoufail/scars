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

    sc=['32/scar/','47/scar/','51/scar/','52/scar/','62/scar/']
    sc = ['52/sticker/','62/sticker/']
    sc=['32/can/','47/can/','51/can/','52/can/','62/can/']
    for n in range(len(sc)):
        scarFolder=sc[n]
        # scarFolder='51/scar/'
        
        scar = []
        for (dirpath, dirnames, filenames) in walk(scarFolder): #value that should be used: 'folderName'
            scar.extend(filenames)
  

        scar.sort()
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
            finalScar=imread(scarFolder+scar[i])
            #scar_lenght_pixels, scar_avg_intensity = kmeansT.main(scarFolder+f[i])
            ax1 = plt.subplot(111)


            red_diff_sticker, red_img_stic = redExtractor.main('sticker',cv2.imread(scarFolder+scar[i]),6000)
            red_img_stic[red_img_stic==0] = 255
            red_img_stic[red_img_stic!=255] = 2
            scar_length_pixels, cannyK_scar = get_feature.length(red_img_stic, Script_Run, j, 3, ax1)
            scar_Jed= JedLength.PixelScaleCan(cannyK_scar,3,i,ax1,red_img_stic)
            j += 1
            # print(circle_length_pixels )
            # elipse = workEllipse.getLength(red_img_stic)
            # print(elipse,'\n')
            j += 1
            # avg_red = get_feature.red(finalScar)
          
            plt.savefig('Output' + str(Script_Run) + '/image_' + str((i+1)))
            plt.close()
        
if __name__ == "__main__":
    main()




