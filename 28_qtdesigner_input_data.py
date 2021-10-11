# SQL Reference
# ...
# CREATE DATABASE <dbname>;
# SHOW DATABASES;
# DROP DATABASE <dbname>;
#
# USE <dbname>;
#
# CREATE TABLE <tbname> (
#   column1 datatype,
#   column2 datatype,
#   ...
# );
#
# DESC <tbname>;
#
# SHOW TABLES;
# DROP TABLE <tbname>;
# ...

# Example of Creating Table (preparation in this file)
# ...
# CREATE TABLE users (
#   id INT NOT NULL AUTO_INCREMENT,
#   email VARCHAR(100) NOT NULL,
#   password VARCHAR(100) NOT NULL,
#   PRIMARY KEY (id)
# );
# ...

################################################################################

# Execute
# % pyqt6-tools designer


# Work UI : Input Data with Qt Designer
# ...


# Save UI : qtdesigner_input_data.ui


# Convert UI
# % pyuic6 -x qtdesigner_input_data.ui -o qtdesigner_input_data.py


# Add Method and Connect
# ...
#     self.pushButton.clicked.connect(self.input_data)
#
# def input_data(self):
#     try:
#         db = mc.connect(
#             host='localhost',
#             user='root',
#             password='',
#             database='pyqt6'
#         )
#         cursor = db.cursor()
#         email = self.email_lineEdit.text()
#         password = self.password_lineEdit.text()
#         cursor.execute('INSERT INTO users (email, password) VALUES (%s, %s)', (email, password))
#         db.commit() # !!!
#         self.result_label.setText('Data Successfully Input!')
#     except mc.Error as e:
#         self.result_label.setText('Data Input Failed.')
#     finally:
#         self.email_lineEdit.clear()
#         self.password_lineEdit.clear()
# ...




