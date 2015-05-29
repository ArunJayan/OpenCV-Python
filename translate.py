import cv2
import numpy as np

img = cv2.imread("images/trex.png")
cv2.imshow("input",img)
cv2.waitKey(0)
#then we have to specify transilation matrix
"""
transition matrix :
[1,0,tx]
[0,1,ty]

#the first row of matrix is [1,0,tx] where tx is the number of pixels we shift the image left or right
#positive values of tx will shift to right
#negative values will shift to left
#the second row of matrix is [0,1,ty] where ty i the number of pixels we shift the image up or down
#positive values of ty will shift to down and negative to up
"""
M = np.float32([[1,0,20],[0,1,40]])
#using above transition matrix , we shift the image to 20 pixel right and 40 pixel to down
shifted = cv2.warpAffine(img,M,(img.shape[1],img.shape[0])) # we get shifted image
cv2.imshow("Shifted",shifted)
cv2.waitKey(0)
img2 = cv2.imread("images/wave.png")
cv2.imshow("img2",img2)
cv2.waitKey(0)
M = np.float32([[1,0,0],[0,1,-60]])
shifted = cv2.warpAffine(img2,M,(img2.shape[1],img2.shape[0]))
cv2.imshow("shifted to up",shifted)
cv2.waitKey(0)
