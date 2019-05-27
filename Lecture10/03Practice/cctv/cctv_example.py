import cv2
import numpy as np
import subprocess as sp
from multiprocessing import Process, Lock, Queue

if __name__ == '__main__':
    cv2.namedWindow("GoPro")
    car_cascade = cv2.CascadeClassifier('cars.xml')

    FFMPEG_BIN = "ffmpeg/bin/ffmpeg.exe"
    VIDEO_URL = "http://220.122.218.208:1935/live/video66.stream/playlist.m3u8"
    pipe = sp.Popen([ FFMPEG_BIN, "-i", VIDEO_URL,
           "-loglevel", "quiet", # no text output
           "-an",   # disable audio
           "-f", "image2pipe",
           "-pix_fmt", "bgr24",
           "-vcodec", "rawvideo", "-"],
           stdin = sp.PIPE, stdout = sp.PIPE)
    while True:
        data = (pipe.stdout.read(720*480*3)) # read 432*240*3 bytes (= 1 frame)
        if len(data) >= 720*480*3:
            image =  np.frombuffer(data, dtype='uint8').reshape((480,720,3))
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
            gray = cv2.blur(gray, (3,3))
            cars = car_cascade.detectMultiScale(gray, 3, 5)

            for (x,y,w,h) in cars: 
                cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),2) 
            
            cv2.imshow("GoPro",image)
        else:
            pipe = sp.Popen([ FFMPEG_BIN, "-i", VIDEO_URL,
               "-loglevel", "quiet", # no text output
               "-an",   # disable audio
               "-f", "image2pipe",
               "-pix_fmt", "bgr24",
               "-vcodec", "rawvideo", "-"],
               stdin = sp.PIPE, stdout = sp.PIPE)
            pass

        if cv2.waitKey(10) == 27:
            break
