from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import json

import sys


class Table(QTableWidget):
    def __init__(self, parent):
        super(Table, self).__init__(parent)
        self.setColumnCount(9)
        self.setRowCount(2)

        self.setItem(0, 0, QTableWidgetItem('A'))
        self.setItem(0, 1, QTableWidgetItem('B'))
        self.setItem(0, 2, QTableWidgetItem('C'))
        self.setItem(0, 3, QTableWidgetItem('D'))
        self.setItem(0, 4, QTableWidgetItem('E'))
        self.setItem(0, 5, QTableWidgetItem('F'))
        self.setItem(0, 6, QTableWidgetItem('A'))
        self.setItem(0, 7, QTableWidgetItem('C'))
        self.setItem(0, 8, QTableWidgetItem('1'))
        self.setItem(1, 0, QTableWidgetItem('A'))
        self.setItem(1, 1, QTableWidgetItem('B'))
        self.setItem(1, 2, QTableWidgetItem('C'))
        self.setItem(1, 3, QTableWidgetItem('D'))
        self.setItem(1, 4, QTableWidgetItem('E'))
        self.setItem(1, 5, QTableWidgetItem('F'))
        self.setItem(1, 6, QTableWidgetItem('A'))
        self.setItem(1, 7, QTableWidgetItem('C'))
        self.setItem(1, 8, QTableWidgetItem(''))

        for r in range(self.rowCount()):
            self.item(r, 6).setBackground(self.colour(self.item(r, 6).text()))
            self.item(r, 8).setBackground(self.colour(self.item(r, 8).text()))

    def colour(self, letter):
        if letter != '':
            colour = QColor('#bdf0d4')
        else:
            colour = QColor('#FF0000')
        return colour


def main():
    app = QApplication(sys.argv)
    window = QWidget()
    window.setGeometry(200, 200, 1000, 400)
    tw = Table(window)
    abc = []
    with open('abc.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        for a, b in enumerate(data):
            abc.append(b)
            tw.setHorizontalHeaderLabels(abc)
    twLayout = QVBoxLayout()
    twLayout.addWidget(tw)
    window.setLayout(twLayout)
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
