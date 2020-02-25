# -*- coding: utf-8 -*-
import sys

import serial
import serial.tools.list_ports
from time import sleep
from PyQt5.QtWidgets import *
from CreatePort import Ui_Form
from PyQt5.QtGui import *
from PyQt5.QtCore import *
class Main(QWidget,Ui_Form):
        def __init__(self, parent=None):
            super(Main,self).__init__(parent)
            self.setupUi(self)
            self.setWindowTitle("小助手")
            print("初始化")
            self.dataS=""
            self.dataR=""

            #设置文本框的只读模式
            self.text_showR.setReadOnly(True)
            self.text_showFile.setReadOnly(True)


            self.btn_send.setEnabled(False)

            self.thread = Worker()  # 线程实例化
            self.ser = serial.Serial()  #串口实例化
            self.setSlot()

        def setSlot(self):
            print("信号槽的初始化")
            self.btn_searchPort.clicked.connect(self.searchPort)#查找串口号
            self.btn_start.clicked.connect(self.start)#启动线程
            self.btn_end.clicked.connect(self.end)#关闭线程
            self.btn_clearR.clicked.connect(self.clearR)#清除接受区数据
            self.btn_clearS.clicked.connect(self.clearS)#清除发送区数据
            self.btn_openFile.clicked.connect(self.openFile)#打开文件
            self.btn_send.clicked.connect(self.send)#发送选取的文件

            self.thread.sinOut1.connect(self.showR)#显示串口信息到接收区


            # self.text_showR.setPlainText("123")设定值
            # self.text_showS.setPlainText("456")
            #测试成功


        #查找串口号
        def searchPort(self):
            ch = list(serial.tools.list_ports.comports())
            print(ch)
            if len(ch) == 0:
                QMessageBox.about(self, "错误", "无法识别串口")
            else:
                self.com_showPort.clear()
                for ch1 in ch:
                    sh = str(ch1)
                    lens = sh.find('-')
                    self.com_showPort.addItem(sh[0:lens - 1])
        # 启动线程、
        def start(self):
            print("线程正常启动")
            try:
                self.thread.working = True
                self.thread.start()

                self.btn_searchPort.setEnabled(False)
                self.btn_openFile.setEnabled(False)
                self.btn_start.setEnabled(False)
                self.btn_send.setEnabled(True)

            except:
                QMessageBox.about(self, "错误", "启动失败")
        #关闭线程
        def end(self):
            print()#换行
            print("成功关闭线程")
            try:
                self.thread.working = False
                self.btn_searchPort.setEnabled(True)
                self.btn_openFile.setEnabled(True)
                self.btn_start.setEnabled(True)
                self.btn_send.setEnabled(False)
            except:
                QMessageBox.about(self, "错误", "关闭线程出错")
        #清除接收区数据
        def clearR(self):
            print("成功清除接收区数据")
            self.text_showR.clear()
            self.dataR=""

            # 清除发送区数据
        # 清除发送区数据
        def clearS(self):
            print("成功清除发送区数据")
            self.text_showS.clear()
        #打开文件
        def openFile(self):
            print("成功打开文件")
            dlg=QFileDialog()
            dlg.setFileMode(QFileDialog.AnyFile)
            dlg.setFilter(QDir.Files)
            if dlg.exec_():
                fileNames=dlg.selectedFiles()
                self.text_showFile.setPlainText(fileNames[0])
                try:
                    f=open(fileNames[0], 'r',encoding='UTF-8')
                    self.dataS=f.read()
                    f.close()
                    self.text_showS.setPlainText(self.dataS)
                except:
                    QMessageBox.about(self, "错误", "出现异常")
                    print("出现异常")
                    f.close()
        #发送文件
        def send(self):
            self.dataS=self.text_showS.toPlainText()
            # print("长度：",len(self.dataS))
            if len(self.dataS)>0:
                # print(type(self.dataS))
                # print(self.dataS)
                print("正在发送中")
                self.ser.write(self.dataS.encode('utf-8'))
                print(3)
            else:
                QMessageBox.about(self, "错误", "发送内容为空")
        # 显示串口信息到接收区

        def showR(self,sh):
            # self.text_showR.clear()
            self.dataR=self.dataR+sh
            self.text_showR.setPlainText(self.dataR)


class Worker(QThread):
    sinOut1 = pyqtSignal(str)

    def __init__(self, parent=None):
        super(Worker, self).__init__(parent)
        self.working = True

    def __del__(self):
        # 线程状态改变与线程终止
        self.working = False
        self.wait()

    def run(self):

        print("线程运行")
        Port=main.com_showPort.currentText()
        Rate=main.com_showRate.currentText()
        if Port.find("COM")!=-1:
            print(2)
            main.ser.setPort(Port)
            main.ser.baudrate=Rate

            main.ser.open()
            try:
                while self.working == True:
                    # pass
                    print("线程开启")
                    num1 = main.ser.readline()
                    num2 = str(num1, 'utf-8')
                    # print(num1)
                    position2 = num2.find('\n')
                    if position2 == 1:
                        self.sinOut1[str].emit(num2[0:1])
                    else:
                        self.sinOut1[str].emit(num2[0:position2 - 1])
                    # self.sinOut1[str].emit(num2)

                main.ser.close()
            except:
                print("串口读取数据失败")
                QMessageBox.about(main, "错误", "串口读取数据失败")
        else:
            QMessageBox.about(main, "错误", "请检查是否配置好串口")



if __name__=="__main__":
    app=QApplication (sys.argv)
    main=Main()
    main.show()
    sys.exit(app.exec_())