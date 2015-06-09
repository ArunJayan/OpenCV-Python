import numpy as np
import cv2

red = cv2.imread("images/red_channel_wave.png")
green = cv2.imread("images/green_channel_wave.png")
blue = cv2.imread("images/blue_channel_wave.png")

r = cv2.split(red)[2]
g = cv2.split(green)[1]
b = cv2.split(blue)[0]

wave = cv2.merge([b,g,r])
cv2.imshow("merged_wave",wave)
cv2.waitKey(0)
