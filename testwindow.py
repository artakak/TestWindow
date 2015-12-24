#!-*-coding:utf-8-*-
import sys

# import PyQt4 QtCore and QtGui modules
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtGui
# from PyQt4 import uic
from ui_testwindow import Ui_MainWindow
from ui_testwidget import Ui_testwidget


#( Ui_MainWindow, QMainWindow ) = uic.loadUiType( 'ui_testwindow.ui' )

class MainWindow(QMainWindow):
    """MainWindow inherits QMainWindow"""

    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.ui.widget.hide)
        self.ui.pushButton_2.clicked.connect(self.ui.widget.show)

    def hide_w(self):
        self.ui.widget.hide()

    def __del__(self):
        self.ui = None


class testwidget(QtGui.QWidget):
    """MainWindow inherits QMainWindow"""

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_testwidget()
        self.ui.setupUi(self)

#-----------------------------------------------------#
if __name__ == '__main__':
    # create application
    app = QApplication(sys.argv)
    app.setApplicationName('TestWindow')

    # create widget
    w = MainWindow()
    w.setWindowTitle('TestWindow')
    w.show()

    # connection
    QObject.connect(app, SIGNAL('lastWindowClosed()'), app, SLOT('quit()'))

    # execute application
    sys.exit(app.exec_())