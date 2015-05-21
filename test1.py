"""
this is sample program written to practise drwing function :-)
"""
import cv2
import numpy as np
canvas = np.zeros((500,500,3),dtype="uint8")
cv2.circle(canvas,(200,200),10,(255,0,0))
for i in range(1,200,10):
	cv2.circle(canvas,(250,250),i,(0,0,255))
cv2.rectangle(canvas,(10,50),(100,100),(255,0,0),-1)
cv2.line(canvas,(0,0),(500,500),(0,255,0),4)
cv2.imshow("test",canvas)
cv2.waitKey(0)
