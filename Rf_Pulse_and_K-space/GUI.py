# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1013, 677)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 2, 2, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.label_2.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.horizontalLayout_2.addWidget(self.line_7)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.Combo1 = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.Combo1.setFont(font)
        self.Combo1.setObjectName("Combo1")
        self.Combo1.addItem("")
        self.Combo1.addItem("")
        self.Combo1.addItem("")
        self.Combo1.addItem("")
        self.Combo1.addItem("")
        self.horizontalLayout_2.addWidget(self.Combo1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.line_11 = QtWidgets.QFrame(self.centralwidget)
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.verticalLayout.addWidget(self.line_11)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.InputImage1 = ImageView(self.centralwidget)
        self.InputImage1.setObjectName("InputImage1")
        self.horizontalLayout.addWidget(self.InputImage1)
        self.FourierInput1 = ImageView(self.centralwidget)
        self.FourierInput1.setObjectName("FourierInput1")
        self.horizontalLayout.addWidget(self.FourierInput1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_4.addWidget(self.comboBox)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_4.addWidget(self.pushButton)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.withx = PlotWidget(self.centralwidget)
        self.withx.setObjectName("withx")
        self.horizontalLayout_3.addWidget(self.withx)
        self.withz = PlotWidget(self.centralwidget)
        self.withz.setObjectName("withz")
        self.horizontalLayout_3.addWidget(self.withz)
        self.withy = PlotWidget(self.centralwidget)
        self.withy.setObjectName("withy")
        self.horizontalLayout_3.addWidget(self.withy)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.line_10 = QtWidgets.QFrame(self.centralwidget)
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.verticalLayout.addWidget(self.line_10)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout.addWidget(self.line_5, 3, 1, 1, 1)
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout.addWidget(self.line_4, 1, 1, 1, 1)
        self.line_14 = QtWidgets.QFrame(self.centralwidget)
        self.line_14.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_14.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_14.setObjectName("line_14")
        self.gridLayout.addWidget(self.line_14, 0, 2, 1, 1)
        self.line_13 = QtWidgets.QFrame(self.centralwidget)
        self.line_13.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_13.setObjectName("line_13")
        self.gridLayout.addWidget(self.line_13, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1013, 21))
        self.menubar.setObjectName("menubar")
        self.menuOpen_Image = QtWidgets.QMenu(self.menubar)
        self.menuOpen_Image.setObjectName("menuOpen_Image")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_Image = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../.designer/DSP/Task 1 DSP/task1-team_18/open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen_Image.setIcon(icon)
        self.actionOpen_Image.setObjectName("actionOpen_Image")
        self.actionOpen_Image_2 = QtWidgets.QAction(MainWindow)
        self.actionOpen_Image_2.setObjectName("actionOpen_Image_2")
        self.menuOpen_Image.addAction(self.actionOpen_Image)
        self.menubar.addAction(self.menuOpen_Image.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Image 1"))
        self.Combo1.setItemText(0, _translate("MainWindow", "Select an Option"))
        self.Combo1.setItemText(1, _translate("MainWindow", "FT Magnitude"))
        self.Combo1.setItemText(2, _translate("MainWindow", "FT Phase"))
        self.Combo1.setItemText(3, _translate("MainWindow", "FT Real Component"))
        self.Combo1.setItemText(4, _translate("MainWindow", "FT Imaginary Component"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Gradient Effect"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Slice Selection"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Phase Encoding"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Frequency Encoding"))
        self.pushButton.setText(_translate("MainWindow", "Show Non-Uniformity in Z"))
        self.menuOpen_Image.setTitle(_translate("MainWindow", "File"))
        self.actionOpen_Image.setText(_translate("MainWindow", "Open Image "))
        self.actionOpen_Image_2.setText(_translate("MainWindow", "Open Image 2"))

from pyqtgraph import ImageView, PlotWidget
