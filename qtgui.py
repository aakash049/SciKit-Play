import  sys
import main
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PyQt4 import QtGui

class Window(QtGui.QMainWindow):
    def __init__(self):
        super(Window,self).__init__()
        self.setGeometry(900,100, 350,115)
        self.setWindowTitle("Scikit Bot")
        self.setWindowIcon(QtGui.QIcon('favicon.ico'))

        extractAction = QtGui.QAction("Quit", self)
        extractAction.setShortcut("Ctrl+Z")
        extractAction.setStatusTip('Leave the App')
        extractAction.triggered.connect(self.close_application)

        openEditor = QtGui.QAction("&Editor", self)
        openEditor.setShortcut("Ctrl+E")
        openEditor.setStatusTip('Open Editor')
        openEditor.triggered.connect(self.editor)

        openFile = QtGui.QAction("&Open Coordinates", self)
        openFile.setShortcut("Ctrl+O")
        openFile.setStatusTip('Open the coordinates of the board')
        openFile.triggered.connect(self.file_open)

        saveFile = QtGui.QAction("&Set Coordinates ", self)
        saveFile.setShortcut("Ctrl+S")
        saveFile.setStatusTip('Set the coordinates of the board')
        saveFile.triggered.connect(self.file_save)

        self.statusBar()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('Menu')
        fileMenu.addAction(extractAction)
        fileMenu.addAction(openFile)
        fileMenu.addAction(saveFile)
        
        editorMenu = mainMenu.addMenu("&Editor")
        editorMenu.addAction(openEditor)

        self.home()

    def home(self):
        btn = QtGui.QPushButton("Run Bot",self)
        btn.clicked.connect(self.call_main)
        btn.move(2,22)
        btn.resize(146,91)
        btn = QtGui.QPushButton("Play Candy Crush",self)
        btn.clicked.connect(self.open_game)
        btn.move(150, 22)
        btn.resize(146, 91)
        self.show()
		
    def file_open(self):
        #name = QtGui.QFileDialog.getOpenFileName(self, 'Open File')
        file = open('coord.py','r')
        self.editor()

        with file:
            text = file.read()
            self.textEdit.setText(text)

    def file_save(self):
        #name = QtGui.QFileDialog.getSaveFileName(self, 'Save File')
        file = open('coord.py','w')
        text = self.textEdit.toPlainText()
        file.write(text)
        file.close()
        self.textEdit.close()
		
    def editor(self):
        self.textEdit = QtGui.QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.textEdit.resize(350,100)

    def open_game(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--kiosk")
        options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
        browser = webdriver.Chrome(chrome_options=options)
        browser.get("http://www.royalgames.com/games/puzzle-games/candy-crush/?language=en_US&action=play")
        browser.execute_script("document.body.style.zoom='111%'")
        #browser.set_window_size(500, 500)
        #browser.maximize_window()


    def call_main(self):
        choice = QtGui.QMessageBox.question(self, 'Confirm Run', 'Are you sure you want to run the bot',
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            main.main()
        else:
            pass

    def close_application(self):
        choice = QtGui.QMessageBox.question(self, 'Confirm Exit', 'Are you sure you want to exit',
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            sys.exit()
        else:
            pass

def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

run()