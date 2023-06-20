# напиши здесь код основного приложения и первого экрана
from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                            QPushButton, QVBoxLayout, QHBoxLayout,
                            QLineEdit)

from instr import *
from second_win import *


class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    
    def set_appear(self):
        self.setWindowTitle('Правила')
        self.resize(win_width, win_height)

    def initUI(self):
        self.btn_next = QPushButton('Начать')
        self.hello_text = QLabel(txt_hello)
        self.hello_text.setFont(QFont('Montserrat', 18, QFont.Bold))
        self.instruction = QLabel(txt_instruction)
        self.instruction.setFont(QFont('Montserrat', 12))

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.hello_text, alignment=Qt.AlignLeft)
        self.layout.addWidget(self.instruction, alignment=Qt.AlignLeft)
        self.layout.addWidget(self.btn_next, alignment=Qt.AlignCenter)

        self.setLayout(self.layout)

    def connects(self):
        self.btn_next.clicked.connect(self.next_click)

    def next_click(self):
        self.hide()
        self.tw = TestWin()

if __name__ == "__main__":
    app = QApplication([])
    win = MainWin()
    app.exec_()