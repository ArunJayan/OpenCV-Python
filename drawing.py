import cv2
import numpy as np
canvas = np.zeros((500,500,3),dtype="uint8")
cv2.imshow("blank-canvas",canvas)
cv2.waitKey(0)

def deraw_line(x1,y1,x2,y2):
	
