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
from objbrowser import browse
from PyQt5 import (QtCore, QtQml)
from PyQt5.QtCore import (QObject, QSettings, QUrl, Qt, QRegExp, pyqtSlot)
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (QHBoxLayout, QVBoxLayout, QMainWindow, QLineEdit, QWidget, QLCDNumber, \
							 QSlider, QVBoxLayout, QApplication, QAction, QLabel, QPushButton, QMenuBar)

from PyQt5.QtQml import (QQmlEngine, QQmlContext, QQmlApplicationEngine)
from PyQt5.QtQuick import (QQuickView, QQuickItem)
from PyQt5.QtQuickWidgets import (QQuickWidget)
from PyQt5.QtGui import (QIcon, QGuiApplication)

settingsName = "mainWindow/state"


class JiraMain(QMainWindow):
	def __init__(self):
		super().__init__()
		self.settings = QSettings("Harman", "JiraTree")
		self.mainWindowState = self.settings.value(settingsName)
		self.initUI()

	@pyqtSlot()
	def onClose(self):
		print("Close")
		state = self.mainWindow.saveGeometry()
		self.settings.setValue(settingsName, state)
		self.mainWindow.close()

	@pyqtSlot()
	def goHandler(self):
		print("GO!")

	@pyqtSlot()
	def onAbout(self):
		print("About")
		
	@pyqtSlot()
	def onConnect(self):
		print("Connect")
		
	@pyqtSlot(QQuickItem)
	def setMenu(self, menuBar):
		print("set menu")
		pprint.pprint(menuBar)
		self.setMenuBar(menuBar)
		
	def loadMainView(self):
		view = QQuickView()
		view.rootContext().setContextProperty("base", self)
		view.setSource(QUrl("main.qml"))
		self.mainWindow = self
		r = view.rootObject()

	def restoreState(self):
		if self.mainWindowState != None and self.mainWindowState.size() > 0:
			self.mainWindow.restoreGeometry(self.mainWindowState)
		else:
			self.mainWindow.setGeometry(300, 300, 800, 600)

	def initUI(self):

		self.loadMainView()
		self.statusBar()
		# exitAction = QAction(QIcon('img/exit.png'), 'Exit', self)
		# exitAction.setShortcut('Ctrl+Q')
		# exitAction.setStatusTip('Exit application')
		# exitAction.triggered.connect(self.onClose)

		# processUrlAction = QAction(QIcon('img/go.svg'), 'Go', self)
		# processUrlAction.setShortcut('Ctrl+G')
		# processUrlAction.setStatusTip('Analyzes issue')
		# processUrlAction.triggered.connect(self.goHandler)

		# menubar = self.menuBar() 
		# fileMenu = menubar.addMenu('&File')
		# fileMenu.addAction(processUrlAction)
		# fileMenu.addSeparator()
		# fileMenu.addAction(exitAction)

		toolbar = self.addToolBar('Exit')
		# toolbar.setObjectName('ToolBar')
		# toolbar.addAction(exitAction)
		# toolbar.addAction(processUrlAction)

		self.restoreState()
		self.show()


if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = JiraMain()
	print("Run")
	app.exec()
	print("Exit")
	sys.exit()
