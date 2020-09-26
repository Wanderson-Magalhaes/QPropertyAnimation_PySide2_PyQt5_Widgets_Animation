# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainkEXhbn.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.progressBar = QProgressBar(self.frame)
        self.progressBar.setObjectName(u"progressBar")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setStyleSheet(u"QProgressBar {	\n"
"	background-color: rgb(68, 76, 86);\n"
"	color: #FFF;\n"
"	border-style: none;\n"
"	border-radius: 10px;\n"
"	text-align: center;\n"
"}\n"
"QProgressBar::chunk{	\n"
"	background-color: rgb(255, 0, 127);\n"
"	margin: 10px;\n"
"	border-radius: 10px;\n"
"}")
        self.progressBar.setValue(24)

        self.gridLayout.addWidget(self.progressBar, 0, 0, 1, 2)

        self.btnExpand = QPushButton(self.frame)
        self.btnExpand.setObjectName(u"btnExpand")
        self.btnExpand.setMinimumSize(QSize(0, 40))
        self.btnExpand.setStyleSheet(u"QPushButton{	\n"
"	background-color: rgb(85, 170, 255);	\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"	color: #FFF\n"
"}")

        self.gridLayout.addWidget(self.btnExpand, 1, 0, 1, 1)

        self.btnRetract = QPushButton(self.frame)
        self.btnRetract.setObjectName(u"btnRetract")
        self.btnRetract.setMinimumSize(QSize(0, 40))
        self.btnRetract.setStyleSheet(u"QPushButton{	\n"
"	background-color: rgb(85, 170, 255);	\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"	color: #FFF\n"
"}")

        self.gridLayout.addWidget(self.btnRetract, 1, 1, 1, 1)

        self.btnResizeWindow = QPushButton(self.frame)
        self.btnResizeWindow.setObjectName(u"btnResizeWindow")
        self.btnResizeWindow.setMinimumSize(QSize(0, 40))
        self.btnResizeWindow.setStyleSheet(u"QPushButton{	\n"
"	background-color: rgb(85, 170, 255);	\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"	color: #FFF\n"
"}")

        self.gridLayout.addWidget(self.btnResizeWindow, 2, 0, 1, 2)


        self.verticalLayout_2.addLayout(self.gridLayout)


        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btnExpand.setText(QCoreApplication.translate("MainWindow", u"Expand", None))
        self.btnRetract.setText(QCoreApplication.translate("MainWindow", u"Retract", None))
        self.btnResizeWindow.setText(QCoreApplication.translate("MainWindow", u"Resize Window", None))
    # retranslateUi

