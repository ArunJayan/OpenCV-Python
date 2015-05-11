import cv2
img = cv2.imread("images/trex.png")
img1 = img[20:120,250:340]
img[20:120,150:240] = (0,0,255)
cv2.imshow("img",img)
cv2.imshow("img1",img1)
cv2.waitKey(0)
