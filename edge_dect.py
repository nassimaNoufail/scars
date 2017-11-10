import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy.misc import imread


image = cv2.imread("test.jpg")
imageO = image
image_grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

imageRed = image[:, :, 0] #only take red
imageRed_grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(imageRed_grey,200,100)
laplacian = cv2.Laplacian(imageRed,cv2.CV_64F)
sobelx = cv2.Sobel(imageRed,cv2.CV_64F,1,0,ksize=5)
sobely = cv2.Sobel(imageRed,cv2.CV_64F,0,1,ksize=5)
sobelxy = cv2.Sobel(imageRed,cv2.CV_64F,1,1,ksize=5)

plt.subplot(2,2,1),plt.imshow(image_grey,cmap = 'gray')
plt.title('Original')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis

plt.subplot(2,2,2),plt.imshow(imageRed_grey,cmap = 'gray')
plt.title('Only Red Channel')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis

plt.subplot(2,2,3),plt.imshow(sobelx,cmap = 'gray')
plt.title('Sobel X Direction')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis

plt.subplot(2,2,4),plt.imshow(sobely,cmap = 'gray')
plt.title('Sobel Y Direction')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis

plt.show()