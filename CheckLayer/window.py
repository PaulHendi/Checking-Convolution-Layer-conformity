# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(406, 661)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.spinBox = QtGui.QSpinBox(self.centralWidget)
        self.spinBox.setGeometry(QtCore.QRect(50, 80, 71, 27))
        self.spinBox.setMaximum(2999)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.spinBox_2 = QtGui.QSpinBox(self.centralWidget)
        self.spinBox_2.setGeometry(QtCore.QRect(140, 80, 71, 27))
        self.spinBox_2.setMaximum(2999)
        self.spinBox_2.setObjectName(_fromUtf8("spinBox_2"))
        self.spinBox_3 = QtGui.QSpinBox(self.centralWidget)
        self.spinBox_3.setGeometry(QtCore.QRect(240, 80, 71, 27))
        self.spinBox_3.setMaximum(9999)
        self.spinBox_3.setObjectName(_fromUtf8("spinBox_3"))
        self.spinBox_4 = QtGui.QSpinBox(self.centralWidget)
        self.spinBox_4.setGeometry(QtCore.QRect(50, 180, 48, 27))
        self.spinBox_4.setObjectName(_fromUtf8("spinBox_4"))
        self.spinBox_5 = QtGui.QSpinBox(self.centralWidget)
        self.spinBox_5.setGeometry(QtCore.QRect(130, 180, 48, 27))
        self.spinBox_5.setObjectName(_fromUtf8("spinBox_5"))
        self.spinBox_6 = QtGui.QSpinBox(self.centralWidget)
        self.spinBox_6.setGeometry(QtCore.QRect(50, 280, 48, 27))
        self.spinBox_6.setObjectName(_fromUtf8("spinBox_6"))
        self.spinBox_7 = QtGui.QSpinBox(self.centralWidget)
        self.spinBox_7.setGeometry(QtCore.QRect(130, 280, 48, 27))
        self.spinBox_7.setObjectName(_fromUtf8("spinBox_7"))
        self.spinBox_8 = QtGui.QSpinBox(self.centralWidget)
        self.spinBox_8.setGeometry(QtCore.QRect(210, 280, 48, 27))
        self.spinBox_8.setMaximum(9999)
        self.spinBox_8.setObjectName(_fromUtf8("spinBox_8"))
        self.spinBox_9 = QtGui.QSpinBox(self.centralWidget)
        self.spinBox_9.setGeometry(QtCore.QRect(300, 280, 48, 27))
        self.spinBox_9.setMaximum(9999)
        self.spinBox_9.setObjectName(_fromUtf8("spinBox_9"))
        self.label = QtGui.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(50, 50, 121, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(50, 150, 121, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(50, 250, 121, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.radioButton = QtGui.QRadioButton(self.centralWidget)
        self.radioButton.setGeometry(QtCore.QRect(50, 350, 117, 22))
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.pushButton = QtGui.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 420, 161, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.Result = QtGui.QLabel(self.centralWidget)
        self.Result.setGeometry(QtCore.QRect(60, 490, 261, 41))
        self.Result.setText(_fromUtf8(""))
        self.Result.setObjectName(_fromUtf8("Result"))
        self.pushButton_2 = QtGui.QPushButton(self.centralWidget)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 560, 161, 27))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 406, 25))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(MainWindow)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "Input dimension", None))
        self.label_2.setText(_translate("MainWindow", "Stride", None))
        self.label_3.setText(_translate("MainWindow", "Weight", None))
        self.radioButton.setText(_translate("MainWindow", "SAME", None))
        self.pushButton.setText(_translate("MainWindow", "Dim of ouput layer", None))
        self.pushButton_2.setText(_translate("MainWindow", "Push to input layer", None))

