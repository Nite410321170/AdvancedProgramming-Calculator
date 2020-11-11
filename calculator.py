import sys
from PyQt5.QtWidgets import (QApplication, QLabel, QWidget, QHBoxLayout, QVBoxLayout, QGridLayout, QLCDNumber,QPushButton, QAction, QMenu)
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QPainter, QColor, QPen, QIcon, QKeyEvent, QPixmap
import PyQt5.QtCore as pie
from decimal import Decimal

class Calculator(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()    
	
	def initUI(self): # open a window    
		grid = QGridLayout()
		self.setLayout(grid)
		
		self.setGeometry(300, 300, 450, 575) # specify the sindow size
		self.setMinimumSize(450,575)
		self.setWindowTitle('TuWorld Calculator') # specify the window title
		self.setWindowIcon(QIcon('nite.png')) # specify the window icon    
		self.input_str = []
		self.equation = []
		self.input = ''.join(self.input_str)
		self.output = '0'
		self.images =["toolong.jpg", "good.jpg", "matherror.jpg", "syntaxerror.png"]
		self.status = 1
		
		self.label = QLabel(self)
		#self.label.resize(400, 40)
		self.label.setAlignment(pie.Qt.AlignRight | pie.Qt.AlignVCenter)
		#self.output = str(grid.columnCount())
		self.label.setText(self.input)
		grid.addWidget(self.label,0,0,1,0)
		
		self.lcd = QLCDNumber()
		#self.input = str(grid.rowCount())
		self.lcd.setDigitCount(20)
		#self.lcd.resize(300,75)
		self.lcd.display(self.output)
		grid.addWidget(self.lcd,1,0,1,0)
		self.setLayout(grid)
		
		cal_button = [['', 'Clear', '<-', 'Close'],
                 ['7', '8', '9', '÷'],
                 ['4', '5', '6', '×'],
                 ['1', '2', '3', '-'],
                 ['=', '0', '.', '+']]
		
		self.pic_label = QLabel(self)
		pixmap = QPixmap(self.images[self.status])
		pixmapScaled = pixmap.scaled(110, 75)
		self.pic_label.setPixmap(pixmapScaled)
		for xposition in range(2,7):
			for yposition in range(4):
				if cal_button[xposition-2][yposition] == '':
					self.pic_label.setMinimumSize(110,75)
					grid.addWidget(self.pic_label,xposition*2, yposition)
				else:
					button = QPushButton(cal_button[xposition-2][yposition])
					button.setMinimumSize(110,75)
					grid.addWidget(button, xposition*2, yposition)
					button.clicked.connect(self.Cli)
		
		
		self.setLayout(grid)
		self.show()
		
	def updater(self, input, output):
		self.input = input
		
		self.label.setText(self.input)
		self.lcd.display(self.output)
		
		if(len(self.output) > 20):
			self.status = 0
		pixmap = QPixmap(self.images[self.status])
		pixmapScaled = pixmap.scaled(110, 75)
		self.pic_label.setPixmap(pixmapScaled)
		self.update()
		
	#Clicking events
	def Cli(self):
		
		sender = self.sender().text()
		
		if sender == 'Clear':
			self.input_str.clear()
			self.equation.clear()
			self.output = '0'
			self.status = 1
		elif sender == '=' and len(self.input_str)>0:
			e = expression()
			while (self.input_str[0]=='0' and len(self.input_str)>1):
				self.input_str.pop(0)
				self.equation.pop(0)
			self.input = ''.join(self.input_str)
			v, rc = e.interpret(''.join(self.equation))
			if v and len(rc)==0:
				try:
					temp = eval(''.join(self.equation))
					self.output = str(temp)
					self.status = 1
				except ZeroDivisionError:
					self.output = 'ErrOr'
					self.status = 2
			elif len(rc) > 0 or v==False:
				self.output = 'ErrOr'
				self.status = 3
		elif sender == '<-':
			if len(self.input)>0:
				temp = len(self.input_str)
				self.input_str.pop(temp-1)
				self.equation.pop(temp-1)
		elif sender == 'Close':
			self.close()
		elif sender!='Close':
			self.input_str.append(sender)
			if(sender=="÷"):
				self.equation.append('/')
			elif(sender=='×'):
				self.equation.append('*')
			else:
				self.equation.append(sender)
		self.updater(''.join(self.input_str), self.output)
		
		
	#Extra functonality for keyboard events	
	def keyPressEvent(self, event):
		if type(event) == QKeyEvent:
			temp = ['.','1', '2','3','4','5','6','7','8','9','0','-','+','/','*','x','X']
			if event.text() in temp:
				if event.text()=='/':
					self.input_str.append('÷')
					self.equation.append(event.text())
				elif event.text()=='*' or event.text()=='x' or event.text()=='X':
					self.input_str.append('×')
					self.equation.append('*')
				else:
					self.input_str.append(event.text())
					self.equation.append(event.text())
			elif (event.key() == pie.Qt.Key_Enter or event.key() == pie.Qt.Key_Return) and len(self.input_str)>0:
				e = expression()
				while (self.input_str[0]=='0' and len(self.input_str)>1):
					self.input_str.pop(0)
					self.equation.pop(0)
				self.input = ''.join(self.input_str)
				v, rc = e.interpret(''.join(self.equation))
				if v and len(rc)==0:
					try:
						self.output = str(eval(''.join(self.equation)))
						self.status = 1
					except ZeroDivisionError:
						self.output = 'ErrOr'
						self.status = 2
				elif len(rc) > 0 or not v:
					self.output = 'ErrOr'
					self.status = 3
			elif event.key() == pie.Qt.Key_Backspace:
				if len(self.input)>0:
					temp = len(self.input_str)
					self.input_str.pop(temp-1)
					self.equation.pop(temp-1)
		self.updater("".join(self.input_str), self.output)


######
## Syntax and Expression checker
######
# Copied and pasted from previous work (assignment2)

class non_terminal:
	def __init__(self):
		self.elems=list()
		self.name=""
		self.val=0
		self.visitor=None
	def interpret():
		pass	
	def set_visitor(self,visitor):
		self.visitor=visitor
	def visit(self):
		self.visitor.visit(self)
		
class visitor:
	def visit():
		pass
		
class structure_visitor(visitor):
	def visit(self,test):
		print("Structure:")
		for x in range(len(test.nonterminal.elems)):
			print("\t\t",test.nonterminal.elems[x][0],":",test.nonterminal.elems[x][1])
		print("\t"+test.nonterminal.name,":",test.nonterminal.val)

class value_visitor(visitor):
	def visit(self,test):
		print("Value:")
		print("\t"+test.nonterminal.name,":",test.nonterminal.val)
		
		
#################
## Sub-classes ##
#################
class minus(non_terminal):
	def __init__(self):
		nonterminal = non_terminal()
	def interpret(self, context):
		self.nonterminal.name = "minus"
		rem_context = list(context)
		if(rem_context[0] == "-"):
			rem_context.pop(0)
			self.nonterminal.val = -1
			return True, "".join(rem_context)
		return False, "".join(rem_context)
		
class digit(non_terminal):
	def __init__(self):
		self.nonterminal = non_terminal()
	def interpret(self, context):
		self.nonterminal.name = "digit"
		rem_context = list(context)
		if(rem_context[0].isdigit()):
			self.nonterminal.val = rem_context.pop(0)
			return True, "".join(rem_context)
		return False, "".join(rem_context)

class decpoint(non_terminal):
	def __init__(self):
		self.nonterminal = non_terminal()
		self.op=""
	def interpret(self, context):
		self.nonterminal.name = "decpoint"
		rem_context = list(context)
		if(rem_context[0] == "."):
			self.op = rem_context.pop(0)
			return True, "".join(rem_context)
		return False, "".join(rem_context)

class number(non_terminal):
	def __init__(self):
		self.nonterminal = non_terminal()
	def interpret(self, context):
		tempEle = list() #Creates a unique list only for this function
		temp = context[0]
		test1, rem_context = digit.interpret(self, context)
		#print(temp,"is digit: ",test1) 
		if(test1):
			tempEle.append(["digit", eval(temp)])
			if(test1 and len(rem_context) > 0):
				temp = rem_context[0]
				test2, rem_context = digit.interpret(self,rem_context)
				#print(temp,"is digit: ",test2)
				if(test2):
					tempEle.append(["digit", eval(temp)])
				
				while(test2 and len(rem_context) > 0):	
					temp = rem_context[0]
					test2, rem_context = digit.interpret(self,rem_context)
					#print(temp,"is digit: ",test2)
					if(test2):
						tempEle.append(["digit", eval(temp)])
				
				if(len(rem_context)>0):
					temp = rem_context[0]
					test2, rem_context = decpoint.interpret(self,rem_context)
					#print(temp,"is decimal point: ",test2)
					if(test2):
						tempEle.append(["decpoint", temp])
					while(test2 and len(rem_context) > 0):
						temp = rem_context[0]
						test2, rem_context = digit.interpret(self,rem_context)
						#print(temp,"is digit: ",test2)
						if(test2):
							tempEle.append(["digit", eval(temp)])
			self.nonterminal.name = "number"
			self.nonterminal.elems = tempEle[:]
			if(test1):
				self.nonterminal.val = eval(context.replace(rem_context,""))
				return True, rem_context
		return False, rem_context

class operator1(non_terminal):
	def __init__(self):
		self.nonterminal = non_terminal()
		self.op=""
	def interpret(self, context):
		self.nonterminal.name = "op1"
		rem_context = list(context)
		if(rem_context[0] == "+" or rem_context[0] == "-"):
			self.op=rem_context.pop(0)
			return True, "".join(rem_context)
		return False, "".join(rem_context)
		
class operator2(non_terminal):
	def __init__(self):
		self.nonterminal = non_terminal()
		self.op=""
	def interpret(self, context):
		self.nonterminal.name = "op2"
		rem_context = list(context)
		if(rem_context[0] == "*" or rem_context[0] == "/"):
			self.op = rem_context.pop(0)
			return True, "".join(rem_context)
		return False, "".join(rem_context)
		
class term(non_terminal):
	def __init__(self):
		self.nonterminal = non_terminal()
	def interpret(self, context):
		tempEle = list()
		test1, rem_context = number.interpret(self, context)
		#print(context.replace(rem_context,""),"is a number: ",test1)
		#Adds a 2 element list to the non terminal list. Format is [str(name), value]. 
		if(test1):
			#eval() function computes strings that are in the form of equations into numeric values
			tempEle.append(["number", 0]) #removed evaluation line
			temp = rem_context
			test2 = True
			while(test2 and len(rem_context) > 0):
				op2 = rem_context
				temp = rem_context
				test2 = False
				test2, rem_context = operator2.interpret(self, rem_context)
				#print(op2.replace(rem_context,""),"is an op2: ",test2)
				if(test2):
					tempEle.append(["op2", op2.replace(rem_context,"")])
					if(len(rem_context)>0):
						test2 = False
						num2 = rem_context
						test2, rem_context = number.interpret(self, rem_context)
						#print(num2.replace(rem_context,""),"is a number: ",test2)
						if(test2):
							tempEle.append(["number", 0]) #removed evaluation line
					else:
						return True, temp
			self.nonterminal.name = "term"
			self.nonterminal.elems = tempEle[:]
			if(test2):
				self.nonterminal.val = 0 #removed evaluation line
				return True, rem_context
			if(test1):
				self.nonterminal.val = 0 #removed evaluation line
				return True, temp
		return False, rem_context

class expression(non_terminal):
	def __init__(self):
		self.nonterminal = non_terminal()
	def interpret(self, context):
		tempEle = list()
		test2, rem_context = minus.interpret(self, context)
		#print("A minus exists: ",test2)
		if(test2):
			tempEle.append(["minus", -1])
			
		term1 = rem_context 
		test1, rem_context = term.interpret(self, rem_context)
		#print(term1.replace(rem_context,""),"is a term: ", test1)
		if(test1):
			tempEle.append(["term", 0]) #removed evaluation line
		temp = rem_context
		if(test1 and len(rem_context)>0):
			test2 = True
			while(test2 and len(rem_context)>0):
				temp = rem_context
				test2 = False
				op1 = rem_context
				test2, rem_context = operator1.interpret(self, rem_context)
				#print(op1.replace(rem_context,""),"is an op1: ", test2)
				if(test2):
					tempEle.append(["op1", op1.replace(rem_context,"")])
				if(test2 and len(rem_context)>0):
					test2 = False
					term1 = rem_context
					test2, rem_context = term.interpret(self,rem_context)
					#print(term1.replace(rem_context,""),"is a term: ", test2)
					if(test2):
						tempEle.append(["term", 0]) #removed evaluation line
		self.nonterminal.name = "expression"
		self.nonterminal.elems = tempEle[:]
		if(test2):
			self.nonterminal.val = 0 #removed evaluation line
			return True, rem_context
		if(test1):
			self.nonterminal.val = 0 #removed evaluation line
			return True, temp
		return False, rem_context

		
#########
## Main Program
#########
if __name__ == '__main__':
	app = QApplication(sys.argv) # construct an application
	ex = Calculator() # create a window
	sys.exit(app.exec_()) # enters the main loop to catch events and exits until closing window
