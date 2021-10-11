# Execute
# % pyqt6-tools designer


# Work UI : Combo Box with Qt Designer
# ...


# Save UI : qtdesigner_combo_box.ui


# Convert UI
# % pyuic6 -x qtdesigner_combo_box.ui -o qtdesigner_combo_box.py


# Add Method and Connect
# ...
#     self.comboBox.currentTextChanged.connect(self.select_text)
#
# def select_text(self):
#     selected_txt = self.comboBox.currentText()
#     self.label.setText('You have selected {}.'.format(selected_txt))
# ...


