import sys
from PySide2.QtWidgets import *
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile, QObject

class AnimationViewer(QLabel):
	def __init__(self, _parent=None):
		super(AnimationViewer, self).__init__(_parent)
		pass

class PlaylistManager(QObject):
	def __init__(self, _parent=None):
		super(PlaylistManager, self).__init__(_parent)
		self.obj = _parent
		pass

	def add_animation(self):
		# retrieve txtEdit content
		# add the contents to the playList
		# exceptional case: check null string
		if self.txtEdit.toPlainText() != "":
			self.playList.addItem(self.txtEdit.toPlainText())
			self.txtEdit.setPlainText("")

	def remove_animation(self):
		print("[SMP] remove")
		print("cur_row:{0}".format(self.playList.currentRow()))

	def up_animation(self):
		print("[SMP] up")

	def down_animation(self):
		print("[SMP] down")

	def __getattr__(self, attr):
		return getattr(self.obj, attr)

class MediaControl(QObject):
	# signal part

	def __init__(self, _parent = None):
		super(MediaControl, self).__init__(_parent)
		self.obj = _parent

	def play_animation(self):
		print("play")
		pass

	def pause_animation(self):
		print("pause")
		pass

	def resume_animation(self):
		print("resume")
		pass

	def stop_animation(self):
		print("stop")
		pass	

	def __getattr__(self, attr):
		return getattr(self.obj, attr)

class StopMotionPlayer(QWidget):
	def __init__(self, _parent = None):
		super(StopMotionPlayer, self).__init__(_parent)
		self.obj = _parent

		self.media_control = MediaControl(self.obj)
		self.playlist_manager = PlaylistManager(self.obj)
		#self.animation_viewer = AnimationViewer(self.obj)

		self.addBtn.clicked.connect(self.playlist_manager.add_animation)
		self.removeBtn.clicked.connect(self.playlist_manager.remove_animation)
		self.upBtn.clicked.connect(self.playlist_manager.up_animation)
		self.downBtn.clicked.connect(self.playlist_manager.down_animation)

		self.playBtn.clicked.connect(self.media_control.play_animation)
		self.pauseBtn.clicked.connect(self.media_control.pause_animation)
		self.resumeBtn.clicked.connect(self.media_control.resume_animation)
		self.stopBtn.clicked.connect(self.media_control.stop_animation)

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

smp = StopMotionPlayer(window)
smp.show()
# Enter Qt application main loop
sys.exit(app.exec_())