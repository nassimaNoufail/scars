import numpy as np
import cv2
import matplotlib.pyplot as plt
from scipy.misc import imread

im = imread('test4c.jpg')
img = im[:,:,2]     #only red channel
Z = img.reshape((-1,3))
# convert to np.float32 as required from kmeans input
Z = np.float32(Z)

# define criteria, number of clusters(K) and apply kmeans()
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K = 2   #number of clusters
ret,label,center=cv2.kmeans(Z,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)

#convert back into uint8, and make original image
center = np.uint8(center)
res = center[label.flatten()]
res2 = res.reshape((img.shape))

#take canny edges of kmeans
canny_edge = cv2.Canny(res2,200,100)

plt.subplot(4,1,1), plt.imshow(im,cmap='pink')
plt.subplot(4,1,2), plt.imshow(img,cmap='pink')
plt.subplot(4,1,3), plt.imshow(res2,cmap='pink')
plt.subplot(4,1,4), plt.imshow(canny_edge,cmap='pink')
plt.show()