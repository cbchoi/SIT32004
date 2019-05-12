import numpy as np
import cv2

def draw_circle(event,x,y,flags,param):
	if event == cv2.EVENT_LBUTTONDOWN:
		cv2.circle(img,(x,y), 100,(0,255,255),-1)
		cv2.imshow('img', img)
		print(x, y)

# Create a black image
img = np.zeros((768,1024,3), np.uint8)

# Create a named window
cv2.namedWindow('img')
cv2.setMouseCallback('img', draw_circle, None)

cv2.imshow('img',img)
cv2.waitKey(0)