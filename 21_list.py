import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLabel, QListWidget)
from PyQt6.QtGui import QIcon, QFont


#################################################
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PyQt6 List')
        self.setWindowIcon(QIcon('qt_icon.png'))
        self.setGeometry(300, 300, 1000, 500)

        self.create_list()

    def create_list(self):
        vbox = QVBoxLayout()

        self.lst = QListWidget()
        self.lst.clicked.connect(self.select_item)
        ##########################################
        # lst.insertItem(0, 'Python')
        # lst.insertItem(1, 'C++')
        # lst.insertItem(2, 'Java')
        # lst.insertItem(3, 'C#')
        ##########################################
        prg_lngs = ['Python', 'C++', 'Java', 'C#']
        for i in range(len(prg_lngs)):
            self.lst.insertItem(i, prg_lngs[i])
        ##########################################
        self.lst.setStyleSheet('background-color: yellow')

        self.lbl = QLabel('Programming Laguages')
        self.lbl.setFont(QFont('Times New Roman', 14))

        vbox.addWidget(self.lst)
        vbox.addWidget(self.lbl)

        self.setLayout(vbox)

    def select_item(self):
        selected_item = self.lst.currentItem()
        self.lbl.setText('You have selected {}.'.format(selected_item.text()))


#################################################
def main():
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
    


