import numpy as np
import cv2
import os
import subprocess as sp

drawing = False # true if mouse is pressed
ix,iy = -1,-1

class ImageBlur(object):
    def __init__(self, _path):
        self._path = _path
        self.drawing = False
        self.ix = 0
        self.iy = 0
        self.img = None

    # mouse callback function
    def MouseBlur(self, event,x,y,flags,param):

        if event == cv2.EVENT_LBUTTONDOWN:
            self.drawing = True
            self.ix, self.iy = x, y

        elif event == cv2.EVENT_MOUSEMOVE:
            if self.drawing == True:
                pass

        elif event == cv2.EVENT_LBUTTONUP:
            self.drawing = False
            self.img = cv2.GaussianBlur(self.img, (3, 3), 0)
            cv2.imshow('frame', self.img)


    def start(self):
        cv2.namedWindow('frame')
        self.img = cv2.imread(self._path)
        cv2.setMouseCallback('frame', self.MouseBlur, None)
        cv2.imshow('frame', self.img)

        cv2.waitKey(0)
        cv2.destroyAllWindows()



if __name__ == "__main__":
    ic = ImageBlur("test_img.jpg")
    ic.start()

