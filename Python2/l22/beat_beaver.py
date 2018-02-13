import sys
import random

from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize


UNACTIVE = "bo1.png"
ACTIVE = "bo2.png"

class MyWindow(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		grid = QGridLayout()
		grid.setSpacing(10)

		self.holes = []
		k, n = 0, 0

		for i in range(9):
			self.holes.append(QPushButton("A", self))
			self.holes[i].setIcon(QIcon(UNACTIVE))
			self.holes[i].setIconSize(QSize(200, 200))

			grid.addWidget(self.holes[i], k, n)

			if k < 2:
				k += 1
			else:
				n += 1
				k = 0

		self.setWindowTitle("Бей бобра!")
		self.setGeometry(50, 50, 1024, 800)
		self.show()


if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = MyWindow()
	sys.exit(app.exec_())