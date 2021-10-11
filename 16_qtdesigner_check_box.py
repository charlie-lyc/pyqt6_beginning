# Execute
# % pyqt6-tools designer


# Work UI : Check Box with Qt Designer
# ...


# Save UI : qtdesigner_check_box.ui


# Convert UI
# % pyuic6 -x qtdesigner_check_box.ui -o qtdesigner_check_box.py


# Add Method and Connect
# ...
#     self.checked_lngs = []
#     self.chk_boxes = [self.checkBox, self.checkBox_2, self.checkBox_3, self.checkBox_4]
#     for chk_box in self.chk_boxes:
#         chk_box.toggled.connect(self.on_checked)
#
# def on_checked(self):
#     for chk_box in self.chk_boxes:
#         if chk_box.isChecked():
#             if chk_box.text() not in self.checked_lngs:
#                 self.checked_lngs.append(chk_box.text())
#         else:
#             if chk_box.text() in self.checked_lngs:
#                 self.checked_lngs.remove(chk_box.text())
#     lngs_str = ', '.join(self.checked_lngs)
#     if not lngs_str:
#         self.label.setText('What languages do you want to write?')
#     else:
#         self.label.setText('You have selected {}.'.format(lngs_str))
# ...