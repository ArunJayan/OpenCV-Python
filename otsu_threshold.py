#Otus thresholding metheod
#in this metheod we can automtically create optimal value of T.
import cv2
import numpy as np
import mahotas

img =cv2.imread("images/coins.png")
cv2.imshow("coins.png",img)
cv2.waitKey(0)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray",gray)
cv2.waitKey(0)

blur_img = cv2.GaussianBlur(gray,(5,5),0)
cv2.imshow("blur-img",blur_img)
cv2.waitKey(0)

T = mahotas.thresholding.otsu(blur_img)
print "Otsu's theshold :%d"%(T)

thresh = gray
thresh[thresh>T] = 255
thresh[thresh<T] = 0
thresh = cv2.bitwise_not(thresh)

cv2.imshow("thresh",thresh)
cv2.waitKey(0)
