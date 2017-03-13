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
from PyQt5.QtCore import (QObject, QSettings, QUrl, Qt, QRegExp, pyqtSlot, pyqtProperty, QCoreApplication)
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (QHBoxLayout, QVBoxLayout, QMainWindow, QLineEdit, QWidget, QLCDNumber, \
							 QSlider, QVBoxLayout, QApplication, QAction, QLabel, QPushButton, QMenuBar, \
							 QTextEdit)

from PyQt5.QtQml import (QQmlEngine, QQmlContext, QQmlApplicationEngine, QJSValue, qmlRegisterType, \
	QQmlComponent, QQmlError)
from PyQt5.QtQuick import (QQuickView, QQuickItem)
from PyQt5.QtQuickWidgets import (QQuickWidget)
from PyQt5.QtGui import (QIcon, QGuiApplication)

settingsName = "mainWindow/state"


class JiraMain(QMainWindow):
	def __init__(self, parent):
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
		
	# @pyqtProperty('QMenuBar')
	# def menuBar(self):
		# return self.menuBar
		
	# @menuBar.setter 
	# def menuBar(self, mBar):
		# browse(mBar)
		# self.setMenuBar(mBar)
		
	# @pyqtSlot('QJSValue')
	# def setMenu(self, menuBar):
		# print("set menu")
		# browse(menuBar)
		# self.setMenuBar(menuBar)
		
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
	qmlRegisterType(JiraMain, 'JiraTree', 1, 0, 'MainWindow')

	engine = QQmlEngine()
	# Create a component factory and load the QML script.
	component = QQmlComponent(engine)
	component.loadUrl(QUrl.fromLocalFile('main.qml'))
	jm = component.create()
	[ print(e.toString()) for e in component.errors() ]
	engine.rootContext().setContextProperty("mainWindow", jm)
	if jm is None:
		print( "JM is none")
		print( { e.toString() for e in component.errors()})
	
#	ex = JiraMain(None)
	print("Run")
	app.exec()
	print("Exit")
	sys.exit()
