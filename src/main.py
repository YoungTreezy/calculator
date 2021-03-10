import sys
from PyQt5 import QtGui, QtCore, QtWidgets
from calc import *


class Gui(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.num_0.clicked.connect(self.num_0)
        self.ui.num_1.clicked.connect(self.num_1)
        self.ui.num_2.clicked.connect(self.num_2)
        self.ui.num_3.clicked.connect(self.num_3)
        self.ui.num_4.clicked.connect(self.num_4)
        self.ui.num_5.clicked.connect(self.num_5)
        self.ui.num_6.clicked.connect(self.num_6)
        self.ui.num_7.clicked.connect(self.num_7)
        self.ui.num_8.clicked.connect(self.num_8)
        self.ui.num_9.clicked.connect(self.num_9)
        self.ui.plus.clicked.connect(self.plus)
        self.ui.minus.clicked.connect(self.minus)
        self.ui.division.clicked.connect(self.division)
        self.ui.multiply.clicked.connect(self.multiply)
        self.ui.equally.clicked.connect(self.equally)
        self.ui.mod.clicked.connect(self.mod)
        self.ui.delete_all.clicked.connect(self.delete_all)

        self.arr = []
        self.first_num = 0
        self.second_num = 0
        self.answer = 0
        self.opp = ''

    def num_0(self):
        self.ui.textBrowser.insertPlainText(str(0))
        self.arr.append(0)

    def num_1(self):
        self.ui.textBrowser.insertPlainText(str(1))
        self.arr.append(1)

    def num_2(self):
        self.ui.textBrowser.insertPlainText(str(2))
        self.arr.append(2)

    def num_3(self):
        self.ui.textBrowser.insertPlainText(str(3))
        self.arr.append(3)

    def num_4(self):
        self.ui.textBrowser.insertPlainText(str(4))
        self.arr.append(4)

    def num_5(self):
        self.ui.textBrowser.insertPlainText(str(5))
        self.arr.append(5)

    def num_6(self):
        self.ui.textBrowser.insertPlainText(str(6))
        self.arr.append(6)

    def num_7(self):
        self.ui.textBrowser.insertPlainText(str(7))
        self.arr.append(7)

    def num_8(self):
        self.ui.textBrowser.insertPlainText(str(8))
        self.arr.append(8)

    def num_9(self):
        self.ui.textBrowser.insertPlainText(str(9))
        self.arr.append(9)

    def plus(self):
        self.ui.textBrowser.insertPlainText(' + ')
        self.opp = '+'
        self.first_num = ''.join(map(str, self.arr))
        self.arr = []

    def minus(self):
        self.ui.textBrowser.insertPlainText(' - ')
        self.opp = '-'
        self.first_num = ''.join(map(str, self.arr))
        self.arr = []

    def multiply(self):
        self.ui.textBrowser.insertPlainText(' * ')
        self.opp = '*'
        self.first_num = ''.join(map(str, self.arr))
        self.arr = []

    def division(self):
        self.ui.textBrowser.insertPlainText(' / ')
        self.opp = '/'
        self.first_num = ''.join(map(str, self.arr))
        self.arr = []

    def mod(self):
        self.ui.textBrowser.insertPlainText(' % ')
        self.opp = '%'
        self.first_num = ''.join(map(str, self.arr))
        self.arr = []

    def equally(self):
        self.ui.textBrowser.insertPlainText(' = ')
        self.second_num = ''.join(map(str, self.arr))
        self.arr = []
        if self.opp == '+':
            self.answer = int(self.first_num) + int(self.second_num)
            self.ui.textBrowser.insertPlainText(str(self.answer))
        elif self.opp == '-':
            self.answer = int(self.first_num) - int(self.second_num)
            self.ui.textBrowser.insertPlainText(str(self.answer))
        elif self.opp == '*':
            self.answer = int(self.first_num) * int(self.second_num)
            self.ui.textBrowser.insertPlainText(str(self.answer))
        elif self.opp == '/':
            self.answer = int(self.first_num) / int(self.second_num)
            self.ui.textBrowser.insertPlainText(str(self.answer))
        elif self.opp == '%':
            self.answer = int(self.first_num) % int(self.second_num)
            self.ui.textBrowser.insertPlainText(str(self.answer))
        self.answer = 0
        self.ui.textBrowser.append('')
        self.ui.textBrowser.append('')

    def delete_all(self):
        self.ui.textBrowser.setText('')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myapp = Gui()
    myapp.show()
    sys.exit(app.exec_())
