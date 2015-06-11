import numpy as np
import cv2

img = cv2.imread("images/coins.png")
cv2.imshow("coins",img)
cv2.waitKey(0)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray-scale",gray)

blur = cv2.GaussianBlur(gray,(7,7),0)
cv2.imshow("blur-img",blur)
cv2.waitKey(0)

(T,threshold_img) = cv2.threshold(blur,160,255,cv2.THRESH_BINARY)
cv2.imshow("threshold-binary",threshold_img)
cv2.waitKey(0)

(T,threshod_bin_inverse_img) = cv2.threshold(blur,160,255,cv2.THRESH_BINARY_INV)
cv2.imshow("threshold-bin-inv",threshod_bin_inverse_img)
cv2.waitKey(0)

out = cv2.bitwise_and(img,img,mask=threshod_bin_inverse_img)
cv2.imshow("out",out)
cv2.waitKey(0)
