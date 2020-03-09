import cv2
import numpy as np

img = cv2.imread('pikachu2.jpg', cv2.IMREAD_COLOR)
print(img.shape)
rows,cols,plane = img.shape

cv2.imshow('src',img)

M = np.float32([[1,0,100],[0,1,50]])
dst = cv2.warpAffine(img,M,(cols,rows))

cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
