import sys
#from PySide2 import QtCore, QtWidgets
'''
print("my program")

app = QtWidgets.QApplication(sys.argv)

mywindow = QtWidgets.QWidget()
mywindow.resize(320, 240)
mywindow.setWindowTitle("World!")

mylabel = QtWidgets.QLabel(mywindow)
mylabel.setText("Hello, my name is cbchoi")
mylabel.setGeometry(QtCore.QRect(20, 20, 200, 20))
mywindow.show()

sys.exit(app.exec_())
'''

from PySide2.QtWidgets import *
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile

app = QApplication(sys.argv)

ui_file = QFile("first_ui.ui")
loader = QUiLoader()
window = loader.load(ui_file)
ui_file.close()

window.show()

sys.exit(app.exec_())