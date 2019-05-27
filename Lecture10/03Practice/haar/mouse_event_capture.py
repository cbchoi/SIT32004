import numpy as np
import cv2
import os
import subprocess as sp

drawing = False # true if mouse is pressed
ix,iy = -1,-1

class ImageCapture(object):
    def __init__(self):
        self._cap = cv2.VideoCapture(0)
        self._pos_image_list = []
        self._image_idx = 0
        self._neg_size = 0

        # list of image file update
        _file = open("positive.txt", "r")
        for l in _file:
            _path = l.split()
            if os.path.isfile(_path[0]):
                self._pos_image_list.append(l)
        _file.close()

        self._image_idx = len(self._pos_image_list)

        _file = open("negative.txt", "w")
        for img in os.listdir('neg'):
            full_filename = os.path.join('neg', img)
            _file.write(full_filename + "\n")
            self._neg_size = self._neg_size + 1
        _file.close()



    # mouse callback function
    def SetROI(self, event,x,y,flags,param):
        global ix,iy,drawing,mode

        if event == cv2.EVENT_LBUTTONDOWN:
            drawing = True
            ix,iy = x,y

        elif event == cv2.EVENT_MOUSEMOVE:
            if drawing == True:
                cv2.rectangle(param,(ix,iy),(x,y),(0,255,0),1)
                #param[1].write(param[0])
                cv2.imshow('frame',param)

        elif event == cv2.EVENT_LBUTTONUP:
            drawing = False
            cv2.rectangle(param,(ix,iy),(x,y),(0,255,0),1)
            
            pos_info = 'pos/imag_{}.jpg'.format(self._image_idx)
            pos_img = param[min(y,iy):max(y,iy), min(x,ix):max(x,ix)]

            pos_img = cv2.cvtColor(pos_img, cv2.COLOR_BGR2GRAY)
            pos_img = cv2.resize(pos_img, (50, 50))

            cv2.imshow(pos_info, pos_img)
            cv2.imwrite(pos_info, pos_img)

            self._pos_image_list.append('{} 1 0 0 {} {}\n'.format(pos_info, max(x,ix) - min(x,ix), max(y,iy) - min(y,iy)))
            self._image_idx += 1

    def start_capture(self):
        cv2.namedWindow('frame')
        while(self._cap.isOpened()):
            ret, frame = self._cap.read()
            if ret==True:
                #frame = cv2.flip(frame,0)
                #cv2.circle(frame,(10,10),100,(255,0,0),-1)
                #cv2.imshow('frame',frame)
                cv2.setMouseCallback('frame', self.SetROI, frame)
                cv2.imshow('frame',frame)
                
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                break

        print('capture done')
        _file = open("positive.txt", "w")
        for item in self._pos_image_list:
            _file.write(item)
        _file.close()
        # Release everything if job is finished
        self._cap.release()
        cv2.destroyAllWindows()

    def training(self):
        # Initalize
        final_lst = open("f_info.lst", "w")
        final_lst.close()

        num_sample = 1

        for idx, item in enumerate(self._pos_image_list):
            num_sample = num_sample + 1
            item = item.split() 
            # Pre-Processing
            _dir_path = "info{}".format(idx)
            _info_path = "info{}/info.lst".format(idx)            

            if os.path.isdir(_dir_path):
                pass
                #onlyfiles = [f for f in os.listdir(_dir_path) if os.path.isfile(os.path.join(_dir_path, f))]
                #for item in onlyfiles:
                #    os.remove(os.path.join(_dir_path, item))
            else:
                os.makedirs("info{}".format(idx))            
            
                print("Processing "+_info_path)
                sp.call(["opencv_createsamples.exe", 
                         "-img", item[0],
                         "-bg", "negative.txt",
                         "-info", _info_path,
                         "-pngoutput", "info",
                         "-maxxangle", "0.5",
                         "-maxyangle", "0.5",
                         "-maxzangle", "0.5",
                         "-num", "1950"
                         ])
            # post_process
            final_lst = open("f_info.lst", "a")
            f_lst = open(_info_path)
            for item in f_lst:
                final_lst.write("info{0}/{1}".format(idx, item))
        
            final_lst.close()
            f_lst.close()

        sp.call(["opencv_createsamples.exe",
                 "-info", "f_info.lst",
                 "-num", "1950",
                 "-w", "20",
                 "-h", "20",
                 "-vec", "positives.vec"])

        sp.call(["opencv_traincascade.exe",
                 "-data", "data",
                 "-vec","positives.vec",
                 "-bg", "negative.txt",
                 "-numPos", str(900),
                 "-numNeg", str(self._neg_size),
                 "-numStages", "10",
                 "-w", "20",
                 "-h", "20"])
        #opencv_createsamples -img watch5050.jpg -bg bg.txt -info info/info.lst -pngoutput info -maxxangle 0.5 -maxyangle 0.5 -maxzangle 0.5 -num 1950


if __name__ == "__main__":
    ic = ImageCapture()
    ic.start_capture()
    ic.training()


