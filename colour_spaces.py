import cv2
import numpy as np

image = cv2.imread("images/trex.png")
cv2.imshow("trex.png",image)
cv2.waitKey(0)

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)	#gray
cv2.imshow("gray",gray)
cv2.waitKey(0)

hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)	#HSV
cv2.imshow("HSV",hsv)
cv2.waitKey(0)

lab = cv2.cvtColor(image,cv2.COLOR_BGR2LAB) #L*A*B
cv2.imshow("L*A*B",lab)
cv2.waitKey(0)

cv2.imshow("YCrCb",cv2.cvtColor(image,cv2.COLOR_BGR2YCR_CB))	#YCrCb colour formt
cv2.waitKey(0)

