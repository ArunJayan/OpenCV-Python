import cv2
import numpy as np
from im_functions  import resize

img = cv2.imread("images/beach.png")
cv2.imshow("beach",img)
cv2.waitKey(0)

resized_img = resize(img,height=500)
cv2.imshow("resized_img",resized_img)
cv2.waitKey(0)

img2 = 