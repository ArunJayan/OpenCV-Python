import cv2
img = cv2.imread("images/trex.png")
img = img[0:200,0:150]
cv2.imshow("img",img)
cv2.waitKey(0)
