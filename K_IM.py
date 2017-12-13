import numpy as np
import cv2
import matplotlib.pyplot as plt
from scipy.misc import imread
import scipy.misc

from scipy import ndimage as ndi
import os
from features import pre_process
import sys

im = imread(*sys.argv[1:])

import matplotlib.gridspec as gridspec

plt.figure(figsize = (25,5))
gs1 = gridspec.GridSpec(1, 6)
gs1.update(wspace=0, hspace=0) # set the spacing between axes. 

i =[2,3,4,5,6]
for K in i:
	ax = plt.subplot(gs1[K-2])
	imK, canny_edge, imR = pre_process(im, K, type = 0)
	ax.imshow(imK,cmap = 'pink')
	ax.set_yticklabels([])
	ax.set_xticklabels([])

ax = plt.subplot(gs1[5])
ax.imshow(im)
ax.set_yticklabels([])
ax.set_xticklabels([])
plt.savefig('kmeans')
plt.close()