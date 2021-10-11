import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt6.QtGui import QIcon, QFont


#################################################
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PyQt6 Layouts - Vertical Box')
        self.setWindowIcon(QIcon('qt_icon.png'))
        self.setGeometry(300, 300, 300, 500)

        # btn1 = QPushButton('Button 1')
        # btn2 = QPushButton('Button 2')
        # btn3 = QPushButton('Button 3')
        ####################################
        btns = []
        for i in range(3):
            btns.append(QPushButton('Button '+ str(i + 1)))
        ####################################
        vbox = QVBoxLayout()
        # vbox.addWidget(btn1)
        # vbox.addWidget(btn2)
        # vbox.addWidget(btn3)
        ####################################
        for btn in btns:
            vbox.addWidget(btn)
        ####################################
        self.setLayout(vbox)


#################################################
def main():
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()