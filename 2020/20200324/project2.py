import sys
import os
import time

from PySide2.QtWidgets import *
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile, QObject, QTimer, Slot, Signal
from PySide2.QtGui import *

class AnimationViewer(QLabel):
	def __init__(self, _parent=None):
		super(AnimationViewer, self).__init__(_parent)
		self.image = QImage()
		pass

	def paintEvent(self, event):
		painter = QPainter(self)
		painter.drawImage(0, 0, self.image)

	def initUI(self):
		self.setWindowTitle('Test')

	@Slot(QImage)
	def setImage(self, image):
		if image.isNull():
			print("Viewer Dropped frame!")

		self.image = image
		if image.size() != self.size():
			self.setFixedSize(image.size())
		self.repaint()  

class PlaylistManager(QObject):
	def __init__(self, _parent=None):
		super(PlaylistManager, self).__init__(_parent)
		self.obj = _parent
		print(f"In PlaylistManager {self.obj}")
		pass

	def add_animation(self):
		# retrieve txtEdit content
		# add the contents to the playList
		# exceptional case: check null string
		if self.txtEdit.toPlainText() != "":
			self.playList.addItem(self.txtEdit.toPlainText())
			self.txtEdit.setPlainText("")

	def remove_animation(self):
		#print("[SMP] remove")
		#print("cur_row:{0}".format(self.playList.currentRow()))
		if self.playList.currentRow() >= 0:
			self.obj.playList.takeItem(self.playList.currentRow())

	def up_animation(self):
		# if currentRow <= 0 skip
		# currentRow > 0 then process
		if self.playList.currentRow() > 0:
			sel_item = self.playList.item(self.playList.currentRow())
			prev_item = self.playList.item(self.playList.currentRow()-1)

			txt = sel_item.text()
			sel_item.setText(prev_item.text())
			prev_item.setText(txt)

		print("[SMP] up")

	def down_animation(self):
		# self.playList.count()
		print("[SMP] down")

	def __getattr__(self, attr):
		return getattr(self.obj, attr)

class MediaControl(QObject):
	# signal part
	VIDEO_SIG = Signal(QImage)

	def __init__(self, _parent = None):
		super(MediaControl, self).__init__(_parent)
		self.obj = _parent

		print(f"In MediaControl {self.obj}")
		#print(self.obj.__dict__.keys())

		self.timer = QTimer()
		self.timer.timeout.connect(self.send_image)

		self.current_animation = []
		self.cur_row_idx = 0
		self.cur_image_idx = 0

	def get_animation(self, _path):
		path = _path
		file_list = os.listdir(path)

		images_lst = []
		for file in file_list:
			image = QImage()
			image.load(path + file)
			images_lst.append(image)

		return images_lst

	@Slot()
	def send_image(self):
		#print("send")

		if self.cur_image_idx >= len(self.current_animation):
			self.cur_row_idx += 1

			if self.cur_row_idx >= self.obj.playList.count():
				self.cur_row_idx = 0

			self.cur_image_idx = 0
			self.current_animation = self.get_animation(self.obj.playList.item(self.cur_row_idx).text())

		self.VIDEO_SIG.emit(self.current_animation[self.cur_image_idx])
		self.cur_image_idx += 1

		pass

	def play_animation(self):
		print("play")

		# When play button is clicked 
		# get animation -> from where?, send to? send what?
		print(self.obj.playList.item(self.cur_row_idx).text())
		self.current_animation = self.get_animation(self.obj.playList.item(self.cur_row_idx).text())

		self.timer.start(100)
		pass

	def pause_animation(self):
		print("pause")

		self.timer.stop()
		pass

	def resume_animation(self):
		print("resume")

		self.timer.start(100)
		pass

	def stop_animation(self):
		print("stop")

		self.cur_row_idx = 0
		self.cur_image_idx = 0

		self.timer.stop()
		pass	

	def __getattr__(self, attr):
		return getattr(self.obj, attr)

class StopMotionPlayer(QWidget):
	def __init__(self, _parent = None):
		super(StopMotionPlayer, self).__init__(_parent)
		self.obj = _parent

		self.media_control = MediaControl(self.obj)
		self.playlist_manager = PlaylistManager(self.obj)

		self.obj.label = AnimationViewer(self.obj.label)
		#self.animation_viewer = AnimationViewer(self.obj)

		self.addBtn.clicked.connect(self.playlist_manager.add_animation)
		self.removeBtn.clicked.connect(self.playlist_manager.remove_animation)
		self.upBtn.clicked.connect(self.playlist_manager.up_animation)
		self.downBtn.clicked.connect(self.playlist_manager.down_animation)

		self.playBtn.clicked.connect(self.media_control.play_animation)
		self.pauseBtn.clicked.connect(self.media_control.pause_animation)
		self.resumeBtn.clicked.connect(self.media_control.resume_animation)
		self.stopBtn.clicked.connect(self.media_control.stop_animation)

		self.media_control.VIDEO_SIG.connect(self.obj.label.setImage)

	def __getattr__(self, attr):
		return getattr(self.obj, attr)

	def show(self):
		self.obj.show()

# Create a Qt application
app = QApplication(sys.argv)

ui_file = QFile("project2.ui")
loader = QUiLoader()
window = loader.load(ui_file)
ui_file.close()

print("components of main window")
print(window.__dict__.keys())

smp = StopMotionPlayer(window)
smp.show()
# Enter Qt application main loop
sys.exit(app.exec_())