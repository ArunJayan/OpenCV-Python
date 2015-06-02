#in this figure we flipp the image
import cv2
import numpy as np

img = cv2.imread("images/wave.png")
cv2.imshow("wave.png",img)
cv2.waitKey(0)

flipped1 = cv2.flip(img,1)	#second argument is flipp magnitude , if place 1 ,image will horizontally
cv2.imshow("flipped horizontal",flipped1)
cv2.waitKey(0)

flipped2 = cv2.flip(img,0)#ZERO will filpp vertical
cv2.imshow("flipped vertical",flipped2)
cv2.waitKey(0)

flipped_horiz_verti = cv2.flip(img,-1)#-1 will flip vertical and horizontal
cv2.imshow("flipped vertical and horizontal",flipped_horiz_verti)
cv2.waitKey(0)

