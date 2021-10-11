# Execute
# % pyqt6-tools designer


# Work UI : Table with Qt Designer
# ...


# Save UI : qtdesigner_table.ui


# Convert UI
# % pyuic6 -x qtdesigner_table.ui -o qtdesigner_table.py


# Add Method
# ...
#     self.input_table_data()
#
# def input_table_data(self):
#     data = [
#         ['First Name', 'Last Name', 'Eamil'],
#         ['John', 'Doe', 'john@gmail.com'],
#         ['Pete', 'Mitchell', 'pete@gmail.com']
#     ]
#     for i in range(len(data)):
#         for j in range(len(data[i])):
#             self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(data[i][j]))
# ...