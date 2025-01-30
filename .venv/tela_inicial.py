import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from patrimonio import Patrimonio
from localizacao import Localizacao
from localizar_patrimonio import LocalizarPatrimonio


class TelaInicnial(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gerenciar")
        self.setGeometry(300,20,200,150)
        self.layout_v = QVBoxLayout()

        self.label_titulo = QLabel("Clique para abrir a janela")
        self.button = QPushButton("Abrir patrimônio")

        self.label_titulo2 = QLabel("Clique para abrir a localização")
        self.button2 = QPushButton("Abrir localização")

        self.label_titulo3 = QLabel("Clique abaixo para localizar")
        self.button3 = QPushButton("Localizar patrimônio")


        self.layout_v.addWidget(self.label_titulo)
        self.layout_v.addWidget(self.button)

        self.layout_v.addWidget(self.label_titulo2)
        self.layout_v.addWidget(self.button2)

        self.layout_v.addWidget(self.label_titulo3)
        self.layout_v.addWidget(self.button3)

        self.button.clicked.connect(self.abrir_cadastro)
        self.button2.clicked.connect(self.abrir_localizacao)
        self.button3.clicked.connect(self.abrir_localizar)

        self.setLayout(self.layout_v)
    
    def abrir_cadastro(self):
        self.pat = Patrimonio()
        self.pat.show()

    def abrir_localizacao(self):
        self.loc = Localizacao()
        self.loc.show()

    def abrir_localizar(self):
        self.locpatri = LocalizarPatrimonio()
        self.locpatri.show()

app = QApplication(sys.argv)
tela = TelaInicnial()
tela.show()
app.exec()
