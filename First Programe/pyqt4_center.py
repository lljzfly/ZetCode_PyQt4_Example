#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
from PyQt4 import QtGui

class Example(QtGui.QWidget):
	def __init__(self):
		super(Example,self).__init__()
		self.initUI()

	def initUI(self):
		self.resize(250,150)
		self.center()
		self.setWindowTitle('Center')

	def center(self):
		qr=self.frameGeometry()
		cp=QtGui.QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())
		

def main():
	app=QtGui.QApplication(sys.argv)
	ex=Example()
	ex.show()
	sys.exit(app.exec_())

if __name__=='__main__':
	main()