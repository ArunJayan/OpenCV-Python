#average blurring metheod
import cv2
import numpy as np

image = cv2.imread("images/trex.png")
#cv2.imshow("trex.png",image)
#cv2.waitKey(0)
blurred = np.hstack([image,cv2.blur(image,(3,3)),
					cv2.blur(image,(5,5)),
					cv2.blur(image,(7,7))])
cv2.imshow("Average blur",blurred)
cv2.waitKey(0)
