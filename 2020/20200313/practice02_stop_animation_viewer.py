import sys
import os
import time

from PySide2.QtWidgets import *
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile
from PySide2.QtGui import *

def get_animation(_path):
    path = _path
    file_list = os.listdir(path)

    images_lst = []
    for file in file_list:
        image = QImage()
        image.load(path + file)
        images_lst.append(image)

    return images_lst

class ImageViewer(QWidget):
    def __init__(self, parent=None):
        super(ImageViewer, self).__init__(parent)
        self.image = QImage()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawImage(0, 0, self.image)

    def initUI(self):
        self.setWindowTitle('Test')

    def setImage(self, image):
        if image.isNull():
            print("Viewer Dropped frame!")

        self.image = image
        if image.size() != self.size():
            self.setFixedSize(image.size())
        self.repaint()  

app = QApplication(sys.argv)

mywidget = ImageViewer()

main_window = QMainWindow()
main_window.setCentralWidget(mywidget)

main_window.show()

# Task 1 : play stop motion animation infinitely.

# Task 2 : play several animation using get_animation function
# ani_lst = []
animation_lst = get_animation('./animation2/')
main_window.setFixedSize(animation_lst[0].size())
for frame in animation_lst:
	mywidget.setImage(frame)
	time.sleep(0.06)

sys.exit(app.exec_())