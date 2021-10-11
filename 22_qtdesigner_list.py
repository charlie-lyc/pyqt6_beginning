# Execute
# % pyqt6-tools designer


# Work UI : List with Qt Designer
# ...


# Save UI : qtdesigner_list.ui


# Convert UI
# % pyuic6 -x qtdesigner_list.ui -o qtdesigner_list.py


# Add Method and Connect
# ...
#     self.listWidget.clicked.connect(self.select_item)
#
# def select_item(self):
#     selected_item = self.listWidget.currentItem()
#     self.label.setText('You have selected {}.'.format(selected_item.text()))
# ...