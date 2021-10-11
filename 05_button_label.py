import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt6.QtGui import QIcon, QFont


#################################################
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PyQt6 Button & Label')
        self.setWindowIcon(QIcon('qt_icon.png'))
        self.setGeometry(500, 500, 1000, 500)

        self.create_buttons()
        self.create_labels()

    def create_buttons(self):
        btn = QPushButton('Click Me', self)
        # btn.move(200, 200) # x-position, y-position
        btn.setGeometry(200, 200, 100, 100) # x-position, y-position, width, height
        btn.setStyleSheet('background-color: red')
        btn.setIcon(QIcon('qt_icon.png'))

    def create_labels(self):
        lbl = QLabel('My Label', self)
        # lbl.move(100, 200)
        lbl.setGeometry(100, 200, 100, 100)
        lbl.setStyleSheet('color: green')
        lbl.setFont(QFont('Times New Roman', 20))


#################################################
def main():
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()