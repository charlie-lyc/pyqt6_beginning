from PyQt6 import QtCore, QtGui, QtWidgets
import mysql.connector as mc


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1000, 500)
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(190, 80, 571, 271))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.dbCreate = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.dbCreate.setFont(font)
        self.dbCreate.setObjectName("dbCreate")
        self.horizontalLayout_2.addWidget(self.dbCreate)
        self.dbConnect = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.dbConnect.setFont(font)
        self.dbConnect.setObjectName("dbConnect")
        self.horizontalLayout_2.addWidget(self.dbConnect)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    ############################################################################
        self.dbCreate.clicked.connect(self.create_database)
        self.dbConnect.clicked.connect(self.connect_database)

    def create_database(self):
        try:
            db = mc.connect(
                host='localhost',
                user='root',
                password=''
            )
            cursor = db.cursor()
            dbname = self.lineEdit.text()
            query = 'CREATE DATABASE {}'.format(dbname)
            cursor.execute(query)
            self.label_2.setText('{} Database Successfully Created!'.format(dbname))
        except mc.Error as e:
            self.label_2.setText('Database Creation Failed.')
        finally:
            self.lineEdit.clear()

    def connect_database(self):
        try:
            dbname = self.lineEdit.text()
            db = mc.connect(
                host = 'localhost',
                user = 'root',
                password = '',
                database = dbname
            )
            self.label_2.setText('{} Database Connected!'.format(dbname))
        except mc.Error as e:
            self.label_2.setText('Database Not Connected.')
        finally:
            self.lineEdit.clear()
    ############################################################################

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Database with Qt Desinger"))
        self.label.setText(_translate("Form", "Database Name"))
        self.dbCreate.setText(_translate("Form", "Database Create"))
        self.dbConnect.setText(_translate("Form", "Database Connect"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
