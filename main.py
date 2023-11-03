import sys
from PyQt5 import uic, Qt
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QMainWindow
import random


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.setFixedSize(600, 600)
        self.qp = QPainter()
        self.qp.begin(self)
        self.do_paint = False
        self.ellipse_btn.clicked.connect(self.paint)
        self.x = 0
        self.y = 0

    def paintEvent(self, event):
        if self.do_paint:
            self.qp = QPainter()
            self.qp.begin(self)
            self.create()
            self.qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()
    def create(self):
        self.x = random.randint(0, 600)
        self.y = random.randint(0, 600)
        self.qp.setBrush(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0,255)))
        self.d = random.randint(50, 300)
        self.qp.drawEllipse(self.x, self.y, self.d, self.d)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    ex.create()
    sys.exit(app.exec())