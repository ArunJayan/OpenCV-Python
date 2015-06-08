import cv2
import numpy as np

rectangle = np.zeros((300,300),dtype="uint8")
cv2.rectangle(rectangle,(100,100),(250,250),255,-1)
cv2.imshow("rectangle",rectangle)
cv2.waitKey(0)

circle = np.zeros((300,300),dtype="uint8")
cv2.circle(circle,(150,150),90,255,-1)
cv2.imshow("circle",circle)
cv2.waitKey(0)

rect_and_circle = cv2.bitwise_and(rectangle,circle)
cv2.imshow("AND operation",rect_and_circle)
cv2.waitKey(0)

rect_or_circle = cv2.bitwise_or(rectangle,circle)
cv2.imshow("OR operation",rect_or_circle)
cv2.waitKey(0)

rect_xor_circle = cv2.bitwise_xor(rectangle,circle)
cv2.imshow("XOR Operation",rect_xor_circle)
cv2.waitKey(0)

circle_not = cv2.bitwise_not(circle)
cv2.imshow("NOT operation",circle_not)
cv2.waitKey(0)

xor_not = cv2.bitwise_not(rect_xor_circle)
cv2.imshow("NOT Operation2",xor_not)
cv2.waitKey(0)
	
