#in this program we are going to rotate a image
import cv2
import numpy as np

img = cv2.imread("images/wave.png")
cv2.imshow("waves.png",img)
cv2.waitKey(0)

"""
#for rotation we have to specify a matrix (rotation matrix) using cv2.getRotationMatrix2D()
# cv2.getRotationMatrix2D has three arguments
### first argument is :: the point at which we want to rotate the image
### second argument is :: the angle of rotation
### third argument is :: degree of magnification (if we put 1.0 there is no magnification , but if we put 2.0 it will double the size)
after creating this matrix we have to give this matrix to cv2.warpAffine() (just like we did in translation)
"""
width = img.shape[1]
height =  img.shape[0]
M = cv2.getRotationMatrix2D((width/2,height/2),60,1.0)
rotated_img = cv2.warpAffine(img,M,(img.shape[1],img.shape[0]))
cv2.imshow("rotated_img",rotated_img)
cv2.waitKey(0)

img2 = cv2.imread("images/trex.png")
cv2.imshow("trex.png",img2)

M = cv2.getRotationMatrix2D((0,0),-20,1.0)
rotated_img2 = cv2.warpAffine(img2,M,(img2.shape[1],img2.shape[0])) 	
cv2.imshow("rotated_img2",rotated_img2)
cv2.waitKey(0)