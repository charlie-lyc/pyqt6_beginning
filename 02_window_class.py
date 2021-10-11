import sys
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon


#################################################
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PyQt6 Window')
        self.setWindowIcon(QIcon('qt_icon.png')) # Not shown on Mac?

        # self.setFixedWidth(200)
        # self.setFixedHeight(200)
        self.setGeometry(500, 500, 200, 200) # x-position, y-position, width, height

        # self.setStyleSheet('background-color: red')
        style_sheet = (
            'background-color: red'
        )
        self.setStyleSheet(style_sheet)

#################################################
if __name__ == '__main__':
    # app = QApplication(sys.argv)
    ## OR
    app = QApplication([])

    window = Window()
    window.show()

    sys.exit(app.exec())