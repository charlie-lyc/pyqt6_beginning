import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QHBoxLayout, QLineEdit,
QLabel, QSpinBox)
from PyQt6.QtGui import QIcon, QFont


#################################################
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PyQt6 Spin Box')
        self.setWindowIcon(QIcon('qt_icon.png'))
        self.setGeometry(300, 300, 1000, 500)

        self.create_widgets_spin_box()

    def create_widgets_spin_box(self):
        hbox = QHBoxLayout()

        lbl = QLabel('Laptop Price: ')
        self.lnedit = QLineEdit()
        self.spnbox = QSpinBox()
        self.spnbox.valueChanged.connect(self.spin_selected)
        self.result = QLineEdit()

        hbox.addWidget(lbl)
        hbox.addWidget(self.lnedit)
        hbox.addWidget(self.spnbox)
        hbox.addWidget(self.result)

        self.setLayout(hbox)

    def spin_selected(self):
        if self.lnedit.text() == '':
            self.lnedit.setText('Please Input Price Here!')
        else:
            price = int(self.lnedit.text())
            amount = self.spnbox.value()
            self.result.setText(str(price * amount))


#################################################
def main():
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()








