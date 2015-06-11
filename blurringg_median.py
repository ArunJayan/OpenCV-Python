import cv2
import numpy as np


img = cv2.imread("images/trex.png")
#cv2.imshow("trex.png",img)
#cv2.waitKey(0)

blurred = np.hstack([img,cv2.medianBlur(img,3),
					 cv2.medianBlur(img,5),
					 cv2.medianBlur(img,7)])
cv2.imshow("medianBlur",blurred)
cv2.waitKey(0)
