import numpy as np
import cv2

img = cv2.imread("images/coin.jpg")
#cv2.imshow("coins.png",img)
#cv2.waitKey(0)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (9,9), 0)
#cv2.imshow("Image", img)

edged = cv2.Canny(blurred, 40, 150)
#cv2.imshow("Edges", edged)
#cv2.waitKey(0)

(cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print "I count %d coins in this image" % (len(cnts))

coins = img.copy()
cv2.drawContours(coins, cnts, -1, (0, 255, 0), 2)
#cv2.imshow("Coins", coins)
#cv2.waitKey(0)

stack = np.hstack([img,coins])
cv2.imshow("result",stack)
cv2.waitKey(0)

