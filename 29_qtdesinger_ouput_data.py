# Execute
# % pyqt6-tools designer


# Work UI : Output Data with Qt Designer
# ...


# Save UI : qtdesigner_output_data.ui


# Convert UI
# % pyuic6 -x qtdesigner_output_data.ui -o qtdesigner_output_data.py


# Add Method and Connect
# ...
#     self.pushButton.clicked.connect(self.output_data)
#
# def output_data(self):
#     try:
#         dbname = self.dbname_lineEdit.text()
#         tbname = self.tbname_lineEdit.text()
#         db = mc.connect(
#             host = 'localhost',
#             user = 'root',
#             password = '',
#             database = dbname
#         )
#         cursor = db.cursor()
#         query = 'SELECT * FROM {}'.format(tbname)
#         cursor.execute(query)
#         result = cursor.fetchall() # !!!
#         # print(result)
#         self.tableWidget.setRowCount(len(result))
#         self.tableWidget.setColumnCount(len(result[0]))
#         for i in range(len(result)):
#             for j in range(len(result[i])):
#                 ## QtWidgets.QTableWidgetItem() 메소드의 인자는 데이터 타입이 string 으로 고정
#                 self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(result[i][j])))
#     except mc.Error as e:
#         print('Data Output Failed.')
#     finally:
#         self.dbname_lineEdit.clear()
#         self.tbname_lineEdit.clear()
# ...




