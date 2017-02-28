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
from PyQt5 import (QtQml)
from PyQt5.QtCore import (QSettings, QUrl, Qt, QRegExp)
from PyQt5.QtWidgets import (QHBoxLayout, QVBoxLayout, QMainWindow, QLineEdit, QWidget, QLCDNumber, \
	QSlider, QVBoxLayout, QApplication, QAction, QLabel,QPushButton)

from PyQt5.QtQml import (QQmlEngine, QQmlContext)
from PyQt5.QtQuick import (QQuickView)
from PyQt5.QtQuickWidgets import (QQuickWidget)
from PyQt5.QtGui import QIcon

settingsName = "mainWindow/state"

class JiraMain(QMainWindow):
	
	def __init__(self):
		super().__init__()
		self.settings = QSettings("Harman", "JiraTree");
		self.mainWindowState = self.settings.value(settingsName)
		self.initUI()

	def onClose(self):
		state = self.saveGeometry()
		self.settings.setValue(settingsName, state)
		self.close()
		
	def loadMainView(self):
		view = QQuickWidget();
		view.setSource(QUrl.fromLocalFile("main.qml"));
#		view->show();
		self.setCentralWidget(view)
		return view

	def goHandler(self):
		print("GO!")

	def createContext(self):
		rootContext = QtQml.QQmlEngine().rootContext()
		pprint.pprint(rootContext.contextObject())
		self.qmlContext = QQmlContext(rootContext)
		pprint.pprint(self.qmlContext.isValid())
		self.qmlContext.setContextProperty("mainObject", self)
		
	def initUI(self):				
		
		self.statusBar()
		
		exitAction = QAction(QIcon('img/exit.png'), 'Exit', self)
		exitAction.setShortcut('Ctrl+Q')
		exitAction.setStatusTip('Exit application')
		exitAction.triggered.connect(self.onClose)

		processUrlAction = QAction(QIcon('img/go.svg'), 'Go', self)
		processUrlAction.setShortcut('Ctrl+G')
		processUrlAction.setStatusTip('Analyzes issue')
		processUrlAction.triggered.connect(self.goHandler)

		menubar = self.menuBar()
		fileMenu = menubar.addMenu('&File')
		fileMenu.addAction(processUrlAction)
		fileMenu.addSeparator()
		fileMenu.addAction(exitAction)

		toolbar = self.addToolBar('Exit')
		toolbar.setObjectName('ToolBar')
		toolbar.addAction(exitAction)
		toolbar.addAction(processUrlAction)

		mView = self.loadMainView()
		self.createContext()
		
		self.setWindowTitle('Main window')
		if self.mainWindowState != None and self.mainWindowState.size() > 0:
			self.restoreGeometry(self.mainWindowState)
		else:
			self.setGeometry(300, 300, 800, 600)
		self.show()
		
		
if __name__ == '__main__':
	
	app = QApplication(sys.argv)
	ex = JiraMain()
	sys.exit(app.exec_())