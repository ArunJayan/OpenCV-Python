import cv2
import numpy as np
drawing = False
ix,iy = -1,-1


def mouse_event(event,x,y,flags,param):
    global ix,iy,drawing,mode
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
    elif event == cv2.EVENT_LBUTTONUP:
        print img[iy,ix][0],img[iy,ix][1],img[iy,ix][2]
       # print ix,iy
        drawing = False
cap = cv2.VideoCapture(1)
cv2.namedWindow('image')
cv2.setMouseCallback('image',mouse_event)

while(cap.isOpened()):
	ret, img = cap.read()
	if ret== True:
			img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
			cv2.imshow('image',img)
			k = cv2.waitKey(1) & 0xFF
			if k == 27:
					break

cv2.destroyAllWindows()
