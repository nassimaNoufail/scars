import matplotlib.pyplot as plt
import skimage
from skimage import data, color, io
from skimage import feature
from skimage.transform import hough_ellipse
from skimage.draw import ellipse_perimeter
import cv2
import numpy as np



def getLength(image):

    np.set_printoptions(threshold=np.inf)
# Load picture, convert to grayscale and detect edges
    image_rgb = cv2.imread(image)
    image_gray = color.rgb2gray(image_rgb)

    s = np.shape(image_gray)
    mag_bin = image_gray.copy()
    max_mag = np.amax(mag_bin)
    mag_bin = (mag_bin/max_mag)*255
    for i in range(s[0]):
    	for j in range(s[1]):
    		if mag_bin[i,j] > 40:
    			# print(mag1[i,j])
    			mag_bin[i,j] = 255
    		else:
    			mag_bin[i,j] = 0
    #cv2.imshow('edges', mag_bin)
    #cv2.waitKey(0)

    # np.uint8(feature.canny(array, sigma=1, ) * 255)
    edges = np.uint8(feature.canny(mag_bin, sigma=2.0)*255)
#print(edges)
# Perform a Hough Transform
# The accuracy corresponds to the bin size of a major axis.
# The value is chosen in order to get a single high accumulator.
# The threshold eliminates low accumulators


#cv2.imshow('edges',edges)
#cv2.waitKey(0)
    result = hough_ellipse(edges,threshold=5,accuracy=10)
    result.sort(order='accumulator')
    print(result)

# Estimated parameters for the ellipse

    COUNT = -1
    best = result[COUNT]
    yc = int(best[1])
    xc = int(best[2])
    a = int(best[3])
    b = int(best[4])
    orientation = best[5]

    while a*b == 0 :
        COUNT = COUNT -1
        best = result[COUNT]
        yc = int(best[1])
        xc = int(best[2])
        a = int(best[3])
        b = int(best[4])
        orientation = best[5]




    # print(yc,xc,a,b,orientation)

# Draw the ellipse on the original image
    cy, cx = ellipse_perimeter(yc, xc, a, b, orientation)
    image_rgb[cy, cx] = (0, 0, 255)
# Draw the edge (white) and the resulting ellipse (red)
    edges = color.gray2rgb(edges)
    edges[cy, cx] = (250, 0, 0)
    # cv2.imshow('cv2', image_rgb)
    # cv2.waitKey(0)
    LEN = 2*b
    return LEN
