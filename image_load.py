import cv2
img = cv2.imread("images/trex.png")
cv2.imshow("image",img)
cv2.waitKey(0)
print "Window Parameters\nWidth : %d"%(img.shape[1])
print "Height : %d"%(img.shape[0])
print "Channel : %d"%(img.shape[2])

#to get width of the image , <image_object>.shape[1]
#to get height of image , <image_object>.shape[0]
#to get channel number , <image_object>.shape[2]
