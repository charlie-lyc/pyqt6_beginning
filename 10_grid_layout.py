import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout
from PyQt6.QtGui import QIcon, QFont


#################################################
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PyQt6 Layouts - Grid')
        self.setWindowIcon(QIcon('qt_icon.png'))
        self.setGeometry(300, 300, 300, 500)

        btns = []
        for i in range(6):
            btns.append(QPushButton('Button '+ str(i + 1)))
        grd = QGridLayout()
        ##############################
        # grd.addWidget(btns[0], 0, 0)
        # grd.addWidget(btns[1], 0, 1)
        # grd.addWidget(btns[2], 0, 2)
        # grd.addWidget(btns[3], 1, 0)
        # grd.addWidget(btns[4], 1, 1)
        # grd.addWidget(btns[5], 1, 2)
        ##############################
        for row in range(2):
            for clm in range(3):
                grd.addWidget(btns.pop(0), row, clm)
        self.setLayout(grd)


#################################################
def main():
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()