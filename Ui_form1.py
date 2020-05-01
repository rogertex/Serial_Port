# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\VS\Serial_Port\form1.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        self.menu_4 = QtWidgets.QMenu(self.menubar)
        self.menu_4.setObjectName("menu_4")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.action_start = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("d:\\VS\\Serial_Port\\ICON/start.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_start.setIcon(icon)
        self.action_start.setObjectName("action_start")
        self.action_zt = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("d:\\VS\\Serial_Port\\ICON/zt.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_zt.setIcon(icon1)
        self.action_zt.setObjectName("action_zt")
        self.action_stop = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("d:\\VS\\Serial_Port\\ICON/stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_stop.setIcon(icon2)
        self.action_stop.setObjectName("action_stop")
        self.menu.addAction(self.action_start)
        self.menu.addAction(self.action_zt)
        self.menu.addAction(self.action_stop)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())
        self.toolBar.addAction(self.action_start)
        self.toolBar.addAction(self.action_zt)
        self.toolBar.addAction(self.action_stop)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menu.setTitle(_translate("MainWindow", "编辑"))
        self.menu_2.setTitle(_translate("MainWindow", "显示"))
        self.menu_3.setTitle(_translate("MainWindow", "工具"))
        self.menu_4.setTitle(_translate("MainWindow", "帮助"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.action_start.setText(_translate("MainWindow", "开始"))
        self.action_zt.setText(_translate("MainWindow", "暂停"))
        self.action_stop.setText(_translate("MainWindow", "停止"))
