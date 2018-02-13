import sys
from PyQt5.QtWidgets import QApplication, QWidget

class MyWindow(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.setWindowTitle("Моё первое приложение!")
		self.setGeometry(100, 100, 800, 500)
		self.show()


if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = MyWindow()
	sys.exit(app.exec_())