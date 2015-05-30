import numpy as np
import cv2
#function that can be used translation of images
def translate(img,tx,ty):
	M = np.float32([[1,0,tx],[0,1,ty]])
	shifted = cv2.warpAffine(img,M,(img.shape[1],img.shape[0]))
	return shifted
