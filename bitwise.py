import cv2
import numpy as np

rectangle = np.zeros((300,300),dtype="uint8")
cv2.rectangle(rectangle,(100,100),(250,250),255,-1)
cv2.imshow("rectangle",rectangle)
cv2.waitKey(0)
