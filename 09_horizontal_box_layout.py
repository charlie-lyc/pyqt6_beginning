import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout
from PyQt6.QtGui import QIcon, QFont


#################################################
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PyQt6 Layouts - Horizontal Box')
        self.setWindowIcon(QIcon('qt_icon.png'))
        self.setGeometry(300, 300, 300, 500)

        btns = []
        for i in range(3):
            btns.append(QPushButton('Button '+ str(i + 1)))
        hbox = QHBoxLayout()
        for btn in btns:
            hbox.addWidget(btn)
        self.setLayout(hbox)


#################################################
def main():
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()