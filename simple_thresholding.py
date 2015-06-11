import numpy as np
import cv2

img = cv2.imread("images/coins.png")
cv2.imshow("coins",img)
cv2.waitKey(0)

blur = cv2.GaussianBlur(img,(3,3),0)
cv2.imshow("blur-img",blur)
cv2.waitKey(0)
