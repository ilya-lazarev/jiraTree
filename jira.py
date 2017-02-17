#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial 

In this example, we create a simple
window in PyQt5.

author: Jan Bodnar
website: zetcode.com 
last edited: January 2015
"""

import sys
import pprint
from PyQt5.QtWidgets import (QHBoxLayout, QVBoxLayout, QMainWindow, QLineEdit, QWidget, QLCDNumber, \
	QSlider, QVBoxLayout, QApplication, QAction, QLabel)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSettings

settingsName = "mainWindow/state"

class JiraMain(QMainWindow):
	
	def __init__(self):
		super().__init__()
		
		self.settings = QSettings("Harman", "JiraTree");
		self.mainWindowState = self.settings.value(settingsName)
		pprint.pprint(self.mainWindowState)
		self.initUI()

	def onClose(self):
		state = self.saveGeometry()
		pprint.pprint(state)
		self.settings.setValue(settingsName, state)
		self.close()
		
	def initUI(self):				
		
		self.statusBar()
		
		exitAction = QAction(QIcon('img/exit.png'), 'Exit', self)
		exitAction.setShortcut('Ctrl+Q')
		exitAction.setStatusTip('Exit application')
		exitAction.triggered.connect(self.onClose)


		menubar = self.menuBar()
		fileMenu = menubar.addMenu('&File')
		fileMenu.addAction(exitAction)

		toolbar = self.addToolBar('Exit')
		toolbar.setObjectName('ToolBar')
		toolbar.addAction(exitAction)

		self.urlEdit = QLineEdit(self)
		hbox = QHBoxLayout()
		hbox.addWidget(QLabel('URL',self))
		hbox.addWidget(self.urlEdit)

		vbox = QVBoxLayout()
		vbox.addLayout(hbox)

#		self.setLayout(vbox)
#		self.setCentralWidget(vbox)
		self.setWindowTitle('Main window')
		if self.mainWindowState != None:
			if self.mainWindowState.size() > 0:
				print("Loaded settings: ")
				self.restoreGeometry(self.mainWindowState);
			else:
				print("Settings is 0")
		else:
			print("No settings")
			self.setGeometry(300, 300, 800, 600)
		self.show()
		
		
if __name__ == '__main__':
	
	app = QApplication(sys.argv)
	ex = JiraMain()
	sys.exit(app.exec_())