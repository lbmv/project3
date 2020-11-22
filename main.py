import sys
import random

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.do_paint = False
        self.setGeometry(300, 300, 666, 550)
        btn = QPushButton('Рисовать', self)
        btn.resize(200, 50)
        btn.move(235, 460)
        btn.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_circle(self, qp):
        qp.setBrush(QColor(random.randrange(0, 255), random.randrange(0, 255),
                           random.randrange(0, 255)))
        side = random.randrange(5, 100)
        qp.drawEllipse(random.randrange(0, 666 - side), random.randrange(0, 460 - side), side, side)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
