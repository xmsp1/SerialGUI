进行串口通信的GUI测试，传输文件。
pyuic5 -o CreatePort.py CreatePort.ui

mqttClient.username_pw_set("sammy","password")


# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import *
from CreatePort import Ui_Form
from PyQt5.QtGui import *
from PyQt5.QtCore import *
class Main(QWidget,Ui_Form):
        def __init__(self, parent=None):
            super(Main,self).__init__(parent)
            self.setupUi(self)

            self.setWindowTitle("")
if __name__=="__main__":
    app=QApplication (sys.argv)
    main=Main()
    main.show()
    sys.exit(app.exec_())

with open("E:/pycharm/untitled/201902/2.24/RevisePort/ReadMe.txt",'r',encoding='UTF-8')as f:
    content=f.read()
print(content)


pyinstaller -F -w main.py Ui.py