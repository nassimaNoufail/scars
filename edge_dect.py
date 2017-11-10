import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy.misc import imread



image = cv2.imread("test.jpg")
imageO = image
image_grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# r = image.copy()
# # set blue and green channels to 0
# r[:, :, 0] = 0
# r[:, :, 1] = 0

# cv2.imshow('R-RGB', r)
# cv2.waitKey(0)

image[:, :, 2] = 0  #green to zero
image[:, :, 1] = 0  #blue to zero

image = image[:, :, 0]

laplacian = cv2.Laplacian(image,cv2.CV_64F)
sobelx = cv2.Sobel(image,cv2.CV_64F,1,0,ksize=5)
sobely = cv2.Sobel(image,cv2.CV_64F,0,1,ksize=5)
sobelxy = cv2.Sobel(image,cv2.CV_64F,1,1,ksize=5)

plt.subplot(2,2,1),plt.imshow(image_grey,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2),plt.imshow(image,cmap = 'gray')
plt.title('Only Red Channel'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3),plt.imshow(sobelx,cmap = 'gray')
plt.title('Sobel X Direction'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4),plt.imshow(sobely,cmap = 'gray')
plt.title('Sobel Y Direction'), plt.xticks([]), plt.yticks([])

plt.show()