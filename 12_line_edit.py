import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QPushButton, QLabel,
QVBoxLayout, QHBoxLayout, QLineEdit)
from PyQt6.QtGui import QIcon, QFont


#################################################
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PyQt6 Line Edit')
        self.setWindowIcon(QIcon('qt_icon.png'))
        self.setGeometry(300, 300, 500, 300)

        self.create_line_edit()

    def create_line_edit(self):
        vbox = QVBoxLayout()

        self.lnedit = QLineEdit()
        self.btn = QPushButton('Click')
        self.btn.clicked.connect(self.clicked_btn)
        self.lbl = QLabel()

        hbox = QHBoxLayout()
        hbox.addWidget(self.btn)
        hbox.addWidget(self.lbl)

        vbox.addWidget(self.lnedit)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

    def clicked_btn(self):
        txt_input = self.lnedit.text()
        self.lbl.setText(txt_input)
        self.lnedit.clear()


#################################################
def main():
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()


    