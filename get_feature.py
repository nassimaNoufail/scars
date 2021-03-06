import numpy as np
import cv2
import matplotlib.pyplot as plt
from scipy.misc import imread
from scipy import ndimage as ndi
import os
def length(im):
	# Script_Run = np.load('ScriptRun.npy')
	# Script_Run = Script_Run+1
	# np.save('ScriptRun.npy',Script_Run)
	K = 3
	imK, canny_edge, imR, canny_edgeK = pre_process(im, K, type = 0)
	theta_deg = auto_rotate(canny_edgeK)
	horiz_im = ndi.rotate(imK, -int(round(theta_deg)), mode='nearest',cval=255)
	horiz_im = pre_process(horiz_im, K, type = 1)
	imL = np.copy(horiz_im)
	row_val, row_ind, scar_start, scar_length = get_row(imL)
	# horiz_orig_im = ndi.rotate(im, -int(round(theta_deg)), mode='constant',cval=255)
	# plt.imshow(horiz_orig_im)
	# plt.imshow(horiz_orig_im,cmap='pink')
	# plt.plot([scar_start, scar_start+scar_length], [row_ind, row_ind],linewidth=3)
	# plt.show()
	# plt.savefig(scar_num +' length' + str(Script_Run) + '.png')
	# plt.close()

	return scar_length

def red(im):
	# Script_Run = np.load('ScriptRun.npy')
	# Script_Run = Script_Run+1
	# np.save('ScriptRun.npy',Script_Run)
	K = 3
	imK, canny_edge, imR, canny_edgeK = pre_process(im, K, type = 0)
	mask, avg_intesity = get_mask(imK, imR)

	# plt.imshow(imK,cmap = 'gray')
	# plt.show()
	# plt.savefig(scar_num +' red' + str(Script_Run) + '.png')
	# plt.close()

	return avg_intesity

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
	return mask, avg_intesity

def auto_rotate(canny_edge):
	#convert image to co ordinated
	white_coord = get_scar_coord(canny_edge)
	#extract co ordinates
	x = white_coord[:,0]
	y = white_coord[:,1]
	alphaI = 2 * np.eye(2)       #covarance of prior
	betaI = np.eye(2)              #variance of noise in data
	m, S = get_posterior(x, y, alphaI, betaI)  #update posterior
	theta_rad = np.arctan(m[1])     #find angle from gradient
	theta_deg = (theta_rad*(180/np.pi))    #convert to degrees
	rotated_im = ndi.rotate(canny_edge, -int(round(theta_deg)), mode='constant',cval=255)
	return theta_deg

def get_scar_coord(canny_edge):
	#convert to a binary image
	s = np.shape(canny_edge)
	canny_bin = canny_edge.copy()
	plt.imshow(canny_edge)
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
		if np.size(im.shape) == 3:
			imR = im[:,:,2]     #only red channel
		else:
			imR = im
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
		imC = np.copy(imK)
		low = np.min(imC)
		imC[imC!=low] = 255

		canny_edgeK = cv2.Canny(imC,200,100)
		return imK, canny_edge, imR, canny_edgeK
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