# Install
# % pip install pyqt6-tools

# Execute
# % pyqt6-tools designer

# Save in .ui file : ex) qt_designer_window.ui

# Load .ui file
import sys
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6 import uic

class UI(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('qtdesigner_window.ui', self)


if __name__ == '__main__':
    app = QApplication([])
    window = UI()
    window.show()
    sys.exit(app.exec())
