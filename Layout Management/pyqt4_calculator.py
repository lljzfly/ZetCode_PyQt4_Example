#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
from PyQt4 import QtGui

class Example(QtGui.QWidget):
	"""docstring for Example"""
	def __init__(self):
		super(Example, self).__init__()
		self.initUI()

	def initUI(self):
		grid=QtGui.QGridLayout()
		self.setLayout(grid)

		names=['Cls','Bck','','Close',
				'7','8','9','/',
				'4','5','6','*',
				'1','2','3','-',
				'0','.','=','+']

		positions=[(i,j) for i in range(5) for j in range(4)]

		for position,name in zip(positions, names):
			if name == '':
				continue

			button=QtGui.QPushButton(name,self)
			grid.addWidget(button,*position)

		self.move(300,150)
		self.setWindowTitle('Calculator')

def main():
	app=QtGui.QApplication(sys.argv)
	ex=Example()
	ex.show()
	sys.exit(app.exec_())

if __name__=='__main__':
	main()
		