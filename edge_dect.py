import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy.misc import imread


image = cv2.imread("test4.jpg")
imageO = image
image_grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

imageRed = image[:, :, 0] #only take red
imageRed_grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

canny_edge = cv2.Canny(imageRed_grey,200,100)
laplacian = cv2.Laplacian(imageRed,cv2.CV_64F)
k = 1
sobelx = cv2.Sobel(image_grey,cv2.CV_64F,1,0,ksize=k)
sobely = cv2.Sobel(imageRed,cv2.CV_64F,0,1,ksize=k)
mag = np.sqrt(sobelx**2 + sobely**2)

s = np.shape(mag)
mag_bin = mag.copy()
max_mag = np.amax(mag_bin)
mag_bin = (mag_bin/max_mag)*255
for i in range(s[0]):
	for j in range(s[1]):
		if mag_bin[i,j] > 40:
			# print(mag1[i,j])
			mag_bin[i,j] = 255
		else:
			mag_bin[i,j] = 0



plt.subplot(2,2,1),plt.imshow(image_grey,cmap = 'gray')
plt.title('Original')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis

plt.subplot(2,2,2),plt.imshow(mag,cmap = 'gray')
plt.title('Sobel')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis

plt.subplot(2,2,3),plt.imshow(mag_bin,cmap = 'gray')
plt.title('Sobel Binary')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis

plt.subplot(2,2,4),plt.imshow(canny_edge,cmap = 'gray')
plt.title('Canny Edge')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis

plt.show()