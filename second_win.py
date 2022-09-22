# напиши здесь код для второго экрана приложения
from instr import *
from final_win import *

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout


class SecWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUI(self):
        self.lb_name = QLabel(txt_name)
        self.lb_age = QLabel(txt_age)
        self.lb_test1 = QLabel(txt_test1)
        self.lb_test2 = QLabel(txt_test2)
        self.lb_test3 = QLabel(txt_test3)
        self.lb_timer = QLabel(txt_timer)

        self.btn_test1 = QPushButton(txt_starttest1)
        self.btn_test2 = QPushButton(txt_starttest2)
        self.btn_test3 = QPushButton(txt_starttest3)
        self.btn_next = QPushButton(txt_sendresults)

        self.le_name = QLineEdit(txt_hintname)
        self.le_age = QLineEdit(txt_hintage)
        self.le_test1 = QLineEdit(txt_hinttest1)
        self.le_test2 = QLineEdit(txt_hinttest2)
        self.le_test3 = QLineEdit(txt_hinttest3)

        self.hline = QHBoxLayout()
        self.vline_l = QVBoxLayout()
        self.vline_r = QVBoxLayout()
        self.vline_r.addWidget(self.lb_timer, alignment=Qt.AlignCenter)
        self.vline_l.addWidget(self.lb_name, alignment=Qt.AlignLeft)
        self.vline_l.addWidget(self.le_name, alignment=Qt.AlignLeft)
        self.vline_l.addWidget(self.lb_age, alignment=Qt.AlignLeft)
        self.vline_l.addWidget(self.le_age, alignment=Qt.AlignLeft)
        self.vline_l.addWidget(self.lb_test1, alignment = Qt.AlignLeft)
        self.vline_l.addWidget(self.btn_test1, alignment = Qt.AlignLeft)
        self.vline_l.addWidget(self.le_test1, alignment = Qt.AlignLeft)
        self.vline_l.addWidget(self.lb_test2, alignment = Qt.AlignLeft)
        self.vline_l.addWidget(self.btn_test2, alignment = Qt.AlignLeft)
        self.vline_l.addWidget(self.lb_test3, alignment = Qt.AlignLeft)
        self.vline_l.addWidget(self.btn_test3, alignment = Qt.AlignLeft)
        self.vline_l.addWidget(self.le_test2, alignment = Qt.AlignLeft)
        self.vline_l.addWidget(self.le_test3, alignment = Qt.AlignLeft)
        self.vline_l.addWidget(self.btn_next, alignment = Qt.AlignCenter)

        self.hline.addLayout(self.vline_l)
        self.hline.addLayout(self.vline_r)
        self.setLayout(self.hline)


    def connects(self):
        self.btn_next.clicked.connect(self.next_window)
        
    def next_window(self):
        self.hide()
        self.final_win = FinalWin()
