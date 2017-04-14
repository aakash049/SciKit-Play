import os
from PyQt4 import QtCore, QtGui

c1 = 0
c2 = 0
c3 = 0
c4 = 0
counter = 0

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8


    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_widget(object):
    #############################################################################################################################
    def call(self):
        url = QtCore.QUrl('utilities\CursorPosition.exe')
        QtGui.QDesktopServices.openUrl(url)

    def callagain(self):
        import webbrowser
        import time
        webbrowser.open("https://royalgames.com/games/puzzle-games/candy-crush/?language=en_US&action=play")
        time.sleep(0.9)
        self.web()

    def web(self):
        import key
        key.hook()

    def callmain(self):
        if counter==1:
            global c1
            global c2
            global c3
            global c4
            c1 = int(self.v1.text())
            c2 = int(self.v2.text())
            c3 = int(self.v3.text())
            c4 = int(self.v4.text())
        board_coords = (c1, c2, c3, c4)
        import driver
        driver_obj = driver.Driver(board_coords)
        driver_obj.play()

    def combo_chosen_1(self):
        global counter
        counter = 0
        global c1
        global c2
        global c3
        global c4 
        c1 = int(688)
        c2 = int(60)
        c3 = int(1325)
        c4 = int(622)

    def combo_chosen_2(self):
        global counter
        counter = 0
        global c1
        global c2
        global c3
        global c4 
        c1 = int(436)
        c2 = int(55)
        c3 = int(1010)
        c4 = int(563)

    def statistic(self):
        url_1 = QtCore.QUrl('utilities\stat_1.pyw')
        QtGui.QDesktopServices.openUrl(url_1)

    def combo_chosen_3(self):
        import win32api
        win32api.MessageBox(0, 'Please Get your coordinates and Enter them on the right side!', 'Message',QtCore.Qt.WindowStaysOnTopHint)
        global counter
        counter = 1

    #############################################################################################################################

    def setupUi(self, widget):
        widget.setObjectName(_fromUtf8("widget"))
        widget.setWindowModality(QtCore.Qt.ApplicationModal)
        widget.setEnabled(True)
        widget.resize(590, 274)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(widget.sizePolicy().hasHeightForWidth())
        widget.setSizePolicy(sizePolicy)
        widget.setMinimumSize(QtCore.QSize(590, 274))
        widget.setMaximumSize(QtCore.QSize(590, 274))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("py.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        widget.setWindowIcon(icon)
        widget.setWindowOpacity(5.0)
        widget.setAutoFillBackground(False)
        widget.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);"))
        self.b3 = QtGui.QPushButton(widget)
        self.b3.setGeometry(QtCore.QRect(330, 220, 241, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.b3.setFont(font)
        self.b3.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
                                        "font: 18pt \"MS Shell Dlg 2\";\n"
                                        "background-color: rgb(68, 163, 252);"))
        self.b3.setObjectName(_fromUtf8("b3"))
        ######## button event3 ##########
        self.b3.clicked.connect(self.callmain)
        #################################
        self.b2 = QtGui.QPushButton(widget)
        self.b2.setGeometry(QtCore.QRect(20, 90, 251, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato Heavy"))
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.b2.setFont(font)
        self.b2.setStyleSheet(_fromUtf8("background-color: rgb(255,255,255);\n"
                                        "font: 87 12pt \"Lato Heavy\";\n"
                                        "alternate-background-color:rgb(0,0,0,0);\n"
                                        "color: rgb(0,0,0);\n"
                                        "border-width:5px;\n"
                                        "border-style:groove;\n"
                                        "border-top-color: rgb(61, 147, 227);\n"
                                        "border-left-color: rgb(61, 147, 227);\n"
                                        "border-right-color: rgb(239, 213, 94);\n"
                                        "border-bottom-color: rgb(239, 213, 94);\n"
                                        ""))
        self.b2.setObjectName(_fromUtf8("b2"))
        ######## button event2 ##########
        self.b2.clicked.connect(self.callagain)
        #################################
        self.b1 = QtGui.QPushButton(widget)
        self.b1.setGeometry(QtCore.QRect(330, 90, 241, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato Heavy"))
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.b1.setFont(font)
        self.b1.setStyleSheet(_fromUtf8("background-color: rgb(255,255,255);\n"
                                        "font: 87 12pt \"Lato Heavy\";\n"
                                        "color: rgb(0,0,0);\n"
                                        "border-width:5px;\n"
                                        "border-style:groove;\n"
                                        "border-top-color: rgb(61, 147, 227);\n"
                                        "border-left-color: rgb(61, 147, 227);\n"
                                        "border-right-color: rgb(239, 213, 94);\n"
                                        "border-bottom-color: rgb(239, 213, 94);\n"
                                        ""))
        self.b1.setObjectName(_fromUtf8("b1"))
        ######## button event1 ##########
        self.b1.clicked.connect(self.call)
        #################################
        self.label1 = QtGui.QLabel(widget)
        self.label1.setGeometry(QtCore.QRect(190, 10, 161, 72))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label1.setFont(font)
        self.label1.setStatusTip(_fromUtf8(""))
        self.label1.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.label1.setObjectName(_fromUtf8("label1"))
        self.label_pic = QtGui.QLabel(widget)
        self.label_pic.setGeometry(QtCore.QRect(110, 10, 81, 71))
        self.label_pic.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
                                               "color: rgb(0, 0, 0);"))
        self.label_pic.setText(_fromUtf8(""))
        self.label_pic.setObjectName(_fromUtf8("label_pic"))
        #################pic#############
        self.label_pic.setPixmap(QtGui.QPixmap(os.getcwd() + "/py.png"))
        #################################
        self.label1_2 = QtGui.QLabel(widget)
        self.label1_2.setGeometry(QtCore.QRect(360, 10, 51, 72))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label1_2.setFont(font)
        self.label1_2.setStatusTip(_fromUtf8(""))
        self.label1_2.setStyleSheet(_fromUtf8("color: rgb(61, 147, 227);"))
        self.label1_2.setObjectName(_fromUtf8("label1_2"))
        self.label1_3 = QtGui.QLabel(widget)
        self.label1_3.setGeometry(QtCore.QRect(410, 10, 61, 72))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label1_3.setFont(font)
        self.label1_3.setStatusTip(_fromUtf8(""))
        self.label1_3.setStyleSheet(_fromUtf8("color: rgb(239, 213, 94);"))
        self.label1_3.setObjectName(_fromUtf8("label1_3"))
        self.horizontalLayoutWidget_2 = QtGui.QWidget(widget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 130, 271, 81))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_3 = QtGui.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato Black"))
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
                                             "border-color: rgb(0, 0, 234);\n"
                                             "font: 87 12pt \"Lato Black\";"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.radioButton = QtGui.QRadioButton(self.horizontalLayoutWidget_2)
        self.radioButton.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
                                                 "font: 87 12pt \"Lato Black\";color: rgb(255, 255, 255);\n"
                                                 "font: 87 12pt \"Lato Black\";"))
        self.radioButton.setCheckable(True)
        self.radioButton.setChecked(False)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        ##############################
        self.radioButton.clicked.connect(self.combo_chosen_2)
        ###############################
        self.verticalLayout.addWidget(self.radioButton)
        self.radioButton_2 = QtGui.QRadioButton(self.horizontalLayoutWidget_2)
        self.radioButton_2.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
                                                   "font: 87 12pt \"Lato Black\";color: rgb(255, 255, 255);\n"
                                                   "font: 87 12pt \"Lato Black\";"))
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        ##############################
        self.radioButton_2.clicked.connect(self.combo_chosen_1)
        ###############################
        self.verticalLayout.addWidget(self.radioButton_2)
        self.radioButton_3 = QtGui.QRadioButton(self.horizontalLayoutWidget_2)
        self.radioButton_3.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
                                                   "font: 87 12pt \"Lato Black\";color: rgb(255, 255, 255);\n"
                                                   "font: 87 12pt \"Lato Black\";"))
        self.radioButton_3.setObjectName(_fromUtf8("radioButton_3"))
        ##############################
        self.radioButton_3.clicked.connect(self.combo_chosen_3)
        ###############################
        self.verticalLayout.addWidget(self.radioButton_3)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.v1 = QtGui.QLineEdit(widget)
        self.v1.setGeometry(QtCore.QRect(340, 180, 51, 22))
        self.v1.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.v1.setObjectName(_fromUtf8("v1"))
        self.v2 = QtGui.QLineEdit(widget)
        self.v2.setGeometry(QtCore.QRect(400, 180, 51, 22))
        self.v2.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.v2.setObjectName(_fromUtf8("v2"))
        self.v3 = QtGui.QLineEdit(widget)
        self.v3.setGeometry(QtCore.QRect(460, 180, 51, 22))
        self.v3.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.v3.setObjectName(_fromUtf8("v3"))
        self.v4 = QtGui.QLineEdit(widget)
        self.v4.setGeometry(QtCore.QRect(520, 180, 51, 22))
        self.v4.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.v4.setObjectName(_fromUtf8("v4"))

        self.label_4 = QtGui.QLabel(widget)
        self.label_4.setGeometry(QtCore.QRect(340, 150, 209, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
                                             "border-color: rgb(0, 0, 234);"))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.line = QtGui.QFrame(widget)
        self.line.setGeometry(QtCore.QRect(300, 150, 3, 59))
        self.line.setStyleSheet(_fromUtf8("color: rgb(186, 186, 186);\n"
                                          "background-color: rgb(186, 186, 186);"))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.b2_2 = QtGui.QPushButton(widget)
        self.b2_2.setGeometry(QtCore.QRect(20, 220, 251, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato heavy"))
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.b2_2.setFont(font)
        self.b2_2.setStyleSheet(_fromUtf8("background-color: rgb(255,255,255);\n"
                                          "font: 87 12pt \"Lato heavy\";\n"
                                          "alternate-background-color:rgb(0,0,0,0);\n"
                                          "color: rgb(0,0,0);\n"
                                          "border-width:5px;\n"
                                          "border-style:groove;\n"
                                          "border-top-color: rgb(61, 147, 227);\n"
                                          "border-left-color: rgb(61, 147, 227);\n"
                                          "border-right-color: rgb(239, 213, 94);\n"
                                          "border-bottom-color: rgb(239, 213, 94);\n"
                                          ""))
        self.b2_2.setObjectName(_fromUtf8("b2_2"))
        ##############################
        self.b2_2.clicked.connect(self.statistic)
        #############################
        self.b3.raise_()
        self.b1.raise_()
        self.b2.raise_()
        self.label1.raise_()
        self.label1_2.raise_()
        self.label1_3.raise_()
        self.label_pic.raise_()
        self.horizontalLayoutWidget_2.raise_()
        self.v4.raise_()
        self.v1.raise_()
        self.v2.raise_()
        self.label_4.raise_()
        self.v3.raise_()
        self.line.raise_()
        self.b2_2.raise_()

        self.retranslateUi(widget)
        QtCore.QMetaObject.connectSlotsByName(widget)


    def retranslateUi(self, widget):
        widget.setWindowTitle(_translate("widget", "SciKit-Play", None))
        self.b3.setText(_translate("widget", "Start SciKit-Play", None))
        self.b2.setText(_translate("widget", "START Your Game!", None))
        self.b1.setText(_translate("widget", "Get coordinates", None))
        self.label1.setText(_translate("widget", "SciKit", None))
        self.label1_2.setText(_translate("widget", "Pl", None))
        self.label1_3.setText(_translate("widget", "ay", None))
        self.label_3.setToolTip(_translate("widget",
                                           "<html><head/><body><p><span style=\" color:#ffffff;\">your coordinates</span></p></body></html>",
                                           None))
        self.label_3.setText(_translate("widget", "Resolution:", None))
        self.radioButton.setText(_translate("widget", "1920 x 1080", None))
        self.radioButton_2.setText(_translate("widget", "1366 x 768", None))
        self.radioButton_3.setText(_translate("widget", "Customized", None))
        self.label_4.setToolTip(_translate("widget",
                                           "<html><head/><body><p><span style=\" color:#ffffff;\">your coordinates</span></p></body></html>",
                                           None))
        self.label_4.setText(_translate("widget", "Enter Coordinates Here :", None))
        self.b2_2.setText(_translate("widget", "Show Statistics", None))

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    widget = QtGui.QWidget()
    ui = Ui_widget()
    ui.setupUi(widget)
    widget.setWindowFlags(widget.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)
    widget.show()
    sys.exit(app.exec_())
