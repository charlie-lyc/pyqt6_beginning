import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QIcon, QAction
from PyQt6.QtCore import QCoreApplication


#################################################
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PyQt6 Menu')
        self.setWindowIcon(QIcon('qt_icon.png'))
        self.setGeometry(300, 300, 1000, 500)

        self.create_menu()

        ## setShortcut() 실행을 위해 Mac OS에서 설정
        self.setObjectName('MainWindow')

    def create_menu(self):
        main_menu = self.menuBar()

        ## Not Using Native Menu Bar on Mac OS
        main_menu.setNativeMenuBar(False)

        file_menu = main_menu.addMenu('File')

        ## Without Icon
        # new_action = QAction('New File', self)

        ## With Icon
        new_action = QAction(QIcon('qt_icon.png'), 'New File', self)
        ## Only on Window OS
        # new_action.setShortcut('Ctrl + N')
        ## 위의 단축키 표시 방법은 Mac OS에서 작동되지 않는 것 같아서 Qt Designer에서 시도해본 결과 아래와 같은 방법을 찾음
        new_action.setShortcut(QCoreApplication.translate('MainWindow', 'Meta+N'))
        file_menu.addAction(new_action)

        save_action = QAction('Save File', self)
        # new_action.setShortcut('Ctrl + S')
        save_action.setShortcut(QCoreApplication.translate('MainWindow', 'Meta+S'))
        file_menu.addAction(save_action)

        copy_action = QAction('Copy File', self)
        # new_action.setShortcut('Ctrl + C')
        copy_action.setShortcut(QCoreApplication.translate('MainWindow', 'Meta+C'))
        file_menu.addAction(copy_action)

        file_menu.addSeparator()

        exit_action = QAction('Exit', self)
        # new_action.setShortcut('Ctrl + E')
        exit_action.setShortcut(QCoreApplication.translate('MainWindow', 'Meta+E'))
        file_menu.addAction(exit_action)

        exit_action.triggered.connect(self.close_window)

    def close_window(self):
        self.close()


#################################################
def main():
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
