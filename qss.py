class QSSRead(object):
    @staticmethod
    def setStyle(path,obj):
        with open(path,'r')as f:
            content=f.read()
            obj.setStyleSheet(content)

# print(content)