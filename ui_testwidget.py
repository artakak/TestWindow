# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testwidget.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_testwidget(object):
    def setupUi(self, testwidget):
        testwidget.setObjectName(_fromUtf8("testwidget"))
        testwidget.resize(400, 300)
        self.pushButton = QtGui.QPushButton(testwidget)
        self.pushButton.setGeometry(QtCore.QRect(40, 40, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(testwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(280, 40, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(testwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(280, 220, 75, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(testwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(40, 220, 75, 23))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_5 = QtGui.QPushButton(testwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(160, 120, 75, 23))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))

        self.retranslateUi(testwidget)
        QtCore.QMetaObject.connectSlotsByName(testwidget)

    def retranslateUi(self, testwidget):
        testwidget.setWindowTitle(_translate("testwidget", "Form", None))
        self.pushButton.setText(_translate("testwidget", "PushButton", None))
        self.pushButton_2.setText(_translate("testwidget", "PushButton", None))
        self.pushButton_3.setText(_translate("testwidget", "PushButton", None))
        self.pushButton_4.setText(_translate("testwidget", "PushButton", None))
        self.pushButton_5.setText(_translate("testwidget", "PushButton", None))

