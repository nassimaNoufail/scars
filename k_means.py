import numpy as np
import cv2
import matplotlib.pyplot as plt
from scipy.misc import imread
from scipy import ndimage as ndi

def main():
	#take from command line
	import sys
	if len(sys.argv) == 1:
		im = imread('test4c.jpg')
	else:
		im = imread(*sys.argv[1:])

	#rotate image - in degrees
	# im = ndi.rotate(im, 45, mode='constant')
	K = 3
	imK, canny_edge, imR = pre_process(im, K, type = 0)
	mask, avg_intesity = get_mask(imK, imR)
	# masked = mask * imR
	plt.subplot(4,1,1), plt.imshow(im,cmap='pink')
	plt.subplot(4,1,2), plt.imshow(imR,cmap='pink')
	plt.subplot(4,1,3), plt.imshow(imK,cmap='pink')
	plt.subplot(4,1,4), plt.imshow(mask,cmap='pink')
	plt.show()

	# canny_edge = ndi.rotate(canny_edge, 20, mode='constant')
	fig = plt.figure()
	ax1 = fig.add_subplot(3,1,1)
	ax2 = fig.add_subplot(3,1,2)
	ax3 = fig.add_subplot(3,1,3)
	theta_deg = auto_rotate(ax1, ax2, ax3, canny_edge)

	horiz_im = ndi.rotate(imK, -int(round(theta_deg)), mode='nearest',cval=255)
	horiz_im = pre_process(horiz_im, K, type = 1)
	horiz_orig_im = ndi.rotate(im, -int(round(theta_deg)), mode='constant',cval=255)

	plt.subplot(2,1,1), plt.imshow(imK,cmap='pink')
	plt.subplot(2,1,2), plt.imshow(horiz_im,cmap='pink')
	plt.show()

	imL = np.copy(horiz_im)

	row_val, row_ind, scar_start, scar_length = get_row(imL)
	print('pixel length is ', row_val)

	plt.subplot(3,1,1), plt.imshow(horiz_im,cmap='pink')
	row_correct = imK.shape[0] - row_ind
	plt.plot([scar_start, scar_start+scar_length], [row_ind, row_ind],linewidth=5)
	plt.subplot(3,1,2), plt.imshow(horiz_orig_im,cmap='pink')
	plt.subplot(3,1,3), plt.imshow(horiz_orig_im,cmap='pink')
	plt.plot([scar_start, scar_start+scar_length], [row_ind, row_ind],linewidth=5)
	plt.show()

def get_row(imBlack):
	min_intensity = np.min(imBlack)
	imBlack[imBlack!=min_intensity] = 0
	imBlack[imBlack==min_intensity] = 1
	rows = np.sum(imBlack, axis=1)
	row_ind = np.argmax(rows)
	row_val = np.max(rows)
	count = -1
	neighbouring = 0
	white = 1
	max_neighbouring = int(row_val/5)
	while neighbouring < max_neighbouring:
		count +=1
		if imBlack[row_ind, count] == 1:
			white = 0
			while white == 0:
				if imBlack[row_ind, count] == 1:
					count += 1
					neighbouring += 1
					if neighbouring >= max_neighbouring:
						break
				else:
					neighbouring = 0
					white = 1
	scar_start = count - max_neighbouring
	white = 0
	count = int(np.copy(scar_start))
	scar_length = 0
	while white == 0 and count < imBlack.shape[1]:
		if imBlack[row_ind, count] == 1:
			count += 1
			scar_length += 1
		else:
			white = 1
	return row_val, row_ind, scar_start, scar_length

def get_mask(imK, im_original):
	min_val = np.amin(imK)
	s = np.shape(imK)
	mask = np.zeros(s)
	mask_count = 0
	for i in range(s[0]):
		for j in range(s[1]):
			if imK[i,j] == min_val:
				mask[i,j] = im_original[i,j]
				mask_count += 1
	mask_intesites = np.zeros(mask_count)
	mask_count = 0
	for i in range(s[0]):
		for j in range(s[1]):
			if imK[i,j] == min_val:
				mask_intesites[mask_count] = im_original[i,j]
				mask_count += 1
	avg_intesity = int(np.round(np.mean(mask_intesites)))
	print('average intentity is ', avg_intesity)
	return mask, avg_intesity

