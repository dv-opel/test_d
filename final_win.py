from instr import *

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout


class FinalWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.show()

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUI(self):
        self.lb_index = QLabel()
        self.lb_work = QLabel()

        self.vline = QVBoxLayout()
        self.vline.addWidget(self.lb_index, alignment= Qt.AlignCenter)
        self.vline.addWidget(self.lb_work, alignment= Qt.AlignCenter)
        self.setLayout(self.vline)

