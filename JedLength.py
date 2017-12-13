# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 09:58:51 2017

@author: JedRoughley
"""

"""
Takes teh extracted red of a can and returns the amount of mm per pixel
"""
from matplotlib import pyplot as plt
import cv2
import numpy as np
import time
from scipy.spatial.distance import pdist, squareform


def PixelScaleCan(im,type,i,ax):
    if type == 1:
        Ratio = 0.3996 #from coke can
        ActL = 145.4
        ActW = 58.1
    else:
        Ratio = 1 #from coke can
        ActL = 20
        ActW = 20
    #Ratio = 0.001 #from scar
    imOrig = im
    # imOrig = cv2.imread(File)
    # plt.imshow(imOrig)
    # plt.show()
    scar = []
    if len(imOrig.shape) == 3:
        w,h,v = imOrig.shape
    else:
        w,h = imOrig.shape
    if type == 3:
        im = imOrig
    else:
        im = cv2.Canny(imOrig,200,100)
    # plt.imshow(im)
    # plt.show()
    for x in range(w):
        for y in range(h):
            if im[x,y] > 50:
                scar.append((x,y))
            
    start_time = time.time()
    D = squareform(pdist(scar))
    N = np.max(D) #Find the max val
    I = np.argmax(D) #find the index of max val as read
    I_row, I_col = np.unravel_index(I, D.shape) #find the coords of the Ith Val
    # print("--- %s seconds ---" % (time.time() - start_time))
    # print('Max Dist is ' +str(N) +'. Between pixels ' +str(scar[I_row]) +' and ' +str(scar[I_col]))
    
    #Draw the max line
    
    # im[scar[I_row][0],scar[I_row][1]] = 1
    # im[scar[I_col][0],scar[I_col][1]] = 1
    imLine = cv2.line(imOrig,(scar[I_col][1],scar[I_col][0]),(scar[I_row][1],scar[I_row][0]),(0,255,0),5)
    ax.imshow(imLine)
    ax.imshow(imOrig,cmap='pink')
    ax.plot([scar[I_row][1], scar[I_col][1]], [scar[I_row][0], scar[I_col][0]],linewidth=5)
    ax.set_yticklabels([])
    ax.set_xticklabels([])

    
    #plot the histogram
    
    #DFlat = D.flatten()
    #DFloor = DFlat.astype(int)
    #print('Calculating histogram...')
    #plt.hist(DFloor, bins='auto')
    #plt.title("Histogram with 'auto' bins")
    #plt.show()
    #print("--- %s seconds ---" % (time.time() - start_time))
    
    #find Width and length 
    L = np.sqrt(N**2/(Ratio**2+1))
    W = Ratio*L
    # print('Length:' +str(L) +'px')
    # print('Width:' +str(W)+'px')
    # print('Diagonal:' +str(N)+'px\n')
    
    
    
    PixelLength = ActL/L
    # print(str(PixelLength) + ' mm/px')
    if type == 1:
        ax.set_title(PixelLength)
        return PixelLength
    else:
        # ax.set_title(N)
        return N

