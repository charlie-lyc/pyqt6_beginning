from PyQt6 import QtCore, QtGui, QtWidgets
import mysql.connector as mc


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1000, 500)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(220, 30, 591, 441))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.dbname_lineEdit = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.dbname_lineEdit.setFont(font)
        self.dbname_lineEdit.setObjectName("dbname_lineEdit")
        self.horizontalLayout.addWidget(self.dbname_lineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.tbname_lineEdit = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.tbname_lineEdit.setFont(font)
        self.tbname_lineEdit.setObjectName("tbname_lineEdit")
        self.horizontalLayout_2.addWidget(self.tbname_lineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.tableWidget.setFont(font)
        self.tableWidget.setObjectName("tableWidget")
        self.verticalLayout.addWidget(self.tableWidget)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    ############################################################################
        self.pushButton.clicked.connect(self.output_data)

    def output_data(self):
        try:
            dbname = self.dbname_lineEdit.text()
            tbname = self.tbname_lineEdit.text()
            db = mc.connect(
                host = 'localhost',
                user = 'root',
                password = '',
                database = dbname
            )
            cursor = db.cursor()
            query = 'SELECT * FROM {}'.format(tbname)
            cursor.execute(query)
            result = cursor.fetchall() # !!!
            # print(result)
            self.tableWidget.setRowCount(len(result))
            self.tableWidget.setColumnCount(len(result[0]))
            for i in range(len(result)):
                for j in range(len(result[i])):
                    ## QtWidgets.QTableWidgetItem() 메소드의 인자는 데이터 타입이 string 으로 고정
                    self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(result[i][j])))
        except mc.Error as e:
            print('Data Output Failed.')
        finally:
            self.dbname_lineEdit.clear()
            self.tbname_lineEdit.clear()
    ############################################################################

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Output Data with Qt Desginer"))
        self.label.setText(_translate("Form", "Database Name"))
        self.label_2.setText(_translate("Form", "         Table Name"))
        self.pushButton.setText(_translate("Form", "Output Data"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
