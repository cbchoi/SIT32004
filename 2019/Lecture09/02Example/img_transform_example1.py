import cv2
import numpy as np

img = cv2.imread('pikachu1.png')

res = cv2.resize(img,None,fx=2, fy=2, interpolation = cv2.INTER_CUBIC)
cv2.imshow('zoom', res)

res = cv2.resize(img,None,fx=0.5, fy=0.5, interpolation = cv2.INTER_AREA)
cv2.imshow('shrink', res)

cv2.waitKey(0)