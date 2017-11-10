import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy.misc import imread



image = cv2.imread("test.jpg")

r = image.copy()
# set blue and green channels to 0
r[:, :, 0] = 0
r[:, :, 1] = 0

cv2.imshow('R-RGB', r)
cv2.waitKey(0)
# plt.axis("off")
# plt.imshow(image)
# plt.show()

# cv2.imshow('R-RGB',image[:, :, 2])

# im = imread("Test2.png")
# fig = plt.figure()
# ax = fig.add_subplot(131)
# ax.imshow(im,cmap="gray")