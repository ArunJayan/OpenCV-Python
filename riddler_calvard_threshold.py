#riddler_calvard.py
import numpy as np 
import cv2
import mahotas

img = cv2.imread("images/coins.png")
cv2.imshow("coins.png",img)
cv2.waitKey(0)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray",gray)
cv2.waitKey(0)

blur_img = cv2.GaussianBlur(gray,(5,5),0)
cv2.imshow("blur-img",blur_img)
cv2.waitKey(0)

T = mahotas.thresholding.rc(blur_img)
print "Riddler-Calvard:%d"%(T)

thresh = gray
thresh[thresh<T]=0
thresh[thresh>T]=255
thresh = cv2.bitwise_not(thresh)
cv2.imshow("thresh",thresh)
cv2.waitKey(0)
