import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QTableWidget,
QTableWidgetItem)
from PyQt6.QtGui import QIcon, QFont


#################################################
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PyQt6 Table')
        self.setWindowIcon(QIcon('qt_icon.png'))
        self.setGeometry(300, 300, 1000, 500)

        self.create_table()

    def create_table(self):
        vbox = QVBoxLayout()

        tbl = QTableWidget()
        tbl.setRowCount(3)
        tbl.setColumnCount(3)

        #######################################################
        # table.setItem(0, 0, QTableWidgetItem('First Name'))
        # table.setItem(0, 1, QTableWidgetItem('Last Name'))
        # table.setItem(0, 2, QTableWidgetItem('Email'))
        #
        # table.setItem(1, 0, QTableWidgetItem('John'))
        # table.setItem(1, 1, QTableWidgetItem('Doe'))
        # table.setItem(1, 2, QTableWidgetItem('john@gmail.com'))
        #
        # table.setItem(2, 0, QTableWidgetItem('Pete'))
        # table.setItem(2, 1, QTableWidgetItem('Mitchell'))
        # table.setItem(2, 2, QTableWidgetItem('pete@gmail.com'))
        #######################################################
        data = [
            ['First Name', 'Last Name', 'Eamil'],
            ['John', 'Doe', 'john@gmail.com'],
            ['Pete', 'Mitchell', 'pete@gmail.com']
        ]
        for i in range(len(data)):
            for j in range(len(data[i])):
                tbl.setItem(i, j, QTableWidgetItem(data[i][j]))
        #######################################################

        tbl.setStyleSheet('background-color: yellow')
        tbl.setFont(QFont('Times New Roman', 14))

        vbox.addWidget(tbl)
        self.setLayout(vbox)


#################################################
def main():
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
    


