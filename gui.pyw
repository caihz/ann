
import sys
from PyQt4 import QtGui,QtCore
import file_tools

class myLabel(QtGui.QLabel):
    _signal=QtCore.pyqtSignal(QtCore.QString)
    path = None
    def __init__(self,parent = None):
        super(myLabel,self).__init__(parent)

    def dragEnterEvent(self, e):

    	print 'drag enter'

        if e.mimeData().hasUrls():
            e.accept()
            print 'has url'
        else:
            e.ignore()

    def dropEvent(self, e):
    	print 'drop event'
        self.path = e.mimeData().urls()[0].toLocalFile()
        print self.path
        self.setPixmap(QtGui.QPixmap(self.path))
       	self._signal.emit(self.path)

class myLcd(QtGui.QLCDNumber):
    def __init__(self, parent = None):
        super(myLcd, self).__init__(parent)

    def display(self,path):
    	num = file_tools.get_num(str(path))
    	super(myLcd, self).display(num)

		

class MyWindow(QtGui.QWidget):
    def __init__(self,parent = None):
        super(MyWindow,self).__init__(parent)
        self.resize(400,800)
        self.mainlayout = QtGui.QVBoxLayout(self)
        self.label= myLabel(self)
        self.lcd = myLcd(self)
        self.label.setAcceptDrops(True)
        self.label.setGeometry(0,0,200,200)
        self.label.setScaledContents(True) 
        self.mainlayout.addWidget(self.label)
        self.mainlayout.addWidget(self.lcd)
        self.label.setPixmap(QtGui.QPixmap("0.png"))
        self.label._signal.connect(self.lcd.display)        
if __name__ == '__main__':
	app=QtGui.QApplication(sys.argv)
	window=MyWindow()
	window.show()
	app.exec_()