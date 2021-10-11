import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLabel, QComboBox)
from PyQt6.QtGui import QIcon, QFont


#################################################
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PyQt6 Combo Box')
        self.setWindowIcon(QIcon('qt_icon.png'))
        self.setGeometry(300, 300, 1000, 500)

        self.create_combo_box()

    def create_combo_box(self):
        vbox = QVBoxLayout()

        self.combo = QComboBox()
        ## 다른 widget 들의 경우와 달리 최초에 마운트 되면서 combo box의 첫번째 item 이 자동 선택되므로
        ## 아래와 같은 위치에서 method 를 connect 할 경우 자동 실행으로 인해 에러가 발생된다.
        # self.combo.currentTextChanged.connect(self.select_text) # AttributeError: 'Window' object has no attribute 'lbl'
        #########################################
        # self.combo.addItem('Python')
        # self.combo.addItem('C++')
        # self.combo.addItem('Java')
        # self.combo.addItem('C#')
        #########################################
        prg_lngs = ['Python', 'C++', 'Java', 'C#']
        for i in range(len(prg_lngs)):
            self.combo.addItem(prg_lngs[i])
        #########################################

        self.lbl = QLabel('Programming Laguages')
        self.lbl.setFont(QFont('Times New Roman', 14))

        vbox.addWidget(self.combo)
        vbox.addWidget(self.lbl)

        self.setLayout(vbox)

        ## 따라서 AttributeError가 발생되지 않기 위해서
        ## 모든 widget 들이 마운트 된 다음에 method 를 connect 하는 것이 안전하다.
        self.combo.currentTextChanged.connect(self.select_text)

    def select_text(self):
        selected_txt = self.combo.currentText()
        self.lbl.setText('You have selected {}.'.format(selected_txt))


#################################################
def main():
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()


