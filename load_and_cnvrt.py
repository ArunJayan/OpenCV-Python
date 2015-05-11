#it read png image and convert into jpg
import cv2
img = cv2.imread("images/trex.png")#read images as numpy array
cv2.imwrite("images/trex.jpg",img)
cv2.imshow("converted-img",cv2.imread("images/trex.jpg"))
cv2.waitKey(0)#wait for any key to press
