from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 500)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(50, 50, 501, 251))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.checkBox = QtWidgets.QCheckBox(self.widget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout.addWidget(self.checkBox)
        self.checkBox_2 = QtWidgets.QCheckBox(self.widget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.horizontalLayout.addWidget(self.checkBox_2)
        self.checkBox_3 = QtWidgets.QCheckBox(self.widget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setObjectName("checkBox_3")
        self.horizontalLayout.addWidget(self.checkBox_3)
        self.checkBox_4 = QtWidgets.QCheckBox(self.widget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        self.checkBox_4.setFont(font)
        self.checkBox_4.setObjectName("checkBox_4")
        self.horizontalLayout.addWidget(self.checkBox_4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setStyleSheet("color: yellow;\nbackground-color: green;")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    ####################################################################
        self.checked_lngs = []
        self.chk_boxes = [self.checkBox, self.checkBox_2, self.checkBox_3, self.checkBox_4]
        for chk_box in self.chk_boxes:
            chk_box.toggled.connect(self.on_checked)

    def on_checked(self):
        for chk_box in self.chk_boxes:
            if chk_box.isChecked():
                if chk_box.text() not in self.checked_lngs:
                    self.checked_lngs.append(chk_box.text())
            else:
                if chk_box.text() in self.checked_lngs:
                    self.checked_lngs.remove(chk_box.text())
        lngs_str = ', '.join(self.checked_lngs)
        if not lngs_str:
            self.label.setText('What languages do you want to write?')
        else:
            self.label.setText('You have selected {}.'.format(lngs_str))
    ####################################################################

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Check Box with Qt Designer"))
        self.checkBox.setText(_translate("Form", "Python"))
        self.checkBox_2.setText(_translate("Form", "C++"))
        self.checkBox_3.setText(_translate("Form", "Java"))
        self.checkBox_4.setText(_translate("Form", "C#"))
        self.label.setText(_translate("Form", "What languages do you want to write?"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
