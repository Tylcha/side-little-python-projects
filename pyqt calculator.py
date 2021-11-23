#clicced connect calismio aq
import sys
from PyQt6 import QtWidgets

class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.sayi1 = 0
        self.sayi2 = 0
        self.sayi3 = 0
        self.islem = ""
        self.hata = ""
        
    def init_ui(self):
        self.line_etiket = QtWidgets.QLineEdit()
        self.buton_arti = QtWidgets.QPushButton("+")
        self.buton_eksi = QtWidgets.QPushButton("-")
        self.buton_bolu = QtWidgets.QPushButton("/")
        self.buton_carpma = QtWidgets.QPushButton("*")
        self.buton_esit = QtWidgets.QPushButton("=")
        self.line_etiket_tire = QtWidgets.QLabel("----------")

        h_box1 = QtWidgets.QHBoxLayout()
        h_box1.addWidget(self.buton_arti)
        h_box1.addWidget(self.buton_eksi)

        h_box2 = QtWidgets.QHBoxLayout()
        h_box2.addWidget(self.buton_carpma)
        h_box2.addWidget(self.buton_bolu)

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.line_etiket)
        v_box.addLayout(h_box1)
        v_box.addLayout(h_box2)
        v_box.addWidget(self.buton_esit)
        v_box.addStretch()
        v_box.addWidget(self.line_etiket_tire)

        self.buton_arti.clicked.connect(self.tikla)
        self.buton_eksi.clicked.connect(self.tikla)
        self.buton_carpma.clicked.connect(self.tikla)
        self.buton_bolu.clicked.connect(self.tikla)
        self.buton_esit.clicked.connect(self.tikla)

        self.setLayout(v_box)
        self.show()
        
    def tikla(self):
        gonderen = self.sender()
        if (gonderen.text() != "="):
            self.islem = gonderen.text()
            self.sayi1 = int(self.line_etiket.text())
            self.line_etiket_tire.setText(str(self.sayi1) + self.islem)
            self.line_etiket.setText("0")
        else:
            self.sayi2 = int(self.line_etiket.text())

            if self.islem == "+":
                self.sayi3 = self.sayi1 + self.sayi2
                self.hata = ""
            elif self.islem == "-":
                self.sayi3 = self.sayi1 - self.sayi2
                self.hata = ""
            elif self.islem == "*":
                self.sayi3 = self.sayi1 * self.sayi2
                self.hata = ""
            elif self.islem == "/":
                if self.sayi2 ==0:
                    self.hata = "Sifira bolme islemi yapilamaz"
                else:
                    self.sayi3 = self.sayi1 / self.sayi2
                    self.hata = ""

            if self.hata != "":
                self.line_etiket_tire.setText(self.hata)
            else:
                self.line_etiket_tire.setText(f"{self.sayi1}{self.islem}{self.sayi2}={self.sayi3}")
                self.line_etiket.setText(str(self.sayi3))

        

app = QtWidgets.QApplication(sys.argv)
pencere = Pencere()
pencere.setWindowTitle("Hesap Makinesi")
sys.exit(app.exec())