################################################################################
##
## BY: WANDERSON M.PIMENTA
## PROJECT MADE WITH: Qt Designer and PySide2
## V: 1.0.0
##
################################################################################

import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

# GUI FILE
from ui_main import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # SET VALUE TO 0
        self.ui.progressBar.setValue(0)

        # EXPAND BTN
        self.ui.btnExpand.clicked.connect(self.expand)

        # RETRACT BTN
        self.ui.btnRetract.clicked.connect(self.retract)

        # RESIZE MAIN WINDOW
        self.ui.btnResizeWindow.clicked.connect(lambda: self.resizeMainWindow(1200,500))


        # SHOW WINDOW
        self.show()

    # FUNCTION TO EXPAND PROGRESS BAR OR ANOTHER WIDGET
    def expand(self):
        # CREATE ANIMATION
        self.animation = QPropertyAnimation(self.ui.progressBar, b"value")
        self.animation.setDuration(2000)
        self.animation.setStartValue(0)
        self.animation.setEndValue(100)
        self.animation.setEasingCurve(QtCore.QEasingCurve.Linear)
        self.animation.start()

    def retract(self):
        # CREATE ANIMATION
        self.animation = QPropertyAnimation(self.ui.progressBar, b"value")
        self.animation.setDuration(2000)
        self.animation.setStartValue(100)
        self.animation.setEndValue(0)
        self.animation.setEasingCurve(QtCore.QEasingCurve.Linear)
        self.animation.start()

    def resizeMainWindow(self, width, height):
        # CREATE ANIMATION
        self.animation = QPropertyAnimation(self, b"size")
        self.animation.setDuration(1000)
        self.animation.setEndValue(QtCore.QSize(width,height))
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuad)
        self.animation.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())