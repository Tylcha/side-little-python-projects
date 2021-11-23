import sys,os
from PyQt5.QtWidgets import QWidget, QApplication, QTextEdit, \
    QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QFileDialog
from PyQt5.QtWidgets import QMainWindow, qApp ,QAction
class Notepad(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        menubar = self.menuBar()
        dosya = menubar.addMenu("File")
        duzenle = menubar.addMenu("Edit")

        ac = QAction("Open",self)
        ac.setShortcut("Ctrl+O") #kisayol tusu ation
        kaydet = QAction("Save",self)
        cikis = QAction("Exit",self)
        dosya.addAction(ac)
        dosya.addAction(kaydet)
        dosya.addAction(cikis)

        #ara_dug = menubar.addMenu("Search/Change")
        ara_dug = duzenle.addMenu("Search/Change")
        temizle = QAction("Clear",self)
        duzenle.addAction(temizle)
        ara = QAction("Search",self)
        degistir = QAction("Change",self)
        ara_dug.addAction(ara)
        ara_dug.addAction(degistir)

        cikis.triggered.connect(qApp.quit)
        dosya.triggered.connect(self.dosya_fonk)

        self.setWindowTitle("Menu Uygulamasi")
        self.show()
        
    def dosya_fonk(self,action):
        if action.text() =="Open":
            print("Dosya menusunde ac tiklandi")
        elif action.text() =="Save":
            print("Dosya menusunde kaydet tiklandi")
        elif action.text() =="Exit":
            print("Dosya menusunde cikis tiklandi")    

app = QApplication(sys.argv)
notepad = Notepad()
sys.exit(app.exec())