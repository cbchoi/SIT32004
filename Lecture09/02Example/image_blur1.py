import cv2
img = cv2.imread('pikachu1.png', cv2.IMREAD_COLOR)
cv2.imshow('before', img)

dst = cv2.GaussianBlur(img, (5,5), 0)
cv2.imshow('after', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()