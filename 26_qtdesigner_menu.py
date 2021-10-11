# Execute
# % pyqt6-tools designer


# Work UI : Menu(Main Window) with Qt Designer
# ...


# Save UI : qtdesigner_menu.ui


# Convert UI
# % pyuic6 -x qtdesigner_menu.ui -o qtdesigner_menu.py


# Add Method and Connect
# ...
# ########################################################################
#     ## Not Using Native Menu Bar on Mac OS
#     self.menubar.setNativeMenuBar(False)
# ########################################################################
#     ## AttributeError: type object 'Qt' has no attribute 'WindowShortcut'
#     # self.actionNew_File.setShortcutContext(QtCore.Qt.WindowShortcut)
# ########################################################################
#     self.actionExit.triggered.connect(self.close_window)
#
# def close_window(self):
#     self.close()
# ########################################################################
# ...
