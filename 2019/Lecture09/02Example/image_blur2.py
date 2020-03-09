import cv2
import numpy as np

def apply_blur(event,x,y,flags,param):
	if event == cv2.EVENT_LBUTTONDOWN:
		img = param[0]
		sliced = img[y-15:y+15, x-15:x+15, :]
		sliced = cv2.GaussianBlur(sliced, (5,5), 0)

		for sx, ix in enumerate(range(x-15, x+15)):
			for sy, iy in enumerate(range(y-15, y+15)):
				for plane in range(3):
					img.itemset((iy, ix, plane), sliced[sy, sx, plane]) #
		cv2.imshow('output', img)

cv2.namedWindow('frame')
cv2.namedWindow('output')
img = cv2.imread('pikachu1.png', cv2.IMREAD_COLOR)
rows, columns, plane = img.shape
print(columns, rows, plane)

cv2.setMouseCallback('frame', apply_blur, (img,))
cv2.imshow('frame', img)
cv2.waitKey(0)


