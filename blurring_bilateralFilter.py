import cv2
import numpy as np

img = cv2.imread("images/trex.png")
blur = np.hstack([img,cv2.bilateralFilter(img,3,21,21),
					  cv2.bilateralFilter(img,5,41,41),
					  cv2.bilateralFilter(img,27,71,71)])
cv2.imshow("BilateralFilter -blur",blur)
cv2.waitKey(0)

img = cv2.imread("images/beach.png")
blur = np.hstack([img,cv2.bilateralFilter(img,3,11,11),
					  cv2.bilateralFilter(img,5,21,21),
					  cv2.bilateralFilter(img,7,51,51)])
cv2.imshow("Bilateral",blur)
cv2.waitKey(0)
