# напиши здесь код для второго экрана приложения
from instr import *
from final_win import *

from PyQt5.QtCore import Qt, QTime, QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QFont

class Experiment():
    def __init__(self, age, test1, test2, test3):
        self.age = int(age)
        self.test1 = int(test1)
        self.test2 = int(test2)
        self.test3 = int(test3)

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
        self.lb_timer.setFont(QFont("Times", 36, QFont.Bold))

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

    def next_window(self):
        self.hide()
        self.exp = Experiment(self.le_age.text(), self.le_test1.text(), self.le_test2.text(), self.le_test3.text())
        self.final_win = FinalWin(self.exp)

    def connects(self):
        self.btn_next.clicked.connect(self.next_window)
        self.btn_test1.clicked.connect(self.timer_test)
        self.btn_test2.clicked.connect(self.timer_sits)
        self.btn_test3.clicked.connect(self.timer_final)
        
    def timer_test(self):
        self.time = QTime(0, 0, 15)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)

    def timer_sits(self):
        self.time = QTime(0, 0, 30)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2Event)
        self.timer.start(1500)
    
    def timer_final(self):
        self.time = QTime(0, 1, 0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer3Event)
        self.timer.start(1000)

    def timer1Event(self):
        self.time = self.time.addSecs(-1)
        self.lb_timer.setText(self.time.toString("hh:mm:ss"))
        self.lb_timer.setFont(QFont("Times", 36, QFont.Bold))
        self.lb_timer.setStyleSheet("color: rgb(0, 0, 0);")
        if self.time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()

    def timer2Event(self):
        self.time = self.time.addSecs(-1)
        self.lb_timer.setText(self.time.toString("hh:mm:ss")[6:8])
        self.lb_timer.setFont(QFont("Times", 36, QFont.Bold))
        self.lb_timer.setStyleSheet("color: rgb(0, 0, 0);")
        if self.time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()

    def timer3Event(self):
        self.time = self.time.addSecs(-1)
        self.lb_timer.setText(self.time.toString("hh:mm:ss"))
        self.lb_timer.setFont(QFont("Times", 36, QFont.Bold))
        if int(self.time.toString("hh:mm:ss")[6:8]) >= 45:
            self.lb_timer.setStyleSheet("color: rgb(0, 255, 0);")
        elif int(self.time.toString("hh:mm:ss")[6:8]) <= 15:
            self.lb_timer.setStyleSheet("color: rgb(0, 255, 0);")
        else:
            self.lb_timer.setStyleSheet("color: rgb(0, 0, 0);")
        if self.time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()

