from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1000, 500)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(150, 80, 711, 321))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("background-color: green")
        self.tableWidget.setRowCount(3)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    ############################################################################
        self.input_table_data()

    def input_table_data(self):
        data = [
            ['First Name', 'Last Name', 'Eamil'],
            ['John', 'Doe', 'john@gmail.com'],
            ['Pete', 'Mitchell', 'pete@gmail.com']
        ]
        for i in range(len(data)):
            for j in range(len(data[i])):
                self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(data[i][j]))
    ############################################################################

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Table with Qt Designer"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("Form", "First Name"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("Form", "Last Name"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("Form", "Email"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
