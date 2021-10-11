import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt6.QtGui import QIcon, QFont


#################################################
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PyQt6 Signal & Slots')
        self.setWindowIcon(QIcon('qt_icon.png'))
        self.setGeometry(500, 500, 1000, 500)

        self.create_widgets()

    def create_widgets(self):
        btn = QPushButton('Click Me', self)
        btn.setGeometry(200, 200, 100, 100)
        btn.setStyleSheet('background-color: red')
        btn.setIcon(QIcon('qt_icon.png'))
        self.lbl = QLabel('My Label', self)
        self.lbl.setGeometry(100, 200, 100, 100)
        self.lbl.setStyleSheet('color: green')
        self.lbl.setFont(QFont('Times New Roman', 15))
        ## Connect Method
        btn.clicked.connect(self.clicked_btn)

    def clicked_btn(self):
        self.lbl.setText('Text is changed')
        self.lbl.setStyleSheet('background-color: green')


#################################################
def main():
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()