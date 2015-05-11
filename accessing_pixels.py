import cv2
img = cv2.imread("images/trex.jpg")
print img[0,0]	#print thr RGB value of pixel [0,0]
img[0,0] = (0,0,0)
img[0,1] = (0,0,0)
img[0,2] = (0,0,0)
cv2.imshow("modified-pixel",img)
cv2.waitKey(0)
width = img.shape[1]
height = img.shape[0]
for i in range(width):
	img[5,i] = (0,0,0)
cv2.imshow("black-line",img)
cv2.waitKey(0) 
i = 0 
while i != 228:
	img[i,i] = (255,0,0)
	i = i +1
cv2.imshow("sample",img)
cv2.waitKey(0)