def auto_rotate(input_ax, line_ax, output_ax, canny_edge):
	#convert image to co ordinated
	white_coord = get_scar_coord(canny_edge)
	#extract co ordinates
	x = white_coord[:,0]
	y = white_coord[:,1]
	input_ax.imshow(canny_edge,cmap='pink')
	line_ax.plot(x, y, '.')

	alphaI = 2 * np.eye(2)       #covarance of prior
	betaI = np.eye(2)              #variance of noise in data
	m, S = get_posterior(x, y, alphaI, betaI)  #update posterior

	theta_rad = np.arctan(m[1])     #find angle from gradient
	theta_deg = (theta_rad*(180/np.pi))    #convert to degrees
	print('rotated ', theta_deg, ' degrees')

	#plot linear regression line
	xplot = [0, 650]
	y1 = [0,0]
	for n in range(2):
		y1[n] = m[1]*xplot[n] + m[0]

	line_ax.plot(xplot, y1, 'r')
	rotated_im = ndi.rotate(canny_edge, -int(round(theta_deg)), mode='constant',cval=255)
	output_ax.imshow(rotated_im,cmap='pink')
	plt.show()

	return theta_deg

def get_scar_coord(canny_edge):
	#convert to a binary image
	s = np.shape(canny_edge)
	canny_bin = canny_edge.copy()
	canny_mag = np.amax(canny_bin)
	canny_bin = (canny_bin/canny_mag)*255    #scale image to 255
	white_pix = 0     #initilise count for number of white pixels
	for i in range(s[0]):
		for j in range(s[1]):
			if canny_bin[i,j] > 100:   #threshold to push pixels to white
				canny_bin[i,j] = 255
				white_pix += 1
			else:
				canny_bin[i,j] = 0

	white_coord = np.zeros([white_pix,2])   #initilse ammount of white pixels
	ind = 0
	white_len = len(white_coord)
	for i in range(s[0]):
		for j in range(s[1]):
			if canny_bin[i,j] == 255:
				white_coord[ind, :] = [j, np.abs(i - s[0])]
				ind += 1
	return white_coord

def pre_process(im, K, type):
	if type == 0:
		imR = im[:,:,2]     #only red channel
		imR = cv2.medianBlur(imR,5)
		# Z = imR.reshape((-1,3))
		Z = np.reshape(imR, (-1, 1))
		# convert to np.float32 as required from kmeans input
		Z = np.float32(Z)

		# define criteria, number of clusters(K) and apply kmeans()
		criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
		# K = 2   #number of clusters
		ret,label,center=cv2.kmeans(Z,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)

		#convert back into uint8, and make original image
		center = np.uint8(center)
		res = center[label.flatten()]
		imK = res.reshape((imR.shape))

		#take canny edges of kmeans
		canny_edge = cv2.Canny(imK,200,100)
		return imK, canny_edge, imR
	if type == 1:
		Z = np.reshape(im, (-1, 1))
		# convert to np.float32 as required from kmeans input
		Z = np.float32(Z)

		# define criteria, number of clusters(K) and apply kmeans()
		criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
		# K = 2   #number of clusters
		ret,label,center=cv2.kmeans(Z,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)

		#convert back into uint8, and make original image
		center = np.uint8(center)
		res = center[label.flatten()]
		imK = res.reshape((im.shape))
		return imK

########################################
#functions for Baysian linear regression
from scipy.stats import norm

def get_prior(alphaI):
	m = [0, 0] 
	K = np.linalg.inv(alphaI)
	return m, K

def get_posterior(x, y, alphaI, betaI):
	x1 = np.ones(x.shape)       
	X = np.stack((x1, x))      
	alpha = np.linalg.inv(alphaI)
	beta = np.linalg.inv(betaI)
	beta = np.eye(2)
	beta = beta * 5
	I = np.eye(2)
	XTX = np.dot(X, np.transpose(X))
	XT = np.transpose(X)
	first = np.dot(beta, XTX)
	s = np.add(first, alpha)
	sInv = np.linalg.inv(s)
	first = np.dot(beta, sInv)
	second = np.dot(X, y)
	m = np.dot(first, second)
	
	return m, sInv

if __name__ == "__main__":
    main()




