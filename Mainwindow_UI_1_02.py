

from PyQt5 import QtCore, QtGui, QtWidgets
from methods import swap_caps

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1255, 664)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/CEB.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(120, 250, 121, 20))
        self.line.setLineWidth(1)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(240, 260, 3, 61))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(110, 190, 21, 21))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(110, 100, 31, 61))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(110, 240, 21, 21))
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(230, 350, 21, 21))
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setGeometry(QtCore.QRect(350, 100, 31, 61))
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.line_9 = QtWidgets.QFrame(self.centralwidget)
        self.line_9.setGeometry(QtCore.QRect(350, 240, 21, 21))
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.line_10 = QtWidgets.QFrame(self.centralwidget)
        self.line_10.setGeometry(QtCore.QRect(350, 190, 21, 21))
        self.line_10.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(240, 250, 121, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_11 = QtWidgets.QFrame(self.centralwidget)
        self.line_11.setGeometry(QtCore.QRect(230, 400, 31, 61))
        self.line_11.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.line_12 = QtWidgets.QFrame(self.centralwidget)
        self.line_12.setGeometry(QtCore.QRect(840, 240, 21, 21))
        self.line_12.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.line_13 = QtWidgets.QFrame(self.centralwidget)
        self.line_13.setGeometry(QtCore.QRect(720, 350, 21, 21))
        self.line_13.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_13.setObjectName("line_13")
        self.line_14 = QtWidgets.QFrame(self.centralwidget)
        self.line_14.setGeometry(QtCore.QRect(600, 100, 31, 61))
        self.line_14.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_14.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_14.setObjectName("line_14")
        self.line_15 = QtWidgets.QFrame(self.centralwidget)
        self.line_15.setGeometry(QtCore.QRect(600, 240, 21, 21))
        self.line_15.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_15.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_15.setObjectName("line_15")
        self.line_16 = QtWidgets.QFrame(self.centralwidget)
        self.line_16.setGeometry(QtCore.QRect(840, 190, 21, 21))
        self.line_16.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_16.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_16.setObjectName("line_16")
        self.line_17 = QtWidgets.QFrame(self.centralwidget)
        self.line_17.setGeometry(QtCore.QRect(840, 100, 31, 61))
        self.line_17.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_17.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_17.setObjectName("line_17")
        self.line_18 = QtWidgets.QFrame(self.centralwidget)
        self.line_18.setGeometry(QtCore.QRect(610, 250, 121, 20))
        self.line_18.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_18.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_18.setObjectName("line_18")
        self.line_19 = QtWidgets.QFrame(self.centralwidget)
        self.line_19.setGeometry(QtCore.QRect(600, 190, 21, 21))
        self.line_19.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_19.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_19.setObjectName("line_19")
        self.line_20 = QtWidgets.QFrame(self.centralwidget)
        self.line_20.setGeometry(QtCore.QRect(730, 250, 121, 20))
        self.line_20.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_20.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_20.setObjectName("line_20")
        self.line_21 = QtWidgets.QFrame(self.centralwidget)
        self.line_21.setGeometry(QtCore.QRect(730, 260, 3, 61))
        self.line_21.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_21.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_21.setObjectName("line_21")
        self.line_22 = QtWidgets.QFrame(self.centralwidget)
        self.line_22.setGeometry(QtCore.QRect(720, 400, 31, 61))
        self.line_22.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_22.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_22.setObjectName("line_22")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1030, 470, 91, 26))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/tick.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1140, 470, 91, 26))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/Delete-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 160, 41, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(170, 210, 41, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(410, 160, 41, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(410, 210, 41, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(290, 320, 41, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(290, 370, 41, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(660, 160, 41, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(660, 210, 41, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(900, 210, 41, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(900, 160, 41, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(780, 370, 41, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(780, 320, 41, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(30, 160, 51, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(30, 210, 51, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(270, 210, 51, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(270, 160, 51, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(160, 370, 41, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(160, 320, 41, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(520, 210, 51, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(520, 160, 51, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(640, 380, 51, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(640, 330, 51, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(760, 210, 51, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(760, 160, 51, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(80, 80, 91, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(320, 80, 91, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(200, 460, 91, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_4 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_4.setGeometry(QtCore.QRect(570, 80, 91, 20))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_5 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_5.setGeometry(QtCore.QRect(810, 80, 91, 22))
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_6 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_6.setGeometry(QtCore.QRect(690, 460, 91, 22))
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_7 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_7.setGeometry(QtCore.QRect(1030, 430, 201, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_7.setFont(font)
        self.comboBox_7.setObjectName("comboBox_7")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setGeometry(QtCore.QRect(950, 430, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.centralwidget)
        self.label_26.setGeometry(QtCore.QRect(60, 540, 181, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.centralwidget)
        self.label_27.setGeometry(QtCore.QRect(250, 540, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.centralwidget)
        self.label_28.setGeometry(QtCore.QRect(440, 540, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(80, 160, 81, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(80, 210, 81, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(320, 160, 81, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(320, 210, 81, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(200, 320, 81, 31))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(200, 370, 81, 31))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(570, 160, 81, 31))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(570, 210, 81, 31))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_9.setGeometry(QtCore.QRect(690, 320, 81, 31))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_10.setGeometry(QtCore.QRect(690, 370, 81, 31))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_11.setGeometry(QtCore.QRect(810, 160, 81, 31))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_12.setGeometry(QtCore.QRect(810, 210, 81, 31))
        self.lineEdit_12.setObjectName("lineEdit_12")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1255, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuExport = QtWidgets.QMenu(self.menuEdit)
        self.menuExport.setObjectName("menuExport")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionPdf = QtWidgets.QAction(MainWindow)
        self.actionPdf.setObjectName("actionPdf")
        self.actionWord = QtWidgets.QAction(MainWindow)
        self.actionWord.setObjectName("actionWord")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionSave_2 = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/Floppy-Disk-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave_2.setIcon(icon3)
        self.actionSave_2.setObjectName("actionSave_2")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionOpen_2 = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/fileopen.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen_2.setIcon(icon4)
        self.actionOpen_2.setObjectName("actionOpen_2")
        self.actionDelete = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/icons8-delete-64 colored.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDelete.setIcon(icon5)
        self.actionDelete.setObjectName("actionDelete")
        self.actionExport2Word = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icons/MS-Word-2-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExport2Word.setIcon(icon6)
        self.actionExport2Word.setObjectName("actionExport2Word")
        self.actionExport2PDF = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("icons/PDF-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExport2PDF.setIcon(icon7)
        self.actionExport2PDF.setObjectName("actionExport2PDF")
        self.actionDelete_2 = QtWidgets.QAction(MainWindow)
        self.actionDelete_2.setObjectName("actionDelete_2")
        self.actionRestore_Original = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("icons/Refresh-2-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRestore_Original.setIcon(icon8)
        self.actionRestore_Original.setObjectName("actionRestore_Original")
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionExit)
        self.menuFile.addAction(self.actionAbout)
        self.menuExport.addAction(self.actionPdf)
        self.menuExport.addAction(self.actionWord)
        self.menuEdit.addAction(self.menuExport.menuAction())
        self.menuEdit.addAction(self.actionDelete_2)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.toolBar.addAction(self.actionSave_2)
        self.toolBar.addAction(self.actionOpen_2)
        self.toolBar.addAction(self.actionDelete)
        self.toolBar.addAction(self.actionExport2Word)
        self.toolBar.addAction(self.actionExport2PDF)
        self.toolBar.addAction(self.actionRestore_Original)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        #-----------------------------------------------------------------
        self.GENERATE_COUNTER = 0
        self.ORIGINAL_INPUT = {}
        self.pushButton.clicked.connect(self.calculate_best_swap)
        self.actionRestore_Original.triggered.connect(self.reset_to_origial)
        #-----------------------------------------------------------------
        
        
    def get_inputData(self):
        original_data_dict = {'A':[self.lineEdit.text() , self.lineEdit_2.text()] , 'B':[self.lineEdit_3.text() , self.lineEdit_4.text()],
        'C':[self.lineEdit_5.text() , self.lineEdit_6.text()],
        'a':[self.lineEdit_7.text() , self.lineEdit_8.text()] , 'b':[self.lineEdit_11.text() , self.lineEdit_12.text()],
        'c':[self.lineEdit_9.text() , self.lineEdit_10.text()]}

        #print(original_data_dict)
        FIRST_Y = [self.comboBox.currentText() , self.comboBox_2.currentText(), self.comboBox_3.currentText()]
        second_Y = [self.comboBox_4.currentText() , self.comboBox_5.currentText(), self.comboBox_6.currentText()]
        arranged_dict = {'R':[] , 'Y':[], 'B':[]}
        arranged_dict_2 = {'R':[] , 'Y':[], 'B':[]}
        
        #___________________________________________________________________
        if FIRST_Y[0] == "First Rack":
            arranged_dict['R'] = original_data_dict['A']
        elif FIRST_Y[1] == "First Rack":
            arranged_dict['R'] = original_data_dict['B']
        elif FIRST_Y[2] == "First Rack":
            arranged_dict['R'] = original_data_dict['C']
            
        if FIRST_Y[0] == "Second Rack":
            arranged_dict['Y'] = original_data_dict['A']
        elif FIRST_Y[1] == "Second Rack":
            arranged_dict['Y'] = original_data_dict['B']
        elif FIRST_Y[2] == "Second Rack":
            arranged_dict['Y'] = original_data_dict['C']
        
        if FIRST_Y[0] == "Third Rack":
            arranged_dict['B'] = original_data_dict['A']
        elif FIRST_Y[1] == "Third Rack":
            arranged_dict['B'] = original_data_dict['B']
        elif FIRST_Y[2] == "Third Rack":
            arranged_dict['B'] = original_data_dict['C']
        #___________________________________________________________________
        
        
            
        #___________________________________________________________________
        if second_Y[0] == "First Rack":
            arranged_dict_2['R'] = original_data_dict['a']
        elif second_Y[1] == "First Rack":
            arranged_dict_2['R'] = original_data_dict['b']
        elif second_Y[2] == "First Rack":
            arranged_dict_2['R'] = original_data_dict['c']
            
        if second_Y[0] == "Second Rack":
            arranged_dict_2['Y'] = original_data_dict['a']
        elif second_Y[1] == "Second Rack":
            arranged_dict_2['Y'] = original_data_dict['b']
        elif second_Y[2] == "Second Rack":
            arranged_dict_2['Y'] = original_data_dict['c']
        
        if second_Y[0] == "Third Rack":
            arranged_dict_2['B'] = original_data_dict['a']
        elif second_Y[1] == "Third Rack":
            arranged_dict_2['B'] = original_data_dict['b']
        elif second_Y[2] == "Third Rack":
            arranged_dict_2['B'] = original_data_dict['c']
        #___________________________________________________________________
        
        
        #print(arranged_dict)
        
        return [arranged_dict , arranged_dict_2]
            
    def calculate_best_swap(self):
        
        #--------------------------------------------------------------------------    
        arrangged_dict = self.get_inputData()
        if self.GENERATE_COUNTER == 0:
            self.ORIGINAL_INPUT = arrangged_dict # save the input data
        #-------------------------------------------------------------------------- 
        
        rack = self.comboBox_7.currentText()
        
        if rack == "First Rack":
            phase = "R"
        elif rack == "Second Rack":
            phase = "Y"
        elif rack == "Third Rack":
            phase = "B"
        
        #--------------------------------------------------------------------------    
        res = swap_caps(arrangged_dict[0] , arrangged_dict[1] , phase)
        swap_diff = res[0]
        Y1 = res[1]
        Y2 = res[2]
        #--------------------------------------------------------------------------    
                
        print(swap_diff)
        diff = 10e50
        pos = -1
        for k,ind in zip(swap_diff , [0,1,2,3]):
            if abs(k) < abs(diff):
                diff = abs(k) ; pos = ind 
        
        if pos == 0:
            print("0_0")
            if self.comboBox_7.currentText() == "First Rack" and (float(self.lineEdit.text()) != float(self.lineEdit_7.text())):
                self.text_swaper( self.label_13, self.label_20, self.lineEdit, self.lineEdit_7 )
            elif self.comboBox_7.currentText() == "Second Rack" and (float(self.lineEdit_3.text()) != float(self.lineEdit_11.text())):
                self.text_swaper( self.label_16, self.label_24, self.lineEdit_3, self.lineEdit_11 )
            elif self.comboBox_7.currentText() == "Third Rack" and (float(self.lineEdit_8.text()) != float(self.lineEdit_9.text())):
                self.text_swaper( self.label_18, self.label_22, self.lineEdit_8, self.lineEdit_9 )
                
            self.label_28.setText("Difference = " + str( abs(round(swap_diff[pos] , 4)) ) + ' μF')
            self.label_26.setText("Total 1 = " + str( round(Y1[pos] , 4) ) + ' μF')
            self.label_27.setText("Total 2 = " + str( round(Y2[pos] , 4) ) + ' μF')
            
                
        elif pos == 1:
            print("0_1")
            if self.comboBox_7.currentText() == "First Rack" and (float(self.lineEdit.text()) != float(self.lineEdit_4.text())):
                self.text_swaper( self.label_13, self.label_19, self.lineEdit, self.lineEdit_4 )
            elif self.comboBox_7.currentText() == "Second Rack" and (float(self.lineEdit_3.text()) != float(self.lineEdit_12.text())):
                self.text_swaper( self.label_16, self.label_23, self.lineEdit_3, self.lineEdit_12 )
            elif self.comboBox_7.currentText() == "Third Rack" and (float(self.lineEdit_5.text()) != float(self.lineEdit_10.text())):
                self.text_swaper( self.label_18, self.label_21, self.lineEdit_5, self.lineEdit_10 )
            
            self.label_28.setText("Difference = " + str( abs( round(swap_diff[pos], 4) )) + ' μF')
            self.label_26.setText("Total 1 = " + str( round(Y1[pos] , 4) ) + ' μF')
            self.label_27.setText("Total 2 = " + str( round(Y2[pos] , 4) ) + ' μF')
          
        elif pos == 2:
            print("1_0")
            if self.comboBox_7.currentText() == "First Rack" and (float(self.lineEdit_2.text()) != float(self.lineEdit_7.text())):
                self.text_swaper( self.label_14, self.label_20, self.lineEdit_2, self.lineEdit_7 )
            elif self.comboBox_7.currentText() == "Second Rack" and (float(self.lineEdit_4.text()) != float(self.lineEdit_11.text())):
                self.text_swaper( self.label_15, self.label_24, self.lineEdit_4, self.lineEdit_11 )
            elif self.comboBox_7.currentText() == "Third Rack" and (float(self.lineEdit_6.text()) != float(self.lineEdit_9.text())):
                self.text_swaper( self.label_17, self.label_22, self.lineEdit_6, self.lineEdit_9 )
            
            self.label_28.setText("Difference = " + str( abs(round( swap_diff[pos] , 4)) ) + ' μF')
            self.label_26.setText("Total 1 = " + str( round(Y1[pos] , 4) ) + ' μF')
            self.label_27.setText("Total 2 = " + str( round(Y2[pos] , 4) ) + ' μF')
            
        elif pos == 3:
            print("1_1")
            if self.comboBox_7.currentText() == "First Rack" and (float(self.lineEdit_2.text()) != float(self.lineEdit_8.text())):
                self.text_swaper( self.label_14, self.label_19, self.lineEdit_2, self.lineEdit_8 )
            elif self.comboBox_7.currentText() == "Second Rack"and (float(self.lineEdit_4.text()) != float(self.lineEdit_12.text())):
                self.text_swaper( self.label_15, self.label_23, self.lineEdit_4, self.lineEdit_12 )
            elif self.comboBox_7.currentText() == "Third Rack" and (float(self.lineEdit_6.text()) != float(self.lineEdit_10.text())):
                self.text_swaper( self.label_17, self.label_21, self.lineEdit_6, self.lineEdit_10 )
            
            self.label_28.setText("Difference = " + str( abs(round(swap_diff[pos] , 4)) ) + ' μF')
            self.label_26.setText("Total 1 = " + str( round(Y1[pos] , 4) ) + ' μF')
            self.label_27.setText("Total 2 = " + str( round(Y2[pos] , 4) ) + ' μF')
        
        # increase the counter
        self.GENERATE_COUNTER+=1 
        
        
    def text_swaper(self, lable_13, lable_20, lineEdit, lineEdit_7 ):
        txt1 = lable_20.text()
        txt2 = lable_13.text()
        lable_13.setText(txt1); lable_13.setStyleSheet("background-color: lightgreen") #rgb(240, 240, 240)
        lable_20.setText(txt2); lable_20.setStyleSheet("background-color: lightgreen")
        
        c1 = lineEdit.text()
        c2 = lineEdit_7.text()
        lineEdit_7.setText( c1 )
        lineEdit.setText( c2 )
    
    def reset_to_origial(self):
        self.label_13.setStyleSheet("background-color: rgb(240, 240, 240)") #rgb(240, 240, 240)
        self.label_14.setStyleSheet("background-color: rgb(240, 240, 240)")
        self.label_15.setStyleSheet("background-color: rgb(240, 240, 240)")
        self.label_16.setStyleSheet("background-color: rgb(240, 240, 240)")
        self.label_17.setStyleSheet("background-color: rgb(240, 240, 240)")
        self.label_18.setStyleSheet("background-color: rgb(240, 240, 240)")
        
        self.label_19.setStyleSheet("background-color: rgb(240, 240, 240)") #rgb(240, 240, 240)
        self.label_20.setStyleSheet("background-color: rgb(240, 240, 240)")
        self.label_21.setStyleSheet("background-color: rgb(240, 240, 240)")
        self.label_22.setStyleSheet("background-color: rgb(240, 240, 240)")
        self.label_23.setStyleSheet("background-color: rgb(240, 240, 240)")
        self.label_24.setStyleSheet("background-color: rgb(240, 240, 240)")
        
        
        # reset texts
        self.label_13.setText("C(1,0)")
        self.label_14.setText("C(1,1)")
        self.label_15.setText("C(1,3)")
        self.label_16.setText("C(1,2)")
        self.label_17.setText("C(1,5)")
        self.label_18.setText("C(1,4)")
        
        self.label_19.setText("C(2,1)")
        self.label_20.setText("C(2,0)")
        self.label_21.setText("C(2,5)")
        self.label_22.setText("C(2,4)")
        self.label_23.setText("C(2,3)")
        self.label_24.setText("C(2,2)")
        
        R = self.ORIGINAL_INPUT[0]['R']
        Y = self.ORIGINAL_INPUT[0]['Y']
        B = self.ORIGINAL_INPUT[0]['B']
        
        a = self.ORIGINAL_INPUT[1]['R']
        b = self.ORIGINAL_INPUT[1]['Y']
        c = self.ORIGINAL_INPUT[1]['B']
        
        
        self.lineEdit.setText(R[0]); self.lineEdit_2.setText(R[1])
        self.lineEdit_3.setText(Y[0]); self.lineEdit_4.setText(Y[1]) 
        self.lineEdit_5.setText(B[0]); self.lineEdit_6.setText(B[1]) 
        
        self.lineEdit_7.setText(a[0]); self.lineEdit_8.setText(a[1])
        self.lineEdit_11.setText(b[0]); self.lineEdit_12.setText(b[1])
        self.lineEdit_9.setText(c[0]); self.lineEdit_10.setText(c[1])
         
         
        
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Capacitor Balancer"))
        self.pushButton.setText(_translate("MainWindow", "Generate"))
        self.pushButton_2.setText(_translate("MainWindow", "Clear"))
        self.label.setText(_translate("MainWindow", "μF"))
        self.label_2.setText(_translate("MainWindow", "μF"))
        self.label_3.setText(_translate("MainWindow", "μF"))
        self.label_4.setText(_translate("MainWindow", "μF"))
        self.label_5.setText(_translate("MainWindow", "μF"))
        self.label_6.setText(_translate("MainWindow", "μF"))
        self.label_7.setText(_translate("MainWindow", "μF"))
        self.label_8.setText(_translate("MainWindow", "μF"))
        self.label_9.setText(_translate("MainWindow", "μF"))
        self.label_10.setText(_translate("MainWindow", "μF"))
        self.label_11.setText(_translate("MainWindow", "μF"))
        self.label_12.setText(_translate("MainWindow", "μF"))
        self.label_13.setText(_translate("MainWindow", "C(1,0)"))
        self.label_14.setText(_translate("MainWindow", "C(1,1)"))
        self.label_15.setText(_translate("MainWindow", "C(1,3)"))
        self.label_16.setText(_translate("MainWindow", "C(1,2)"))
        self.label_17.setText(_translate("MainWindow", "C(1,5)"))
        self.label_18.setText(_translate("MainWindow", "C(1,4)"))
        self.label_19.setText(_translate("MainWindow", "C(2,1)"))
        self.label_20.setText(_translate("MainWindow", "C(2,0)"))
        self.label_21.setText(_translate("MainWindow", "C(2,5)"))
        self.label_22.setText(_translate("MainWindow", "C(2,4)"))
        self.label_23.setText(_translate("MainWindow", "C(2,3)"))
        self.label_24.setText(_translate("MainWindow", "C(2,2)"))
        self.comboBox.setItemText(0, _translate("MainWindow", "First Rack"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Second Rack"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Third Rack"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Second Rack"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "First Rack"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "Third Rack"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "Third Rack"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "Second Rack"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "First Rack"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "First Rack"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "Second Rack"))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "Third Rack"))
        self.comboBox_5.setItemText(0, _translate("MainWindow", "Second Rack"))
        self.comboBox_5.setItemText(1, _translate("MainWindow", "First Rack"))
        self.comboBox_5.setItemText(2, _translate("MainWindow", "Third Rack"))
        self.comboBox_6.setItemText(0, _translate("MainWindow", "Third Rack"))
        self.comboBox_6.setItemText(1, _translate("MainWindow", "Second Rack"))
        self.comboBox_6.setItemText(2, _translate("MainWindow", "First Rack"))
        self.comboBox_7.setItemText(0, _translate("MainWindow", "First Rack"))
        self.comboBox_7.setItemText(1, _translate("MainWindow", "Second Rack"))
        self.comboBox_7.setItemText(2, _translate("MainWindow", "Third Rack"))
        self.label_25.setText(_translate("MainWindow", "Swap the "))
        self.label_26.setText(_translate("MainWindow", "Total 1 = "))
        self.label_27.setText(_translate("MainWindow", "Total 2 = "))
        self.label_28.setText(_translate("MainWindow", "Difference = "))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuExport.setTitle(_translate("MainWindow", "Export"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionPdf.setText(_translate("MainWindow", "Pdf"))
        self.actionWord.setText(_translate("MainWindow", "Word"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+Shift+E"))
        self.actionSave_2.setText(_translate("MainWindow", "Save"))
        self.actionSave_2.setToolTip(_translate("MainWindow", "Save"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionOpen_2.setText(_translate("MainWindow", "Open"))
        self.actionOpen_2.setToolTip(_translate("MainWindow", "Open"))
        self.actionDelete.setText(_translate("MainWindow", "Delete"))
        self.actionDelete.setToolTip(_translate("MainWindow", "Delete"))
        self.actionExport2Word.setText(_translate("MainWindow", "Export2Word"))
        self.actionExport2Word.setToolTip(_translate("MainWindow", "Export to word"))
        self.actionExport2PDF.setText(_translate("MainWindow", "Export2PDF"))
        self.actionExport2PDF.setToolTip(_translate("MainWindow", "Export to pdf"))
        self.actionDelete_2.setText(_translate("MainWindow", "Delete"))
        self.actionRestore_Original.setText(_translate("MainWindow", "Restore Original"))
        self.actionRestore_Original.setToolTip(_translate("MainWindow", "Restore Original"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    #global ui
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
