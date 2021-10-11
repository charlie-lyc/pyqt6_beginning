# Execute
# % pyqt6-tools designer


# Work UI : Button & Label with Qt Designer
# ...


# Save UI : qtdesigner_button_label.ui


# Convert UI
# % pyuic6 -x qtdesigner_button_label.ui -o qtdesigner_button_label.py


# Add Method and Connect
# ...
#     self.pushButton.clicked.connect(self.clicked_btn)
#
# def clicked_btn(self):
#     self.label.setText('Text is changed')
#     self.label.setStyleSheet('background-color: green')
# ...