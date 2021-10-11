from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(1000, 500)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("qt_icon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Form.setWindowIcon(icon)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(200, 200, 100, 100))
        self.pushButton.setStyleSheet("background-color: red\n")
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(100, 200, 100, 100))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setStyleSheet("color: green\n")
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    #######################################################
        self.pushButton.clicked.connect(self.clicked_btn)

    def clicked_btn(self):
        self.label.setText('Text is changed')
        self.label.setStyleSheet('background-color: green')
    #######################################################

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Button & Label with Qt Designer"))
        self.pushButton.setText(_translate("Form", "Click Me"))
        self.label.setText(_translate("Form", "My Label"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
