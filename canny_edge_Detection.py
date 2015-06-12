import cv2
import numpy as np

img = cv2.imread("images/coins.png")
cv2.imshow("coins.png",img)
cv2.waitKey(0)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray",gray)
cv2.waitKey(0)

blurred_img = cv2.GaussianBlur(img,(7,7),0)
cv2.imshow("GaussianBlur-output",blurred_img)
cv2.waitKey(0)

canny = cv2.Canny(gray,55,150)
cv2.imshow("Canny",canny)
cv2.waitKey(0)