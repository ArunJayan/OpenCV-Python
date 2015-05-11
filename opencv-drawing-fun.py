import cv2
import numpy as np

img = np.zeros((600,600,3),dtype="uint8")
#in opencv there functions for drawing line , rectangle and circle
#  for drawing  a line we have to use cv2.line() function .
cv2.line(img,(100,100),(400,400),(0,0,2550))
cv2.imshow("drawing functions",img)
cv2.waitKey(0)
#so we can draw the lines using tha function
# first argument is a numpy array of image , second is initial coordinate of line , 
# 3rd argument is final coordinate and next parameter is color
# now we can set the thickness of the line like below
cv2.line(img,(200,200),(560,30),(0,255,0),4)
cv2.imshow("drawing functions2",img)
cv2.waitKey(0)
# now we can draw a rectangle using cv2.rectangle()
cv2.rectangle(img,(30,30),(400,400),(255,0,0),2)
cv2.imshow("drawing functions3",img)
cv2.waitKey(0)
"""
first argument of cv2.rectangle() : numpy array of image
second argument of cv2.rectangle() : first coordinate of rectangle (left top)
third argument of cv2.rectangle() : final coordinate of rectangle (right bottom)
fourth argument of cv2.rectangle() : colour
fifth : thickness 
"""
#another example
cv2.rectangle(img,(100,100),(400,550),(0,240),1)
cv2.imshow("drawing function4",img)
cv2.waitKey(0)
## now we can draw a circle using cv2.circle()
cv2.circle(img,(300,300),50,(0,250,200))
## fist parameter of fun is numpy array
## second is coordinates of center
## third is radius
## fourth is colour
cv2.imshow("drawing function5",img)
cv2.waitKey(0)
#another example
img2 = np.zeros((500,500),dtype="uint8")
for a in range(1,200,25):
	cv2.circle(img2,(250,250),a,(255,0,0))
for a in range(70):
	cv2.circle(img,(250,250),a,(255,0,0))	
cv2.imshow("pattern",img2)
cv2.waitKey(0)
cv2.imshow("modified",img)
cv2.waitKey(0)

