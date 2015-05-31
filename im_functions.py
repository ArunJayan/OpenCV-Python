import cv2
import numpy as np

def translate(img,tx,ty):
	M = np.float32([[1,0,tx],[0,1,ty]])
	shifted_img = cv2.warpAffine(img,M,(img.shape[1],img.shape[0]))
	return shifted_img
def rotate(img,angle,point=None,scale=1.0):
	width = img.shape[1]
	height = img.shape[0]

	if point is None:
		point = (width/2,height/2)
	M = cv2.getRotationMatrix2D(point,angle,scale)
	rotated_img = cv2.warpAffine(img,M,(width,height))
	return  rotated_img
def resize(img,width=None,height=None,inter = cv2.INTER_AREA):
	dim = None
	(h,w) = (img.shape[0],img.shape[1])
	if width is None and height is None:
		return img
	if width is None:
		r = height/float(h)
		dim = (int(r*w),height)
	else:
		r = width/float(w)
		dim = (width,int(h*r))
	resized = cv2.resize(img,dim,interpolation=inter)
	return resized