from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (QApplication, QMainWindow, QAction, QLineEdit)
from PyQt5.QtGui import (QIcon, QPalette, QPixmap)
from PyQt5.QtCore import (QFile, QTextStream)
from Ui_mainwindow import Ui_MainWindow
import resources_rc
import sys


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
        self.setWindowTitle('OnePlus Hotel')
        self.setWindowIcon(QIcon(':/images/windowicon.png'))
        self.icon_login_title.setPixmap(QPixmap(':/images/windowicon.png'))
        self.icon_inputboard.setPixmap(QPixmap(':/images/hotel.png'))
        a1 = QAction(self.input_account)
        a1.setIcon(QIcon(':/images/account.png'))
        self.input_account.addAction(a1, QLineEdit.LeadingPosition)
        self.input_account.setPlaceholderText("请输入用户名")
        a1 = QAction(self.input_account)
        a1.setIcon(QIcon(':/images/password.png'))
        self.input_password.addAction(a1, QLineEdit.LeadingPosition)
        self.input_password.setPlaceholderText("请输入密码")
        self.text_tips.setReadOnly(True)
        setQSS(self, ':/style.qss')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = LogInWindow()
    win.show()
    app.exit(app.exec_())