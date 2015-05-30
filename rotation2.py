import cv2
import numpy as np
from im_functions import rotate

img = cv2.imread("images/wave.png")
cv2.imshow("wave.png",img)
cv2.waitKey(0)
rotated_img = rotate(img,30)
cv2.imshow("Rotated image",rotated_img)
cv2.waitKey(0)	