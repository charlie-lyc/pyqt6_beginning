# Install MySQL Server
# % brew install mysql

# Install MySQL Client
# % brew install mysql-client

# Start MySQL Server
# % brew services start mysql

# Connect to MySQL Server
# % mysql -u <user> -p <password> -h <host>

################################################################################

# Install mysql-connector-python 8.0.26
# % pip install mysql-connector-python

################################################################################

# Execute
# % pyqt6-tools designer


# Work UI : Database with Qt Designer
# ...


# Save UI : qtdesigner_create_connect_database.ui


# Convert UI
# % pyuic6 -x qtdesigner_create_connect_database.ui -o qtdesigner_create_connect_database.py


# Add Method and Connect
# ...
#     self.dbCreate.clicked.connect(self.create_database)
#     self.dbConnect.clicked.connect(self.connect_database)
#
# def create_database(self):
#     try:
#         db = mc.connect(
#             host='localhost',
#             user='root',
#             password=''
#         )
#         cursor = db.cursor()
#         dbname = self.lineEdit.text()
#         cursor.execute('CREATE DATABASE {}'.format(dbname))
#         self.label_2.setText('{} Database Successfully Created!'.format(dbname))
#     except mc.Error as e:
#         self.label_2.setText('Database Creation Failed.')
#
# def connect_database(self):
#     try:
#         dbname = self.lineEdit.text()
#         db = mc.connect(
#             host='localhost',
#             user='root',
#             password='',
#             database='{}'.format(dbname)
#         )
#         self.label_2.setText('{} Database Connected!'.format(dbname))
#     except mc.Error as e:
#         self.label_2.setText('Database Not Connected.')
# ...
