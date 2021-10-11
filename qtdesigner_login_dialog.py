from PyQt6 import QtCore, QtGui, QtWidgets
import mysql.connector as mc


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1000, 500)
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(240, 80, 521, 301))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.email_lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.email_lineEdit.setFont(font)
        self.email_lineEdit.setObjectName("email_lineEdit")
        self.horizontalLayout.addWidget(self.email_lineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.password_lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.password_lineEdit.setFont(font)
        self.password_lineEdit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.horizontalLayout_2.addWidget(self.password_lineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.result_label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.result_label.setFont(font)
        self.result_label.setText("")
        self.result_label.setObjectName("result_label")
        self.verticalLayout.addWidget(self.result_label)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    ############################################################################
        self.pushButton.clicked.connect(self.log_in)

    def log_in(self):
        try:
            email = self.email_lineEdit.text()
            password = self.password_lineEdit.text()
            db = mc.connect(
                host = 'localhost',
                user = 'root',
                password = '',
                database = 'pyqt6'
            )
            cursor = db.cursor()
            ####################################################################
            # query = 'SELECT email, password FROM users WHERE email LIKE "' + email + '" AND password LIKE "' + password+ '"'
            # cursor.execute(query)
            # result = cursor.fetchone()
            # print(result)
            # if result == None:
            #     self.result_label.setText('Incorrect email or password.')
            # else:
            #     self.result_label.setText('You are logged in.')
            #     dialog = QtWidgets.QDialog()
            #     dialog.setModal(True)
            #     dialog.setWindowTitle('Welcome to Our Website!')
            #     dialog.exec()
            ####################################################################
            query = 'SELECT email, password FROM users WHERE email="{}" AND password="{}"'.format(email, password)
            cursor.execute(query)
            result = cursor.fetchall()
            if len(result) == 1:
                self.result_label.setText('Successfully Logged In!')
                dialog = QtWidgets.QDialog()
                dialog.setModal(True)
                dialog.setWindowTitle('Welcome to Our Website!')
                dialog.exec()
            else:
                self.result_label.setText('Login Failed. Please Check Email and Password.')
            ####################################################################
        except mc.Error as e:
            self.result_label.setText('Error in Login.')
        finally:
            self.email_lineEdit.clear()
            self.password_lineEdit.clear()
    ############################################################################

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Login Dialog with Qt Designer"))
        self.label.setText(_translate("Form", "         Email"))
        self.label_2.setText(_translate("Form", "Password"))
        self.pushButton.setText(_translate("Form", "Log In"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
