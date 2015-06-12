import numpy as np 
import cv2

img = cv2.imread("images/coins.png")
cv2.imshow("coins.png",img)
cv2.waitKey(0)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray",gray)
cv2.waitKey(0)

lap = cv2.Laplacian(gray,cv2.CV_64F)
#cv2.imshow("Laplacian",lap)
lap = np.uint8(np.absolute(lap))
#transition from black to white is positive
#but transition from black to white is negative
#8bit unsigned integer can't represent negative numbers
#so we are using floating point datatype otherwise we loss the edges etc.
cv2.imshow("Laplacian image",lap)
cv2.waitKey(0)

sobelX = cv2.Sobel(img,cv2.CV_64F,1,0)
sobelY = cv2.Sobel(img,cv2.CV_64F,0,1)

sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

sobel_combined = cv2.bitwise_or(sobelX,sobelY)
cv2.imshow("sobelX",sobelX)
cv2.imshow("sobelY",sobelY)
cv2.imshow("sobel_combined",sobel_combined)
cv2.waitKey(0)