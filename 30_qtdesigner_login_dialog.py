# Execute
# % pyqt6-tools designer


# Work UI : Login Dialog with Qt Designer
# ...


# Save UI : qtdesigner_login_dialog.ui


# Convert UI
# % pyuic6 -x qtdesigner_login_dialog.ui -o qtdesigner_login_dialog.py


# Add Method and Connect
# ...
#     self.pushButton.clicked.connect(self.log_in)
#
# def log_in(self):
#     try:
#         email = self.email_lineEdit.text()
#         password = self.password_lineEdit.text()
#         db = mc.connect(
#             host = 'localhost',
#             user = 'root',
#             password = '',
#             database = 'pyqt6'
#         )
#         cursor = db.cursor()
#         ####################################################################
#         # query = 'SELECT email, password FROM users WHERE email LIKE "' + email + '" AND password LIKE "' + password+ '"'
#         # cursor.execute(query)
#         # result = cursor.fetchone()
#         # print(result)
#         # if result == None:
#         #     self.result_label.setText('Incorrect email or password.')
#         # else:
#         #     self.result_label.setText('You are logged in.')
#         #     dialog = QtWidgets.QDialog()
#         #     dialog.setModal(True)
#         #     dialog.setWindowTitle('Welcome to Our Website!')
#         #     dialog.exec()
#         ####################################################################
#         query = 'SELECT email, password FROM users WHERE email="{}" AND password="{}"'.format(email, password)
#         cursor.execute(query)
#         result = cursor.fetchall()
#         if len(result) == 1:
#             self.result_label.setText('Successfully Logged In!')
#             dialog = QtWidgets.QDialog()
#             dialog.setModal(True)
#             dialog.setWindowTitle('Welcome to Our Website!')
#             dialog.exec()
#         else:
#             self.result_label.setText('Login Failed. Please Check Email and Password.')
#         ####################################################################
#     except mc.Error as e:
#         self.result_label.setText('Error in Login.')
#     finally:
#         self.email_lineEdit.clear()
#         self.password_lineEdit.clear()
# ...


