# Execute
# % pyqt6-tools designer


# Work UI : TextEdit, Color & Font Dialog with Qt Designer
# ...


# Save UI : qtdesigner_textEdit_colorDialog_fontDialog.ui


# Convert UI
# % pyuic6 -x qtdesigner_textEdit_colorDialog_fontDialog.ui -o qtdesigner_textEdit_colorDialog_fontDialog.py


# Add Method and Connect
# ...
#     self.pushButton.clicked.connect(self.color_dialog)
#     self.pushButton_2.clicked.connect(self.font_dialog)
#
# def color_dialog(self):
#     color = QtWidgets.QColorDialog.getColor()
#     self.textEdit.setTextColor(color)
#
# def font_dialog(self):
#     (font, ok) = QtWidgets.QFontDialog.getFont()
#     if ok:
#         self.textEdit.setFont(font)
# ...
