# -*- coding: utf-8 -*-
import struct
import sys
import time
import serial
import serial.tools.list_ports
from time import sleep
from PyQt5.QtWidgets import *
from CreatePort import Ui_Form
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import os
from PyQt5.QtWebEngineWidgets import QWebEngineView
class Main(QWidget,Ui_Form):
        def __init__(self, parent=None):
            super(Main,self).__init__(parent)
            self.setupUi(self)
            self.setWindowTitle("小助手")
            print("初始化")
            self.dataS=""
            self.dataR=""
            self.ishtml=0
            self.record=""
            #设置文本框的只读模式

            self.text_showFile.setReadOnly(True)


            self.btn_send.setEnabled(False)



            self.thread = Worker()  # 线程实例化
            self.ser = serial.Serial()  #串口实例化


            self.setSlot()
            self.setqss()



        def setqss(self):
            from qss import QSSRead
            # QSSRead.setStyle("QSS.qss", self)
        def setSlot(self):
            print("信号槽的初始化")
            
            self.btn_searchPort.clicked.connect(self.searchPort)#查找串口号
            self.btn_start.clicked.connect(self.start)#启动线程
            self.btn_end.clicked.connect(self.end)#关闭线程

            self.btn_claerT1.clicked.connect(self.clearT1)#清除日志

            self.btn_clearS.clicked.connect(self.clearS)#清除发送区数据

            self.btn_openFile.clicked.connect(self.openFile)#打开文件
            self.btn_sendFile.clicked.connect(self.sendFile)#发送文件的内容
            self.btn_send.clicked.connect(self.send)#发送内容
            self.thread.sinOut1.connect(self.showRecord)#显示串口信息到接收区
            self.thread.sinOut2.connect(self.showHTML)#加载HTML
            self.radio_show.toggled.connect(lambda :self.setHTML(self.radio_show))#暂时保留，功能没弄


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
        def clearT1(self):
            self.text_showRecord.clear()
            self.record=""


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
                self.fileNames=dlg.selectedFiles()
                self.text_showFile.setPlainText(self.fileNames[0])

                try:
                    print(2)
                    f=open(self.fileNames[0], 'r',encoding='UTF-8')
                    print(3)
                    self.dataS=f.read()
                    print(self.dataS)
                    print(1)
                    f.close()

                    # self.text_showS.setPlainText(self.dataS)
                except:
                    QMessageBox.about(self, "错误", "出现异常")
                    print("出现异常")
                    f.close()
                # with open(r"E:\pycharm\untitled\201902\24\RevisePort\12.jpg","wb") as f:
                #     f.write(self.dataS)

            # fname, _=QFileDialog.getOpenFileName(self,"","C:\\","Image files(*.jpg *.gif)")
            # print("fname:",fname)
        #发送文件
        def  sendFile(self):
            # self.dataS=self.text_showS.toPlainText()
            # print("长度：",len(self.dataS))
            # self.dataS=b"</html>"
            if len(self.dataS)>0:
                # print(type(self.dataS))
                # print(self.dataS)
                self.record+="正在发送中\n"
                
                self.text_showRecord.setPlainText(self.record)
                print("正在发送中")
                # self.size=self.ser.write(self.dataS)
                str=self.dataS.encode('UTF-8') #发送文本文件
                print("文本长度", len(self.dataS))
                print("发送长度",len(str))
                self.size = self.ser.write(str)

                self.record+="发送完成，发送的大小{}:\n".format(len(str))
                self.text_showRecord.setPlainText(self.record)
                print("Size:",self.size)
            else:
                QMessageBox.about(self, "错误", "发送内容为空")
        # 接收区显示串口信息

        def send(self):
            self.dataS=self.text_showS.toPlainText()
            if len(self.dataS)>0:
                # print(type(self.dataS))
                # print(self.dataS)
                print("正在发送中")
                # self.size=self.ser.write(self.dataS)
                strs=self.dataS.encode('UTF-8')
                print("文本长度", len(self.dataS))
                print("发送长度",len(strs))
                self.size = self.ser.write(strs)
                print("Size:",self.size)

        def showRecord(self,sh):
            # self.text_showR.clear()

            self.record+=sh
            # if sh.
            self.text_showRecord.setPlainText(self.record)

        def setHTML(self,btn):
            if btn.isChecked()==True:
                print("ON")
            else:
                print("OFF")
            
        def showHTML(self):
            try:
                if self.ishtml==0:
                    self.brower = QWebEngineView()
                    self.vbox = QVBoxLayout(self.tab_2)
                    self.vbox.addWidget(self.brower)

                    self.ishtml=1
                else:
                    self.brower.destroy()


                self.record+="正在加载HTML文件，请等候......\n"

                self.text_showRecord.setPlainText(self.record)
                # self.brower.setHtml(html)
                file = r"D:/HTML/test.html"
                self.brower.load(QUrl(file))

                self.record += "加载HTML文件完成\n"
                self.text_showRecord.setPlainText(self.record)
            except Exception as e:
                print('Error:', e)
                self.record += "加载失败\n"
                self.text_showRecord.setPlainText(self.record)

