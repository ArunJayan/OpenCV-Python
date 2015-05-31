import cv2
import numpy as np

image = cv2.imread("images/wave.png")
cv2.imshow("Wave.png",image)
cv2.waitKey(0)
#in above steps we read a image called wave.png and showed it .

width = image.shape[1]	#current image's width
height = image.shape[0]	#current image's height 

print "width : %d\nheight : %d"%(width,height)

#while resizing an image we need to keep aspect ratio of the image
#Aspect ratio is the relationship of the width and height of the image.
r = 500/image.shape[1]
dim = (500,int(r*image.shape[0]))
"""
computing aspect ratio is performed on previous step.
we define the new image width to be 500 pixels
to compute ratio of new height to old height , we define r as follows
				r = new  width / old width
to compute new height we multiply the old height with aspect ratio r.
				new height = r*old height
"""
resized_img = cv2.resize(image,dim,interpolation = cv2.INTER_AREA)
cv2.imwrite("resized.png",resized_img)
cv2.imshow("resized",resized_img)
cv2.waitKey(0)