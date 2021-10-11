from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 500)
        font = QtGui.QFont()
        font.setPointSize(14)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: green;\n"
"color: white;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        ########################################################################
        ## Not Using Native Menu Bar on Mac OS
        self.menubar.setNativeMenuBar(False)
        ########################################################################
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew_File = QtGui.QAction(MainWindow)
        self.actionNew_File.setCheckable(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("qt_icon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionNew_File.setIcon(icon)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.actionNew_File.setFont(font)
        ########################################################################
        ## AttributeError: type object 'Qt' has no attribute 'WindowShortcut'
        # self.actionNew_File.setShortcutContext(QtCore.Qt.WindowShortcut)
        ########################################################################
        self.actionNew_File.setAutoRepeat(False)
        self.actionNew_File.setShortcutVisibleInContextMenu(False)
        self.actionNew_File.setObjectName("actionNew_File")
        self.actionSave_File = QtGui.QAction(MainWindow)
        self.actionSave_File.setObjectName("actionSave_File")
        self.actionCopy_File = QtGui.QAction(MainWindow)
        self.actionCopy_File.setObjectName("actionCopy_File")
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setShortcutVisibleInContextMenu(True)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionNew_File)
        self.menuFile.addAction(self.actionSave_File)
        self.menuFile.addAction(self.actionCopy_File)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    ############################################################################
        self.actionExit.triggered.connect(self.close_window)

    def close_window(self):
        self.close()
    ############################################################################

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Menu(Main Window) with Qt Designer "))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionNew_File.setText(_translate("MainWindow", "New File"))
        self.actionNew_File.setShortcut(_translate("MainWindow", "Meta+N"))
        self.actionSave_File.setText(_translate("MainWindow", "Save File"))
        self.actionCopy_File.setText(_translate("MainWindow", "Copy File"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
