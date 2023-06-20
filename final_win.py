# напиши здесь код третьего экрана приложения
from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                            QPushButton, QVBoxLayout, QHBoxLayout,
                            QLineEdit)

from instr import *

class FinalWin(QWidget):
    def __init__(self, exp):
        super().__init__()
        self.res = ''
        self.index = (4 * (exp.t1 + exp.t2 + exp.t3) - 200) / 10
        self.age = exp.age
        self.get_result()
        self.set_appear()
        self.initUI()
        self.show()
    
    def set_appear(self):
        self.setWindowTitle('Результаты')
        self.resize(win_width, win_height)

    def initUI(self):
        self.text = QLabel('Результаты:' + self.res)
        self.index_text = QLabel('Индекс Руффье: ' + str(self.index))
        self.results = QLabel('Результаты: ' + self.res)
        
        self.text.setFont(QFont('Montserrat', 20, QFont.Bold))
        self.index_text.setFont(QFont('Montserrat', 20, QFont.Bold))

        self.layout = QVBoxLayout()

        self.layout.addWidget(self.text, alignment=Qt.AlignCenter)
        self.layout.addWidget(self.index_text, alignment=Qt.AlignCenter)

        self.setLayout(self.layout)

    def get_result(self):
        if self.age >= 7 and self.age <= 8:
            if self.index > 21:
                self.res = 'Низкий'
            elif self.index >= 17 and self.index <= 20.9:
                self.res = 'Удовлетворительный'
            elif self.index >= 12 and self.index <= 16.9:
                self.res = 'Средний'
            elif self.index >= 6.5 and self.index <= 11.9:
                self.res = 'Выше среднего'
            elif self.index <= 6.4:
                self.res = 'Высокий'
        if self.age >= 9 and self.age <= 10:
            if self.index > 19.5:
                self.res = 'Низкий'
            elif self.index >= 15.5 and self.index <= 19.4:
                self.res = 'Удовлетворительный'
            elif self.index >= 10.5 and self.index <= 15.4:
                self.res = 'Средний'
            elif self.index >= 5 and self.index <= 10.4:
                self.res = 'Выше среднего'
            elif self.index <= 4.9:
                self.res = 'Высокий'
        if self.age >= 11 and self.age <= 12:
            if self.index > 18:
                self.res = 'Низкий'
            elif self.index >= 14 and self.index <= 17.9:
                self.res = 'Удовлетворительный'
            elif self.index >= 9 and self.index <= 13.9:
                self.res = 'Средний'
            elif self.index >= 3.5 and self.index <= 8.9:
                self.res = 'Выше среднего'
            elif self.index <= 3.4:
                self.res = 'Высокий'
        if self.age >= 13 and self.age <= 14:
            if self.index > 16.5:
                self.res = 'Низкий'
            elif self.index >= 12.5 and self.index <= 16.4:
                self.res = 'Удовлетворительный'
            elif self.index >= 7.5 and self.index <= 12.4:
                self.res = 'Средний'
            elif self.index >= 2 and self.index <= 7.4:
                self.res = 'Выше среднего'
            elif self.index <= 1.9:
                self.res = 'Высокий'
        if self.age >= 15:
            if self.index > 15:
                self.res = 'Низкий'
            elif self.index >= 11 and self.index <= 14.9:
                self.res = 'Удовлетворительный'
            elif self.index >= 6 and self.index <= 10.9:
                self.res = 'Средний'
            elif self.index >= 0.5 and self.index <= 5.9:
                self.res = 'Выше среднего'
            elif self.index <= 0.4:
                self.res = 'Высокий'
        else:
            if self.age < 7:
                self.res = 'Нет результатов на такой возраст'
        
        if self.res == '':
            self.res = 'Результатов с таким индексом нет'
        
        
        
        