# Execute
# % pyqt6-tools designer


# Work UI : Spin Box with Qt Designer
# ...


# Save UI : qtdesigner_spin_box.ui


# Convert UI
# % pyuic6 -x qtdesigner_spin_box.ui -o qtdesigner_spin_box.py


# Add Method and Connect
# ...
#     self.spinBox.valueChanged.connect(self.spin_selected)
#
# def spin_selected(self):
#     if self.lineEdit.text() == '':
#         self.lineEdit.setText('Please Input Price Here!')
#     else:
#         price = int(self.lineEdit.text())
#         amount = self.spinBox.value()
#         self.lineEdit_2.setText(str(price * amount))
# ...