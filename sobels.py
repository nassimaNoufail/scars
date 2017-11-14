import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import imread
from scipy import ndimage as ndi
from skimage import feature
import cv2

im = imread('test4.jpg')
im = im[:,:,0]
plt.subplot(2,2,1),plt.imshow(im,cmap='pinkf')

#rotate image - in degrees
im = ndi.rotate(im, 90, mode='constant')

imG = ndi.gaussian_filter(im, 4)
plt.subplot(2,2,2),plt.imshow(im)

# Compute the Canny filter for two values of sigma
edges1 = feature.canny(im)
edges2 = feature.canny(im, sigma=3)
canny_edge = cv2.Canny(im,200,100)

plt.subplot(2,2,3),plt.imshow(edges2)
plt.subplot(2,2,4),plt.imshow(canny_edge)
plt.show()