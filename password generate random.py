import random,string,sys
from PyQt5.QtWidgets import QApplication,QPushButton,QLabel,QVBoxLayout,QWidget

class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self): 
        self.etiket = QLabel("Sifreniz:")
        self.buton = QPushButton("Sifre Uret")

        v_box = QVBoxLayout()
        v_box.addWidget(self.buton)
        v_box.addWidget(self.etiket)

        self.buton.clicked.connect(self.sifre_uret)
        self.setLayout(v_box)
        self.show()
    
    def sifre_uret(self):
        self.sifre = ""
        self.yeni_sifre = ""
        rakamlar=string.digits
        semboller=string.punctuation
        kucuk_harfler=string.ascii_lowercase
        buyuk_harfler=string.ascii_uppercase
        tum_karakterler=[rakamlar, semboller, kucuk_harfler, buyuk_harfler]
        for j in range(4):
            for i in range(2):
                self.sifre+=tum_karakterler[j][random.randint(0, 9)]

        self.sifre=list(self.sifre)
        random.shuffle(self.sifre)
        print(self.sifre)

        self.yeni_sifre= ""
        for i in self.sifre:
            self.yeni_sifre+=i
            
        self.etiket.setText(f"Sifreniz:{self.yeni_sifre}")

app = QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec())