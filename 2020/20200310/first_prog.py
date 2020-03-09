import sys
from PySide2.QtWidgets import *
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile

# Create a Qt application
app = QApplication(sys.argv)

ui_file = QFile("first_ui.ui")
loader = QUiLoader()
window = loader.load(ui_file)
ui_file.close()

window.show()
# Enter Qt application main loop
sys.exit(app.exec_())