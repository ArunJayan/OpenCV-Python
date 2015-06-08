import cv2
import numpy as np

img = cv2.imread("images/trex.png")
cv2.imshow("trex.png",img)
cv2.waitKey(0)

img2 = cv2.imread("images/wave.png")
cv2.imshow("wave.png",img2)
cv2.waitKey(0)

img_not = cv2.bitwise_not(img)
cv2.imshow("OR",img_not)
cv2.waitKey(0)

img_not2 = cv2.bitwise_not(img2)
cv2.imshow("NOT",img_not2)
cv2.waitKey(0)
