#live_streaming.py
import cv2
import numpy as np

video = cv2.VideoCapture("images/coin.mp4")
while True:
	ret, frame = video.read()
	if ret==True:
		gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
		blurred = cv2.GaussianBlur(gray, (13,13), 0)
		edged = cv2.Canny(blurred, 30, 150)
		(cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
		print "I count %d coins in this image" % (len(cnts))
		coins = frame.copy()
		cv2.drawContours(coins, cnts, -1, (0, 255, 0), 2)
		cv2.imshow('frame',coins)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	else:
		break
