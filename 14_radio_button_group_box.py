import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
QGroupBox, QRadioButton, QLabel)
from PyQt6.QtGui import QIcon, QFont


#################################################
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PyQt6 Radio Button & Group Box')
        self.setWindowIcon(QIcon('qt_icon.png'))
        self.setGeometry(300, 300, 1000, 500)

        self.create_widgets_radio_btn()

        vbox = QVBoxLayout()
        vbox.addWidget(self.grpbox)

        self.lbl = QLabel('What language do you want to write?')
        self.lbl.setFont(QFont('Times New Roman', 18))
        vbox.addWidget(self.lbl)

        self.setLayout(vbox)

    def create_widgets_radio_btn(self):
        self.grpbox = QGroupBox('Choose Programming Language')
        self.grpbox.setFont(QFont('Times New Roman', 20))

        hbox = QHBoxLayout()
        ######################################################
        # self.radio_btn1 = QRadioButton('Python')
        # self.radio_btn1.setChecked(False)
        # self.radio_btn1.setFont(QFont('Times New Roman', 16))
        # self.radio_btn1.toggled.connect(self.on_selected)
        # hbox.addWidget(self.radio_btn1)
        #
        # self.radio_btn2 = QRadioButton('C++')
        # self.radio_btn2.setChecked(False)
        # self.radio_btn2.setFont(QFont('Times New Roman', 16))
        # self.radio_btn2.toggled.connect(self.on_selected)
        # hbox.addWidget(self.radio_btn2)
        #
        # self.radio_btn3 = QRadioButton('Java')
        # self.radio_btn3.setChecked(False)
        # self.radio_btn3.setFont(QFont('Times New Roman', 16))
        # self.radio_btn3.toggled.connect(self.on_selected)
        # hbox.addWidget(self.radio_btn3)
        #
        # self.radio_btn4 = QRadioButton('C#')
        # self.radio_btn4.setChecked(False)
        # self.radio_btn4.setFont(QFont('Times New Roman', 16))
        # self.radio_btn4.toggled.connect(self.on_selected)
        # hbox.addWidget(self.radio_btn4)
        ######################################################
        lng_lst = ['Python', 'C++', 'Java', 'C#']
        for i in range(len(lng_lst)):
            radio_btn = QRadioButton(lng_lst[i])
            radio_btn.setFont(QFont('Times New Roman', 16))
            radio_btn.setChecked(False)
            radio_btn.toggled.connect(self.on_selected)
            hbox.addWidget(radio_btn)
        ######################################################
        self.grpbox.setLayout(hbox)

    def on_selected(self):
        radio_btn = self.sender()
        if radio_btn.isChecked():
            self.lbl.setText('You have selected {}.'.format(radio_btn.text()))


#################################################
def main():
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()




