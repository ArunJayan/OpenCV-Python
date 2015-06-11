import numpy as np
import cv2

img = cv2.imread("images/trex.png")
cv2.imshow("trex.png",img)
cv2.waitKey(0)

blurred = np.hstack([cv2.GaussianBlur(img,(3,3),0),
					 cv2.GaussianBlur(img,(5,5),0),
					 cv2.GaussianBlur(img,(7,7),0)])
cv2.imshow("GaussianBlur",blurred)
cv2.waitKey(0)
# the third argument of cv2.GaussianBlur() is standard deviation in the x axis direction
# by setting this zero it will automatically compute its value for our image
#in Gaussian Blur , image has less blurring effect than the average blurring metheod
