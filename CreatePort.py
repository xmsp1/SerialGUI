# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CreatePort.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(690, 620)
        font = QtGui.QFont()
        font.setPointSize(20)
        Form.setFont(font)
        self.gridLayout_3 = QtWidgets.QGridLayout(Form)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setMaximumSize(QtCore.QSize(260, 16777215))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 258, 600))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.layoutWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 10, 214, 107))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.com_showPort = QtWidgets.QComboBox(self.layoutWidget)
        self.com_showPort.setObjectName("com_showPort")
        self.gridLayout.addWidget(self.com_showPort, 0, 1, 1, 1)
        self.com_showRate = QtWidgets.QComboBox(self.layoutWidget)
        self.com_showRate.setObjectName("com_showRate")
        self.com_showRate.addItem("")
        self.com_showRate.addItem("")
        self.com_showRate.addItem("")
        self.gridLayout.addWidget(self.com_showRate, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.splitter = QtWidgets.QSplitter(self.scrollAreaWidgetContents)
        self.splitter.setGeometry(QtCore.QRect(10, 130, 191, 51))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.btn_searchPort = QtWidgets.QPushButton(self.splitter)
        self.btn_searchPort.setObjectName("btn_searchPort")
        self.btn_openFile = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.btn_openFile.setGeometry(QtCore.QRect(10, 190, 191, 41))
        self.btn_openFile.setObjectName("btn_openFile")
        self.btn_start = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.btn_start.setGeometry(QtCore.QRect(10, 320, 191, 41))
        self.btn_start.setObjectName("btn_start")
        self.btn_end = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.btn_end.setGeometry(QtCore.QRect(10, 380, 191, 41))
        self.btn_end.setObjectName("btn_end")
        self.btn_clearR = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.btn_clearR.setGeometry(QtCore.QRect(10, 430, 191, 41))
        self.btn_clearR.setObjectName("btn_clearR")
        self.text_showFile = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.text_showFile.setGeometry(QtCore.QRect(10, 240, 191, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.text_showFile.setFont(font)
        self.text_showFile.setObjectName("text_showFile")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_3.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.splitter_2 = QtWidgets.QSplitter(Form)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.groupBox = QtWidgets.QGroupBox(self.splitter_2)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.text_showR = QtWidgets.QTextEdit(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.text_showR.setFont(font)
        self.text_showR.setObjectName("text_showR")
        self.horizontalLayout.addWidget(self.text_showR)
        self.scrollArea_2 = QtWidgets.QScrollArea(self.splitter_2)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 404, 199))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.btn_clearS = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.btn_clearS.setObjectName("btn_clearS")
        self.gridLayout_2.addWidget(self.btn_clearS, 1, 0, 1, 1)
        self.btn_send = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.btn_send.setObjectName("btn_send")
        self.gridLayout_2.addWidget(self.btn_send, 1, 1, 1, 1)
        self.text_showS = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_2)
        self.text_showS.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.text_showS.setFont(font)
        self.text_showS.setObjectName("text_showS")
        self.gridLayout_2.addWidget(self.text_showS, 0, 0, 1, 2)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout_3.addWidget(self.splitter_2, 0, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "波特率"))
        self.com_showRate.setItemText(0, _translate("Form", "115200"))
        self.com_showRate.setItemText(1, _translate("Form", "9600"))
        self.com_showRate.setItemText(2, _translate("Form", "256000"))
        self.label.setText(_translate("Form", "串口号"))
        self.btn_searchPort.setText(_translate("Form", "查找串口"))
        self.btn_openFile.setText(_translate("Form", "打开文件"))
        self.btn_start.setText(_translate("Form", "开始"))
        self.btn_end.setText(_translate("Form", "停止"))
        self.btn_clearR.setText(_translate("Form", "清除"))
        self.groupBox.setTitle(_translate("Form", "接收区"))
        self.text_showR.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.btn_clearS.setText(_translate("Form", "清除"))
        self.btn_send.setText(_translate("Form", "发送"))

