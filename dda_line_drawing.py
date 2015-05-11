#in this program we are going to draw the lines using DDA Alogorithm
import cv2
import numpy as np

def draw_line(canvas,x0,y0,xn,yn,color):
	x = x0
	y = y0
	dx = xn-x0
	dy = yn-y0
	m = dy/dx
	if(m>0):
		if(dx>dy):
			steps = dx
			for a in range(1,steps):
				canvas[x,y]=color
				x = x + 1
				y = y + m
		else:
			steps = dy
			for a in range(1,steps):
				canvas[x,y]=color
				y = y+1
				x = x+1/m
	else:
		if(dx>dy): 
			steps = dx
			for a in range(1,steps):
				canvas[x,y] = color
				x = x-1
				y = y-m
		else:
			steps = dy
			for a in range(1,steps):
				canvas[x,y] = color
				y = y-1
				x = x-1/m

if __name__ == "__main__":
		  canvas = np.zeros((500,500,3),dtype="uint8")
		  color = (0,255,0)
		  draw_line(canvas,100,100,300,300,color)
		  cv2.imshow("dda",canvas)
		  cv2.waitKey(0)
