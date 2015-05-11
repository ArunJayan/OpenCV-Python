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
