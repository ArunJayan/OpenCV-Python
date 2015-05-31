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
