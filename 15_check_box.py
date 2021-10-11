import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
QCheckBox, QLabel)
from PyQt6.QtGui import QIcon, QFont


#################################################
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PyQt6 Check Box')
        self.setWindowIcon(QIcon('qt_icon.png'))
        self.setGeometry(300, 300, 1000, 500)

        self.create_widgets_check_box()
        self.checked_lngs = []

    def create_widgets_check_box(self):
        hbox = QHBoxLayout()
        ######################################################
        # self.chk_box1 = QCheckBox('Python')
        # self.chk_box1.setChecked(False)
        # self.chk_box1.setFont(QFont('Times New Roman', 16))
        # self.chk_box1.toggled.connect(self.on_checked)
        # hbox.addWidget(self.chk_box1)
        #
        # self.chk_box2 = QCheckBox('C++')
        # self.chk_box2.setChecked(False)
        # self.chk_box2.setFont(QFont('Times New Roman', 16))
        # self.chk_box2.toggled.connect(self.on_checked)
        # hbox.addWidget(self.chk_box2)
        #
        # self.chk_box3 = QCheckBox('Java')
        # self.chk_box3.setChecked(False)
        # self.chk_box3.setFont(QFont('Times New Roman', 16))
        # self.chk_box3.toggled.connect(self.on_checked)
        # hbox.addWidget(self.chk_box3)
        #
        # self.chk_box4 = QCheckBox('C#')
        # self.chk_box4.setChecked(False)
        # self.chk_box4.setFont(QFont('Times New Roman', 16))
        # self.chk_box4.toggled.connect(self.on_checked)
        # hbox.addWidget(self.chk_box4)
        ######################################################
        lng_lst = ['Python', 'C++', 'Java', 'C#']
        for i in range(len(lng_lst)):
            chk_box = QCheckBox(lng_lst[i])
            chk_box.setFont(QFont('Times New Roman', 16))
            chk_box.setChecked(False)
            chk_box.toggled.connect(self.on_checked)
            hbox.addWidget(chk_box)
        ######################################################
        vbox = QVBoxLayout()
        vbox.addLayout(hbox)

        self.lbl = QLabel('What languages do you want to write?')
        self.lbl.setFont(QFont('Times New Roman', 18))
        vbox.addWidget(self.lbl)

        self.setLayout(vbox)

    def on_checked(self):
        chk_box = self.sender()
        if chk_box.isChecked():
            self.checked_lngs.append(chk_box.text())
            # print(self.checked_lngs)
        else:
            self.checked_lngs.remove(chk_box.text())
            # print(self.checked_lngs)

        lngs_str = ', '.join(self.checked_lngs)
        if not lngs_str:
            self.lbl.setText('What languages do you want to write?')
        else:
            self.lbl.setText('You have selected {}.'.format(lngs_str))


#################################################
def main():
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()


