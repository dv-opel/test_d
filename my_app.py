from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout

app = QApplication([])

class MainWin(QWidget):
    def __init__(self):
        super().__init__()

        self.show()





main_window = MainWin()
app.exec_()