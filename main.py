import sys
import os

from PySide6.QtWidgets import QApplication, QWidget, QLabel, QSystemTrayIcon, QMenu
from PySide6.QtGui import QIcon, QMovie, Qt, QAction

def resource_path(relative_path):
    # Get absolute path to resource, works for dev and for PyInstaller """
		try:
			# PyInstaller creates a temp folder and stores path in _MEIPASS
			base_path = sys._MEIPASS
		except Exception:
			base_path = os.path.abspath(".")

		return os.path.join(base_path, relative_path)


app = QApplication([])
app.setQuitOnLastWindowClosed(True)
icon = QIcon(resource_path("icon.png"))
tray = QSystemTrayIcon()
movie2 = QMovie(resource_path("MZTeto.gif"))
movie1 = QMovie(resource_path("MZMiku.gif"))

class Window(QWidget):
	

	def __init__(self):
		super().__init__()
		self.setWindowFlags(Qt.FramelessWindowHint)
		self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
		self.setGeometry(100,100,700,500)
		self.setContentsMargins(0,0,0,0)
		global label 
		label = QLabel(self)
		label.setMovie(movie1)
		movie1.start()

	def change_teto(self):
		label.setMovie(movie2)
		movie2.start()
	def change_miku(self):
		label.setMovie(movie1)
		movie1.start()
	def mousePressEvent(self, event):
		self.dragPos = event.globalPosition().toPoint()
	def mouseMoveEvent(self, event):
		self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos)
		self.dragPos = event.globalPosition().toPoint() 
		event.accept()
	def app_quit(self):
		sys.exit(0)
# Create the tray
		
tray.setIcon(icon)
tray.setVisible(True)

		# Create the menu
menu = QMenu()

quit = QAction("Quit")
quit.triggered.connect(Window.app_quit)
menu.addAction(quit)

change_teto_act = QAction("Change to Teto!")
change_teto_act.triggered.connect(Window.change_teto)
menu.addAction(change_teto_act)

change_miku_act = QAction("Change to Miku!")
change_miku_act.triggered.connect(Window.change_miku)
menu.addAction(change_miku_act)

tray.setContextMenu(menu)
		
window = Window()
window.show()
app.exec()
sys.exit(app.exec())
