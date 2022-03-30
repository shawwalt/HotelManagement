from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (QApplication, QMainWindow)
from PyQt5.QtGui import (QIcon, QPalette)
from PyQt5.QtCore import (QFile, QTextStream)
from Ui_mainwindow import Ui_MainWindow
import resources_rc
import sys

WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080
WINDOW_MUL = 6
WINDOW_DIV = 8


def setQSS(widget, style):
    f = QFile(style)
    f.open(QFile.ReadOnly | QFile.Text)
    stream = QTextStream(f)
    widget.setStyleSheet(stream.readAll())


class LogInWindow(Ui_MainWindow, QMainWindow):
    def __init__(self, *args, **kwargs):
        super(LogInWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.resetupUi()

    def resetupUi(self):
        a = WINDOW_MUL / WINDOW_DIV
        width, height = int(WINDOW_WIDTH * a), int(WINDOW_HEIGHT * a)
        self.resize(width, height)
        self.setWindowTitle('OnePlus Hotel')
        self.setWindowIcon(QIcon(':/images/windowicon.png'))
        setQSS(self, ':/style.qss')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = LogInWindow()
    win.show()
    app.exit(app.exec_())