import cv2
import numpy as np
import matplotlib.pyplot as plt

class StraightenImage(object):
	def __init__(self, _path):
		self.drawing = False
		self.ix = 0
		self.iy = 0
		self.img = cv2.imread(_path)
		self.pos_list = []
		cv2.setMouseCallback('original', self.mouse_catch, None)

	def get_img(self):
		return self.img

	def mouse_catch(self, event, x, y, flags, param):
		pass

	def straighten(self, width, height):
		pass


cv2.namedWindow('original')
si = StraightenImage("sudoku-original.jpg")
cv2.imshow('original', si.get_img())
cv2.waitKey(0)

#cv2.namedWindow('straighten')
cv2.imshow('straighten', si.straighten(300, 300))

cv2.waitKey(0)
cv2.destroyAllWindows()