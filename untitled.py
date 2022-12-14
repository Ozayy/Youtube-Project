# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1279, 898)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(30, 70, 1231, 821))
        self.stackedWidget.setStyleSheet("")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.frame_3 = QtWidgets.QFrame(self.page)
        self.frame_3.setGeometry(QtCore.QRect(0, 0, 1231, 821))
        self.frame_3.setStyleSheet("background-color:qlineargradient(spread:pad,x1:0.091,y1:0.101636,x2:0.991379,y2:0.977,stop:0 rgba(209,107,165,255),stop:1 rgba(255,255,255,255))")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setGeometry(QtCore.QRect(590, 180, 361, 471))
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:30px\n"
"")
        self.label.setText("")
        self.label.setObjectName("label")
        self.login_button = QtWidgets.QPushButton(self.frame_3)
        self.login_button.setGeometry(QtCore.QRect(630, 510, 141, 51))
        self.login_button.setStyleSheet("QPushButton{\n"
"background-color:rgba(85,98,112,255);\n"
"color:rgba(255,255,255,200);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgba(255,107,107,255);\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgba(255,107,107,255);\n"
"}")
        self.login_button.setObjectName("login_button")
        self.User_login = QtWidgets.QLineEdit(self.frame_3)
        self.User_login.setGeometry(QtCore.QRect(630, 350, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.User_login.setFont(font)
        self.User_login.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,200);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px\n"
"")
        self.User_login.setObjectName("User_login")
        self.Password_login = QtWidgets.QLineEdit(self.frame_3)
        self.Password_login.setGeometry(QtCore.QRect(630, 430, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Password_login.setFont(font)
        self.Password_login.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,200);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px\n"
"")
        self.Password_login.setObjectName("Password_login")
        self.label_11 = QtWidgets.QLabel(self.frame_3)
        self.label_11.setGeometry(QtCore.QRect(630, 280, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_11.setObjectName("label_11")
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setGeometry(QtCore.QRect(240, 180, 361, 471))
        self.label_3.setStyleSheet("background-color: qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 rgba(85,98,112,255),stop: 1 rgba(255,107,107,255));\n"
"border-radius:20px")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.frame_4 = QtWidgets.QFrame(self.page_2)
        self.frame_4.setGeometry(QtCore.QRect(0, 0, 1231, 821))
        self.frame_4.setStyleSheet("background-color:rgb(247,239,237)")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.tableWidget = QtWidgets.QTableWidget(self.frame_4)
        self.tableWidget.setGeometry(QtCore.QRect(280, 100, 821, 581))
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.table_approve = QtWidgets.QPushButton(self.frame_4)
        self.table_approve.setGeometry(QtCore.QRect(280, 700, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.table_approve.setFont(font)
        self.table_approve.setStyleSheet("\n"
"QPushButton{\n"
"background-color: rgb(203,200,177);\n"
"border-radius:10px\n"
"}\n"
"QPushButton:hover{\n"
"background:rgb(195,207,226)\n"
"}")
        self.table_approve.setObjectName("table_approve")
        self.user_table_line = QtWidgets.QLineEdit(self.frame_4)
        self.user_table_line.setGeometry(QtCore.QRect(130, 145, 141, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.user_table_line.setFont(font)
        self.user_table_line.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.user_table_line.setObjectName("user_table_line")
        self.deneme1 = QtWidgets.QPushButton(self.frame_4)
        self.deneme1.setGeometry(QtCore.QRect(600, 700, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.deneme1.setFont(font)
        self.deneme1.setStyleSheet("\n"
"QPushButton{\n"
"background-color: rgb(203,200,177);\n"
"border-radius:10px\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(255,176,163)\n"
"}")
        self.deneme1.setObjectName("deneme1")
        self.table_goback = QtWidgets.QPushButton(self.frame_4)
        self.table_goback.setGeometry(QtCore.QRect(980, 700, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.table_goback.setFont(font)
        self.table_goback.setStyleSheet("\n"
"QPushButton{\n"
"background-color: rgb(203,200,177);\n"
"border-radius:10px\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(255,176,163)\n"
"}")
        self.table_goback.setObjectName("table_goback")
        self.label_44 = QtWidgets.QLabel(self.frame_4)
        self.label_44.setGeometry(QtCore.QRect(40, 130, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_44.setFont(font)
        self.label_44.setObjectName("label_44")
        self.user_password_line = QtWidgets.QLineEdit(self.frame_4)
        self.user_password_line.setGeometry(QtCore.QRect(130, 240, 141, 21))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.user_password_line.setFont(font)
        self.user_password_line.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.user_password_line.setObjectName("user_password_line")
        self.label_6 = QtWidgets.QLabel(self.frame_4)
        self.label_6.setGeometry(QtCore.QRect(40, 180, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.add_table = QtWidgets.QPushButton(self.frame_4)
        self.add_table.setGeometry(QtCore.QRect(140, 280, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.add_table.setFont(font)
        self.add_table.setStyleSheet("\n"
"QPushButton{\n"
"background-color: rgb(203,200,177);\n"
"border-radius:10px\n"
"}\n"
"QPushButton:hover{\n"
"background:rgb(195,207,226)\n"
"}")
        self.add_table.setObjectName("add_table")
        self.delete_table = QtWidgets.QPushButton(self.frame_4)
        self.delete_table.setGeometry(QtCore.QRect(140, 440, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.delete_table.setFont(font)
        self.delete_table.setStyleSheet("\n"
"QPushButton{\n"
"background-color: rgb(203,200,177);\n"
"border-radius:10px\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(255,176,163)\n"
"}")
        self.delete_table.setObjectName("delete_table")
        self.update_table = QtWidgets.QPushButton(self.frame_4)
        self.update_table.setGeometry(QtCore.QRect(140, 360, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.update_table.setFont(font)
        self.update_table.setStyleSheet("\n"
"QPushButton{\n"
"background-color: rgb(203,200,177);\n"
"border-radius:10px\n"
"}\n"
"QPushButton:hover{\n"
"background:rgb(195,207,226)\n"
"}")
        self.update_table.setObjectName("update_table")
        self.label_45 = QtWidgets.QLabel(self.frame_4)
        self.label_45.setGeometry(QtCore.QRect(40, 90, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_45.setFont(font)
        self.label_45.setObjectName("label_45")
        self.user_id_line = QtWidgets.QLineEdit(self.frame_4)
        self.user_id_line.setGeometry(QtCore.QRect(130, 103, 141, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.user_id_line.setFont(font)
        self.user_id_line.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.user_id_line.setObjectName("user_id_line")
        self.labell = QtWidgets.QLabel(self.frame_4)
        self.labell.setGeometry(QtCore.QRect(40, 233, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labell.setFont(font)
        self.labell.setObjectName("labell")
        self.comboBox_2 = QtWidgets.QComboBox(self.frame_4)
        self.comboBox_2.setGeometry(QtCore.QRect(130, 190, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.alanlari_temizle = QtWidgets.QPushButton(self.frame_4)
        self.alanlari_temizle.setGeometry(QtCore.QRect(10, 280, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.alanlari_temizle.setFont(font)
        self.alanlari_temizle.setStyleSheet("\n"
"QPushButton{\n"
"background-color: rgb(203,200,177);\n"
"border-radius:10px\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(255,176,163)\n"
"}")
        self.alanlari_temizle.setObjectName("alanlari_temizle")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.frame_2 = QtWidgets.QFrame(self.page_3)
        self.frame_2.setGeometry(QtCore.QRect(0, 10, 1231, 801))
        self.frame_2.setStyleSheet("QFrame{\n"
"background-color:rgb(25, 86, 155, 255);\n"
"color:rgb(220,220,220);\n"
"border-radius: 20px;\n"
"\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(270, 70, 481, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 170, 255);")
        self.label_4.setObjectName("label_4")
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(40, 180, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(255, 170, 255);")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setGeometry(QtCore.QRect(40, 240, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(255, 170, 255);")
        self.label_8.setObjectName("label_8")
        self.link_line = QtWidgets.QLineEdit(self.frame_2)
        self.link_line.setGeometry(QtCore.QRect(140, 190, 551, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.link_line.setFont(font)
        self.link_line.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:1px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgba(255,255,255);\n"
"padding-bottom:7px")
        self.link_line.setAlignment(QtCore.Qt.AlignCenter)
        self.link_line.setPlaceholderText("")
        self.link_line.setObjectName("link_line")
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        self.label_9.setGeometry(QtCore.QRect(170, 250, 511, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:1px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgba(255,255,255);\n"
"padding-bottom:7px")
        self.label_9.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_9.setText("")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setOpenExternalLinks(False)
        self.label_9.setObjectName("label_9")
        self.browse_konum = QtWidgets.QPushButton(self.frame_2)
        self.browse_konum.setGeometry(QtCore.QRect(710, 250, 91, 51))
        self.browse_konum.setStyleSheet("QPushButton {\n"
"border-radius:10px;\n"
"font: 87 8pt \"Arial Black\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(255, 170, 255);\n"
"    border: 0px solid\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(85, 255, 255);\n"
"\n"
"}")
        self.browse_konum.setObjectName("browse_konum")
        self.download_button = QtWidgets.QPushButton(self.frame_2)
        self.download_button.setGeometry(QtCore.QRect(230, 430, 381, 71))
        self.download_button.setStyleSheet("QpushButton#pushButton{\n"
"background-color:rgba(2,65,118,255);\n"
"color:rgba(255,255,255,200);\n"
"border-radius:6px;\n"
"}\n"
"QPushButton#pushButton:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgba(2,65,118,100);\n"
"background-position:calc(100%-10px)center;\n"
"\n"
"}\n"
"\n"
"QPushButton#pushButton{\n"
"background-color:rgba(2,65,118,200);\n"
"}")
        self.download_button.setObjectName("download_button")
        self.label_10 = QtWidgets.QLabel(self.frame_2)
        self.label_10.setGeometry(QtCore.QRect(700, 320, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.mp4_radio = QtWidgets.QRadioButton(self.frame_2)
        self.mp4_radio.setGeometry(QtCore.QRect(730, 390, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.mp4_radio.setFont(font)
        self.mp4_radio.setStyleSheet("color: rgb(255, 170, 255);")
        self.mp4_radio.setObjectName("mp4_radio")
        self.mp3_radio = QtWidgets.QRadioButton(self.frame_2)
        self.mp3_radio.setGeometry(QtCore.QRect(730, 430, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.mp3_radio.setFont(font)
        self.mp3_radio.setStyleSheet("color: rgb(255, 170, 255);")
        self.mp3_radio.setObjectName("mp3_radio")
        self.progressBar = QtWidgets.QProgressBar(self.frame_2)
        self.progressBar.setGeometry(QtCore.QRect(220, 570, 391, 51))
        self.progressBar.setStyleSheet("QProgressBar{\n"
"background-color: rgb(255, 255, 255);\n"
" color: rgb(200, 200, 200);\n"
"  border-style: none;\n"
"  border-radius: 23px;\n"
"  text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"border-radius : 23;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(251, 108, 108, 255), stop:1 rgba(61, 188, 254, 255));\n"
"}")
        self.progressBar.setMaximum(100)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar.setObjectName("progressBar")
        self.refresh_button = QtWidgets.QPushButton(self.frame_2)
        self.refresh_button.setGeometry(QtCore.QRect(960, 620, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.refresh_button.setFont(font)
        self.refresh_button.setStyleSheet("QPushButton {\n"
"\n"
"background: rgb(0,170,255);\n"
"border: 2px solid rgb(0,170,255);\n"
"border-radius: 20px;\n"
"color: white;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(255,0,127);\n"
"border:2px rgb(255,0,127);\n"
"\n"
"}")
        self.refresh_button.setObjectName("refresh_button")
        self.listWidget = QtWidgets.QListWidget(self.frame_2)
        self.listWidget.setGeometry(QtCore.QRect(840, 110, 371, 471))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.listWidget.setFont(font)
        self.listWidget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.listWidget.setObjectName("listWidget")
        self.comboBox = QtWidgets.QComboBox(self.frame_2)
        self.comboBox.setGeometry(QtCore.QRect(700, 480, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.comboBox.setObjectName("comboBox")
        self.combobox_secim = QtWidgets.QComboBox(self.frame_2)
        self.combobox_secim.setGeometry(QtCore.QRect(700, 360, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.combobox_secim.setFont(font)
        self.combobox_secim.setEditable(False)
        self.combobox_secim.setObjectName("combobox_secim")
        self.combobox_secim.addItem("")
        self.combobox_secim.addItem("")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(340, 670, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
"\n"
"background: rgb(0,170,255);\n"
"border: 2px solid rgb(0,170,255);\n"
"border-radius: 20px;\n"
"color: white;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(255,0,127);\n"
"border:2px rgb(255,0,127);\n"
"\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(70, 50, 121, 111))
        self.label_2.setStyleSheet("image: url(:/resim/youtubee.gif);")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/resim/youtubee.gif"))
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.stackedWidget.addWidget(self.page_3)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 0, 1231, 111))
        self.frame.setStyleSheet("background-color:rgba(85,98,112,255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.icona = QtWidgets.QPushButton(self.frame)
        self.icona.setGeometry(QtCore.QRect(1120, 10, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.icona.setFont(font)
        self.icona.setStyleSheet("QPushButton {\n"
"background-color: rgb(253, 188, 64);\n"
"color: rgb(253, 188, 64);\n"
"border-radius: 14.99px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    background-color: rgb(203, 166, 44);\n"
"\n"
"    color: rgb(255, 255, 255);\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(203, 166, 44);\n"
"border-radius: 10.99px;\n"
"}")
        self.icona.setIconSize(QtCore.QSize(30, 30))
        self.icona.setCheckable(False)
        self.icona.setAutoRepeat(False)
        self.icona.setObjectName("icona")
        self.close = QtWidgets.QPushButton(self.frame)
        self.close.setGeometry(QtCore.QRect(1170, 10, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.close.setFont(font)
        self.close.setStyleSheet("QPushButton {\n"
"background-color: rgb(252, 87, 83);\n"
"border-radius: 14.99px;\n"
"color: rgb(252, 87, 83);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    background-color: rgb(193, 65, 63);\n"
"\n"
"    color: rgb(255, 255, 255);\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(193, 65, 63);\n"
"border-radius: 10.99px;\n"
"}")
        self.close.setIconSize(QtCore.QSize(80, 80))
        self.close.setCheckable(False)
        self.close.setChecked(False)
        self.close.setAutoRepeat(False)
        self.close.setAutoExclusive(False)
        self.close.setObjectName("close")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(2)
        self.comboBox_2.setCurrentIndex(-1)
        self.combobox_secim.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.login_button.setText(_translate("MainWindow", "L O G I N"))
        self.User_login.setPlaceholderText(_translate("MainWindow", "User Name"))
        self.Password_login.setPlaceholderText(_translate("MainWindow", "Password"))
        self.label_11.setText(_translate("MainWindow", "Log In"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "User Id"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "UserName"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Password"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Status"))
        self.table_approve.setText(_translate("MainWindow", "Aprrove"))
        self.deneme1.setText(_translate("MainWindow", "Video download"))
        self.table_goback.setText(_translate("MainWindow", "Go Back"))
        self.label_44.setText(_translate("MainWindow", "User Name:"))
        self.label_6.setText(_translate("MainWindow", "Status:"))
        self.add_table.setText(_translate("MainWindow", "Add"))
        self.delete_table.setText(_translate("MainWindow", "Delete"))
        self.update_table.setText(_translate("MainWindow", "Update"))
        self.label_45.setText(_translate("MainWindow", "User Id:"))
        self.labell.setText(_translate("MainWindow", "Passsword:"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Aktif"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Pasif"))
        self.alanlari_temizle.setText(_translate("MainWindow", "Clear"))
        self.label_4.setText(_translate("MainWindow", "<strong>Youtube Download</strong> "))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p>Link:</p><p><br/></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "Hedef:"))
        self.browse_konum.setText(_translate("MainWindow", "B R O W S E"))
        self.download_button.setText(_translate("MainWindow", "D  O  W  N  L  O  A  D  V  ??  D  E  O"))
        self.label_10.setText(_translate("MainWindow", "Format?? se??"))
        self.mp4_radio.setText(_translate("MainWindow", "mp4"))
        self.mp3_radio.setText(_translate("MainWindow", "mp3"))
        self.refresh_button.setText(_translate("MainWindow", "R E F R E S H"))
        self.combobox_secim.setItemText(0, _translate("MainWindow", "Playlist"))
        self.combobox_secim.setItemText(1, _translate("MainWindow", "Tekvideo"))
        self.pushButton.setText(_translate("MainWindow", "H O M E P A G E"))
        self.icona.setText(_translate("MainWindow", "_"))
        self.close.setText(_translate("MainWindow", "X"))
import resim_rc
