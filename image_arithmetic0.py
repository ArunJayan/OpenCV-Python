import cv2
import numpy as np

print "Max of 255 :"+str(cv2.add(np.uint8([200]),np.uint8([100])))
print "minimum 0:"+str(cv2.subtract(np.uint8([90]),np.uint8([800])))


image1 = cv2.imread("images/trex.png")
M = np.ones(image1.shape,dtype="uint8")*100
added = cv2.add(image1,M)
cv2.imshow("added images",added)
cv2.waitKey(0)

image2 = cv2.imread("images/wave.png")
M = np.ones(image2.shape,dtype="uint8")*130
subtracted = cv2.subtract(image2,M)
cv2.imshow("subtracted",subtracted)
cv2.waitKey(0)


