import cv2
import numpy as np

def translate(img,tx,ty):
	M = np.float32([[1,0,tx],[0,1,ty]])
	shifted_img = cv2.warpAffine(img,M,(img.shape[1],img.shape[0]))
	return shifted_img
def rotate(img,point=None,angle,scale=1.0):
	width = img.shape[1]
	height = img.shape[0]

	if pont is None:
		point = (width/2,height/2)
	M = cv2.getRotationMatrix2D(point,angle,scale)
	rotated_img = cv2.warpAffine(img,M,(img.shape[1],img.shape[0]))
	return  rotated_img
	