class Worker(QThread):
    sinOut1 = pyqtSignal(str)
    sinOut2 = pyqtSignal()
    def __init__(self, parent=None):
        super(Worker, self).__init__(parent)
        self.working = True

    def __del__(self):
        # 线程状态改变与线程终止
        self.working = False
        self.wait()

    def run(self):

        print("线程启动")
        Port=main.com_showPort.currentText()
        Rate=main.com_showRate.currentText()
        print(111111111111111111111111111111111)

        
        file=r"D:\HTML\test.html"

        if Port.find("COM")!=-1:
            print(2)
            main.ser.setPort(Port)
            main.ser.baudrate=Rate
            main.ser.timeout=2

            main.ser.open()
            line = b""
            lines = b""

            try:
                while self.working == True:
                    self.record="无新的消息，等待中......\n"
                    self.sinOut1.emit(self.record)
                    # main.text_showRecord.setPlainText("开始接收，请等待")
                    # main.text_showRecord.setPlainText(main.record)
                    print("线程运行")
                    lenterm = len("</html>")

                    # by=main.ser.read_until("\n")
                    # print(by)
                    print("disanbu")
                    flag=0
                    while True:

                       text= main.ser.read(100000)

                       # print( text)
                       time.sleep(0.1)

                       if text:
                           if flag == 0:
                               self.record = "正在接收中.......\n"
                               self.sinOut1.emit(self.record)
                               flag = 1
                           line=line+text

                           # print(line[-lenterm:])
                           print(len(line))
                           if line[-lenterm:] == b'</html>':
                               lines = lines + line
                               
                                
                               print("接收结束")
                               break


                           if len(line) >=100000:
                               lines=lines+line
                               line=b""
                            #    print(line)
                               print(len(lines))
                           else:
                               lines = lines + line
                               print("结束")
                               print(len(lines))
                               break


                               # with open(file, "a+") as f:
                               #     print(" start write 1")
                               #     # f.write(c)
                               #     f.write(lines.decode("UTF-8"))
                               #     print(" start write 2")
                               #     print(" start write 2")
                               #     print(" start write 2")
                               #     line = b""
                               #     print(" start write 3")
                               #     print("写入文件正常")

                    # print("nums1 HTML",line)
                    # print(str(line,"UTF-8"))



                    with open(file, "w",encoding="UTF-8") as f:
                        html=str(lines, "UTF-8")
                        f.write(html)
                        print("写入文件完成")
                        self.record="接收完毕，接收了  ：{}\n".format(len(lines))
                        self.sinOut1.emit(self. record)
                        self.sinOut2.emit()
                        flag=0
                        lines=b""
                        line=b""




                main.ser.close()
            except Exception as e:
                print('Error:', e)

                print("串口读取数据失败")
                QMessageBox.about(main, "错误", "串口读取数据失败")
        else:
            QMessageBox.about(main, "错误", "请检查是否配置参数")



if __name__=="__main__":
    app=QApplication (sys.argv)
    main=Main()
    main.show()
    sys.exit(app.exec_())
