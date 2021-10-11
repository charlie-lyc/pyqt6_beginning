import sys
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon, QPaintEvent, QPainter, QPen, QBrush, QTextDocument
from PyQt6.QtCore import Qt, QRect, QRectF


#################################################
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PyQt6 Menu')
        self.setWindowIcon(QIcon('qt_icon.png'))
        self.setGeometry(300, 300, 1000, 500)

    # def paintEvent(self, a0: QPaintEven) -> None: # PyCharm !!!
    def paintEvent(self, e): # Keep Method Name !!!
        painter = QPainter(self)
        ########################################################################
        ## 1. Draw Rectangle

        ## Default 설정으로 도형을 그림
        # painter.drawRect(100, 100, 300, 100) # x(left), y(top), width, height

        ## 다양하게 설정하여 도형을 그림
        # # painter.setPen(QPen(Qt.GlobalColor.black, 5, Qt.PenStyle.SolidLine))
        # painter.setPen(QPen(Qt.GlobalColor.black, 5, Qt.PenStyle.DashDotLine))
        #
        # # painter.setBrush(QBrush(Qt.GlobalColor.green, Qt.BrushStyle.SolidPattern))
        # painter.setBrush(QBrush(Qt.GlobalColor.green, Qt.BrushStyle.DiagCrossPattern))
        #
        # painter.drawRect(100, 100, 300, 100)
        ########################################################################
        ## 2. Draw Ellipse

        # painter.setPen(QPen(Qt.GlobalColor.yellow, 5, Qt.PenStyle.SolidLine))
        #
        # # painter.setBrush(QBrush(Qt.GlobalColor.green, Qt.BrushStyle.Dense1Pattern))
        # painter.setBrush(QBrush(Qt.GlobalColor.green, Qt.BrushStyle.Dense5Pattern))
        #
        # painter.drawEllipse(100, 100, 300, 200)
        ########################################################################
        ## 3. Draw Text

        painter.drawText(100, 100, 'PyQt6 Draw Text')

        rect = QRect(100, 100, 300, 300)
        painter.drawRect(rect)
        painter.drawText(rect, Qt.AlignmentFlag.AlignCenter, 'PyQt6 Draw Text in Rectangle')
        ########################################################################
        ## 4. Draw HTML

        document = QTextDocument()
        rectf = QRectF(0, 0, 250, 25)
        document.setTextWidth(rectf.width())
        document.setHtml('<b><i>PyQt6 Draw HTML<i></b>')
        document.drawContents(painter, rectf)


#################################################
def main():
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
