import numpy as np
import cv2

img = cv2.imread("images/wave.png")
cv2.imshow("wave",img)
cv2.waitKey(0)

(Blue,Green,Red)=cv2.split(img)
cv2.imshow("Red",Red)   
cv2.imshow("Green",Green)
cv2.imshow("Blue",Blue)
cv2.waitKey(0)

cv2.imwrite("images/red_channel_wave.png",Red)
cv2.imwrite("images/green_channel_wave.png",Green)
cv2.imwrite("images/blue_channel_wave.png",Blue)


cv2.imshow("merged",cv2.merge([Blue,Green,Red]))
cv2.waitKey(0)

zero = np.zeros(img.shape[:2],dtype='uint8')

red = cv2.merge([zero,zero,Red])	#reconstruct the image
green = cv2.merge([zero,Green,zero])# " "         "   ""
blue = cv2.merge([Blue,zero,zero])	# ""          "   ""


cv2.imshow("reconstrcted-->Red",red)
cv2.imshow("reconstrcted-->Green",green)
cv2.imshow("reconstrcted-->Blue",blue)
cv2.waitKey(0)

cv2.destroyAllWindows()
