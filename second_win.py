# напиши здесь код для второго экрана приложения
from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtGui import QFont, QIntValidator
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                            QPushButton, QVBoxLayout, QHBoxLayout,
                            QLineEdit)

from instr import *
from final_win import *

class Experiment:
    def __init__(self, age, test1, test2, test3):
        self.age = age
        self.t1 = test1
        self.t2 = test2
        self.t3 = test3


class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    
    def set_appear(self):
        self.setWindowTitle('Тест')
        self.resize(win_width, win_height)
    
    def initUI(self):
        self.btn_next = QPushButton(txt_sendresults)
        self.btn_test1 = QPushButton(txt_starttest1)
        self.btn_test2 = QPushButton(txt_starttest2)
        self.btn_test3 = QPushButton(txt_starttest3)

        self.text_name = QLabel('Введите ваше Ф.И.О.')
        self.text_age = QLabel('Введите ваш возраст')
        self.text_test1 = QLabel(txt_test1)
        self.text_test2 = QLabel(txt_test2)
        self.text_test3 = QLabel(txt_test3)
        self.text_timer = QLabel(txt_timer)
        self.text_timer.setFont(QFont('Times', 36, QFont.Bold))
        self.warning_test = QLabel('')
        self.warning_test.setFont(QFont('Montserrat', 14, QFont.Bold))
        self.warning_test.setStyleSheet('color: rgb(180, 64, 61)')

        self.line_name = QLineEdit('')
        self.line_age = QLineEdit('0')
        self.line_test1 = QLineEdit('0')
        self.line_test2 = QLineEdit('0')
        self.line_test3 = QLineEdit('0')

        self.validator = QIntValidator()
        self.line_age.setValidator(self.validator)
        self.line_test1.setValidator(self.validator)
        self.line_test2.setValidator(self.validator)
        self.line_test3.setValidator(self.validator)

        self.l_line = QVBoxLayout()
        self.r_line = QVBoxLayout()
        self.h_line = QHBoxLayout()
        self.r_line.addWidget(self.text_timer, alignment=Qt.AlignCenter)
        self.r_line.addWidget(self.warning_test, alignment=Qt.AlignCenter)
        self.l_line.addWidget(self.text_name, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_name, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.text_age, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_age, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.text_test1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.btn_test1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_test1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.text_test2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.btn_test2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.text_test3, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.btn_test3, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_test2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_test3, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.btn_next, alignment = Qt.AlignCenter)
        self.h_line.addLayout(self.l_line) 
        self.h_line.addLayout(self.r_line)       
        self.setLayout(self.h_line)
    
    def connects(self):
        self.btn_next.clicked.connect(self.next_click)
        self.btn_test1.clicked.connect(self.timer_test)
        self.btn_test2.clicked.connect(self.timer_sits)
        self.btn_test3.clicked.connect(self.timer_final)
    
    def timer_test(self):
        global time
        time = QTime(0, 0, 15)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)

    def timer_sits(self):
        global time
        time = QTime(0, 0, 30)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2Event)
        self.timer.start(1500)

    def timer_final(self):
        global time
        time = QTime(0, 1, 0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer3Event)
        self.timer.start(1000)

    def timer1Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString('hh:mm:ss'))
        self.text_timer.setFont(QFont('Times', 36, QFont.Bold))
        self.text_timer.setStyleSheet('color: rgb(0, 0, 0)')
        if time.toString('hh:mm:ss') == '00:00:00':
            self.timer.stop()
    
    def timer2Event(self):
        global time 
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString('hh:mm:ss')[6:8])
        self.text_timer.setFont(QFont('Times', 36, QFont.Bold))
        self.text_timer.setStyleSheet('color: rgb(0, 0, 0)')
        if time.toString('hh:mm:ss') == '00:00:00':
            self.timer.stop()
    
    def timer3Event(self):
        global time 
        time = time.addSecs(-1)
        if int(time.toString('hh:mm:ss')[6:8]) >= 45:
            self.text_timer.setStyleSheet('color: rgb(0, 255, 0)')
        elif int(time.toString('hh:mm:ss')[6:8]) <= 15:
            self.text_timer.setStyleSheet('color: rgb(0, 255, 0)')
        else:
            self.text_timer.setStyleSheet('color: rgb(255, 0, 0)')
        self.text_timer.setFont(QFont('Times', 36, QFont.Bold))
        self.text_timer.setText(time.toString('hh:mm:ss'))
        if time.toString('hh:mm:ss') == '00:00:00':
            self.timer.stop()

    def next_click(self):
        if self.line_test1.text() == '0' or self.line_test2.text() == '0' or self.line_test3.text() == '0':
            self.warning_test.setText('Результаты тестов не должны быть нулевыми!')
        else:
            self.hide()
            self.exp = Experiment(int(self.line_age.text()), int(self.line_test1.text()), int(self.line_test2.text()), int(self.line_test3.text()))
            self.fw = FinalWin(self.exp)
