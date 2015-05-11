import cv2
import numpy as np
canvas = np.zeros((500,500,3),dtype = "uint8")
for i in range(0,30):
	r = np.random.randint(10,high=400)
	color = np.random.randint(0,high=256,size=(3,)).tolist()
	pt = np.random.randint(0,high = 300,size = (2,))
	cv2.circle(canvas,tuple(pt),r,color,-1)#thickness prameter -1 so it will fill the circle
cv2.imshow("canvas",canvas)
cv2.waitKey(0)
