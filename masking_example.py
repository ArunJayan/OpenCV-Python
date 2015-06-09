#my own making experiments :-P
import cv2
import numpy as np
from im_functions  import resize

img = cv2.imread("images/wave.png")
cv2.imshow("wave",img)
cv2.waitKey(0)

img = resize(img,height=600)
print img.shape[:2]

img2 = np.zeros((600,864),dtype="uint8")
cv2.circle(img2,(100,100),100,255,-1)
cv2.rectangle(img2,(200,200),(400,400),255,-1)
cv2.circle(img2,(400,400),200,255,-1)
cv2.imshow("frame",img2)
cv2.waitKey(0)

masked = cv2.bitwise_and(img,img,mask=img2)
cv2.imshow("mask",masked)
cv2.waitKey(0)

