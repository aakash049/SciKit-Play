from PyQt4 import QtCore, QtGui
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
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
        url = QtCore.QUrl('C:\Users\Aadit bhojgi\Desktop\Cursor Position')
        QtGui.QDesktopServices.openUrl(url)

    def callagain(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--kiosk")
        options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
        browser = webdriver.Chrome(chrome_options=options)
        browser.get("http://www.royalgames.com/games/puzzle-games/candy-crush/?language=en_US&action=play")
        browser.execute_script("document.body.style.zoom='111%'")
        # browser.set_window_size(500, 500)
        # browser.maximize_window()
        # webbrowser.open("http://www.royalgames.com/games/puzzle-games/candy-crush/?language=en_US&action=play")

    def callmain(self):
        v1 = int(self.c1.text())
        v2 = int(self.c2.text())
        v3 = int(self.c3.text())
        v4 = int(self.c4.text())
        board_coords = (v1, v2, v3, v4)
        import driver
        driver_obj = driver.Driver(board_coords)
        driver_obj.play()


        #############################################################################################################################
    def setupUi(self, widget):
        widget.setObjectName(_fromUtf8("widget"))
        widget.setWindowModality(QtCore.Qt.ApplicationModal)
        widget.resize(551, 222)
        widget.setMinimumSize(QtCore.QSize(540, 222))
        widget.setMaximumSize(QtCore.QSize(551, 222))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("py.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        widget.setWindowIcon(icon)
        widget.setWindowOpacity(5.0)
        widget.setAutoFillBackground(False)
        widget.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);"))
        self.b3 = QtGui.QPushButton(widget)
        self.b3.setGeometry(QtCore.QRect(310, 170, 221, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.b3.setFont(font)
        self.b3.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgb(68, 163, 252);"))
        self.b3.setObjectName(_fromUtf8("b3"))
        ######## button event3 ##########
        self.b3.clicked.connect(self.callmain)
        #################################
        self.label = QtGui.QLabel(widget)
        self.label.setGeometry(QtCore.QRect(20, 143, 209, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 234);"))
        self.label.setObjectName(_fromUtf8("label"))
        self.b2 = QtGui.QPushButton(widget)
        self.b2.setGeometry(QtCore.QRect(20, 90, 221, 28))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.b2.setFont(font)
        self.b2.setStyleSheet(_fromUtf8("background-color: rgb(255,255,255);\n"
"color: rgb(0,0,0);\n"
"border-width:3px;\n"
"border-style:groove;\n"
"border-top-color: rgb(61, 147, 227);\n"
"border-left-color: rgb(61, 147, 227);\n"
"border-right-color: rgb(239, 213, 94);\n"
"border-bottom-color: rgb(239, 213, 94);"))
        self.b2.setObjectName(_fromUtf8("b2"))
        ######## button event2 ##########
        self.b2.clicked.connect(self.callagain)
        #################################
        self.b1 = QtGui.QPushButton(widget)
        self.b1.setGeometry(QtCore.QRect(307, 90, 222, 28))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.b1.setFont(font)
        self.b1.setStyleSheet(_fromUtf8("background-color: rgb(255,255,255);\n"
"color: rgb(0,0,0);\n"
"border-width:3px;\n"
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
        self.label1.setGeometry(QtCore.QRect(140, 10, 161, 72))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label1.setFont(font)
        self.label1.setStatusTip(_fromUtf8(""))
        self.label1.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.label1.setObjectName(_fromUtf8("label1"))
        self.horizontalLayoutWidget = QtGui.QWidget(widget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 160, 291, 51))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.c1 = QtGui.QLineEdit(self.horizontalLayoutWidget)
        self.c1.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"alternate-background-color: rgb(0, 0, 0);\n"
"background-color: rgb(0, 0, 0);\n"
"selection-color: rgb(0, 0, 0);\n"
"selection-background-color: rgb(0, 0, 0);"))
        self.c1.setObjectName(_fromUtf8("c1"))
        self.horizontalLayout_2.addWidget(self.c1)
        self.c2 = QtGui.QLineEdit(self.horizontalLayoutWidget)
        self.c2.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"alternate-background-color: rgb(0, 0, 0);\n"
"background-color: rgb(0, 0, 0);\n"
"selection-color: rgb(0, 0, 0);\n"
"selection-background-color: rgb(0, 0, 0);"))
        self.c2.setObjectName(_fromUtf8("c2"))
        self.horizontalLayout_2.addWidget(self.c2)
        self.c3 = QtGui.QLineEdit(self.horizontalLayoutWidget)
        self.c3.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"alternate-background-color: rgb(0, 0, 0);\n"
"background-color: rgb(0, 0, 0);\n"
"selection-color: rgb(0, 0, 0);\n"
"selection-background-color: rgb(0, 0, 0);"))
        self.c3.setObjectName(_fromUtf8("c3"))
        self.horizontalLayout_2.addWidget(self.c3)
        self.c4 = QtGui.QLineEdit(self.horizontalLayoutWidget)
        self.c4.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.c4.setMouseTracking(False)
        self.c4.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"alternate-background-color: rgb(0, 0, 0);\n"
"background-color: rgb(0, 0, 0);\n"
"selection-color: rgb(0, 0, 0);\n"
"selection-background-color: rgb(0, 0, 0);"))
        self.c4.setObjectName(_fromUtf8("c4"))
        self.horizontalLayout_2.addWidget(self.c4)
        self.horizontalLayout.addLayout(self.horizontalLayout_2)
        self.label_pic = QtGui.QLabel(widget)
        self.label_pic.setGeometry(QtCore.QRect(60, 10, 81, 71))
        self.label_pic.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"color: rgb(0, 0, 0);"))
        self.label_pic.setText(_fromUtf8(""))
        self.label_pic.setObjectName(_fromUtf8("label_pic"))
        self.label_pic.setPixmap(QtGui.QPixmap(os.getcwd() + "/py.png"))
        self.label1_2 = QtGui.QLabel(widget)
        self.label1_2.setGeometry(QtCore.QRect(310, 10, 51, 72))
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
        self.label1_3.setGeometry(QtCore.QRect(360, 10, 61, 72))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label1_3.setFont(font)
        self.label1_3.setStatusTip(_fromUtf8(""))
        self.label1_3.setStyleSheet(_fromUtf8("color: rgb(239, 213, 94);"))
        self.label1_3.setObjectName(_fromUtf8("label1_3"))
        self.b3.raise_()
        self.label.raise_()
        self.b1.raise_()
        self.b2.raise_()
        self.label1.raise_()
        self.horizontalLayoutWidget.raise_()
        self.label1_2.raise_()
        self.label1_3.raise_()
        self.label_pic.raise_()

        self.retranslateUi(widget)
        QtCore.QMetaObject.connectSlotsByName(widget)

    def retranslateUi(self, widget):
        widget.setWindowTitle(_translate("widget", "SciKit-Play", None))
        self.b3.setText(_translate("widget", "Start SciKit-Play", None))
        self.label.setToolTip(_translate("widget", "<html><head/><body><p><span style=\" color:#ffffff;\">your coordinates</span></p></body></html>", None))
        self.label.setText(_translate("widget", "Enter Coordinates Here :", None))
        self.b2.setText(_translate("widget", "START Your Game!", None))
        self.b1.setText(_translate("widget", "CLICK to get the coordinates", None))
        self.label1.setText(_translate("widget", "SciKit", None))
        self.label1_2.setText(_translate("widget", "Pl", None))
        self.label1_3.setText(_translate("widget", "ay", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    widget = QtGui.QWidget()
    ui = Ui_widget()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())

