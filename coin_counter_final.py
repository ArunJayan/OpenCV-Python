import numpy as np
import cv2

img = cv2.imread("images/coins.png")
cv2.imshow("coins.png",img)
cv2.waitKey(0)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray",gray)
cv2.waitKey(0)

blurred_img = cv2.GaussianBlur(gray,(5,5),0)
cv2.imshow("GaussianBlur",blurred_img)
cv2.waitKey(0)

canny = cv2.Canny(gray,30,150)
cv2.imshow("canny",canny)
cv2.waitKey(0)
