import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from decimal import Decimal

class Medal410321170(QWidget): # XXXXXXXXX is your student ID (be sure to follow this naming for this class)
	def __init__(self, parent=None):
		super().__init__(parent=parent)
		self.testinit()
		
	def testinit(self):
		self.setGeometry(300, 300, 450, 575) # specify the sindow size
		self.setWindowTitle('test?')
		self.show()	
	
	def paintEvent(self, e):
		test = QPainter()
		test.begin(self)
		self.drawRectangles(test,e)
		test.end()
	
	def drawRectangles(self,test,e):
		
		test = QPainter()
		c1 = QColor(100,0,0)
		c2 = QColor(100,0,0)
		test.setPen(c1)
		test.setBrush(c2)
		test.drawRect(0,0,180,200)
		### Design your own widget here. 
		### Don't use Chinese characters in the class design. 
		### The size of the medal cannot be larger than 180(w)x200(h) pixels.
		### Do not write more than 35 lines of statements. 
		### You don't need to write any code to construct the medal object by yourself. The saint will do it for you.

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Medal410321170()
    sys.exit(app.exec_())