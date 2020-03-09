import cv2, os
import numpy as np
from pathlib import Path

from functools import wraps


class ImageHandler(object):
	
	def validity_check(fn):
		pass

	def __init__(self, _path):
		self._img = cv2.imread(_path, cv2.IMREAD_COLOR)
		self._img_path = _path

	def get_img(self):
		return self._img

	def LoadImageFile(self, _path):
		pass

	def SaveImageFile(self):
		pass

	def SaveAsImageFile(self, _path):
		pass

	def ResizeImageFile(self, _fx, _fy):
		pass

	def RotateImageFile(self, angle, scale=1):
		h, w, plane = self._img.shape
		cX, cY = (w // 2, h // 2)

		M = cv2.getRotationMatrix2D((cX, cY), angle, scale)
		cos = np.abs(M[0, 0])
		sin = np.abs(M[0, 1])
	
		# compute the new bounding dimensions of the image
		nW = int((h * sin) + (w * cos))
		nH = int((h * cos) + (w * sin))
	
		# adjust the rotation matrix to take into account translation
		M[0, 2] += (nW / 2) - cX
		M[1, 2] += (nH / 2) - cY
		self._img = cv2.warpAffine(self._img, M, (nW, nH))

	def ShowImageFile(self):
		pass

if __name__ == "__main__":
	pass