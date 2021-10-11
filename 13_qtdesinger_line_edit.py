# Execute
# % pyqt6-tools designer


# Work UI : Line Edit with Qt Designer
# ...


# Save UI : qtdesigner_line_edit.ui


# Convert UI
# % pyuic6 -x qtdesigner_line_edit.ui -o qtdesigner_line_edit.py


# Add Method and Connect
# ...
#     self.pushButton.clicked.connect(self.clicked_btn)
#
# def clicked_btn(self):
#     txt_input = self.lineEdit.text()
#     self.label.setText(txt_input)
#     self.lineEdit.clear()
# ...