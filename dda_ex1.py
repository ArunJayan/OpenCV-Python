from ddalib import draw_line
import cv2
import numpy as np
image = np.zeros((600,600,3),dtype="uint8")
color = (255,0,255)
draw_line(image,50,50,500,500,color)
cv2.imshow("DDA Example",image)
cv2.waitKey(0)
