from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox 
import sys
import csv

class LocalizarPatrimonio(QWidget):
    def __init__(self):
        super().__init__()

        # Vamos configurar a geometria da tela. 
        # Setando os valores de posição x e y,
        # Além de largura
        self.setGeometry(10, 30, 400, 300) # Fazendo o tamanho da Janela

        # Texto para a barra de título
        self.setWindowTitle("Cadastro de equipamentos")

        # Gerenciador de layout vertical
        self.layout_v = QVBoxLayout()

        # ID
        # Labels para os id dos produtos
        self.label_id = QLabel("Id do equipamento")
        self.label_id.setStyleSheet("QLabel{font-size:12pt}")

        # LineEdit para o id do cliente
        self.edit_id = QLineEdit()
        self.edit_id.setStyleSheet("QLineEdit{font-size:12pt}")

        # Adicionar o label id e o lineedit ao layout vertical
        self.layout_v.addWidget(self.label_id)
        self.layout_v.addWidget(self.edit_id)
        self.btnbuscar = QPushButton('Buscar patrimonio')
        self.layout_v.addWidget(self.btnbuscar)
        self.btnbuscar.clicked.connect(self.localizar)

        # Número de serie
        # Labels para o número de serie do produto
        self.label_serie = QLabel("Número de série: ")
        self.label_serie.setStyleSheet("QLabel{font-size:12pt}")

        # LineEdit para o número de serie do produto
        self.edit_serie = QLineEdit()
        self.edit_serie.setStyleSheet("QLineEdit{font-size:12pt}")

        # Adicionar o label número de serie e o lineedit ao layout vertical
        self.layout_v.addWidget(self.label_serie)
        self.layout_v.addWidget(self.edit_serie)

        # Nome
        # Labels para o nome do equipamento
        self.label_nome = QLabel("Nome do equipamento: ")
        self.label_nome.setStyleSheet("QLabel{font-size:12pt}")

        # LineEdit para o nome do equipamento
        self.edit_nome = QLineEdit()
        self.edit_nome.setStyleSheet("QLineEdit{font-size:12pt}")

        # Adicionar o label nome do equipamento e o lineedit ao layout vertical
        self.layout_v.addWidget(self.label_nome)
        self.layout_v.addWidget(self.edit_nome)

        # Tipo de produto
        # Labels para o Idade do cliente
        self.label_tipo = QLabel("Tipo de produto: ")
        self.label_tipo.setStyleSheet("QLabel{font-size:12pt}")

        # LineEdit para o tipo de produto
        self.edit_tipo = QLineEdit()
        self.edit_tipo.setStyleSheet("QLineEdit{font-size:12pt}")

        # Adicionar o label tipo e o lineedit ao layout vertical
        self.layout_v.addWidget(self.label_tipo)
        self.layout_v.addWidget(self.edit_tipo)

        # Descrição do produto
        # Labels para o Idade do cliente
        self.label_desc = QLabel("Descrição do produto: ")
        self.label_desc.setStyleSheet("QLabel{font-size:12pt}")

        # LineEdit para o descrição de produto
        self.edit_desc = QLineEdit()
        self.edit_desc.setStyleSheet("QLineEdit{font-size:12pt}")

        # Adicionar o label descrição e o lineedit ao layout vertical
        self.layout_v.addWidget(self.label_desc)
        self.layout_v.addWidget(self.edit_desc)

        # Localização do produto
        # Labels para o Idade do cliente
        self.label_local = QLabel("Localização do produto: ")
        self.label_local.setStyleSheet("QLabel{font-size:12pt}")

        # LineEdit para o localização de produto
        self.edit_local = QLineEdit()
        self.edit_local.setStyleSheet("QLineEdit{font-size:12pt}")

        # Adicionar o label local e o lineedit ao layout vertical
        self.layout_v.addWidget(self.label_local)
        self.layout_v.addWidget(self.edit_local)

        # Data de fabricação
        # Labels para o data de fabricação
        self.label_dataf = QLabel("Data de fabricação: ")
        self.label_dataf.setStyleSheet("QLabel{font-size:12pt}")

        # LineEdit para o data de fabricação
        self.edit_dataf = QLineEdit()
        self.edit_dataf.setStyleSheet("QLineEdit{font-size:12pt}")

        # Adicionar o label data e o lineedit ao layout vertical
        self.layout_v.addWidget(self.label_dataf)
        self.layout_v.addWidget(self.edit_dataf)

        # Data de aquisição
        # Labels para o data de aquisição
        self.label_dataq = QLabel("Data de aquisição: ")
        self.label_dataq.setStyleSheet("QLabel{font-size:12pt}")

        # LineEdit para data de aquisição
        self.edit_dataq = QLineEdit()
        self.edit_dataq.setStyleSheet("QLineEdit{font-size:12pt}")

        # Adicionar o label data e o lineedit ao layout vertical
        self.layout_v.addWidget(self.label_dataq)
        self.layout_v.addWidget(self.edit_dataq)

        # Adicionanado o layout na tela
        self.setLayout(self.layout_v)

    def localizar(self):
        # Abrir o arquivo csv e atribuir a uma variável
        arquivo = open("patrimonio.csv","r",encoding="utf-8")
        linhas = csv.reader(arquivo) # essa linha serve para ler o que está dentro do arquivo

        for i in linhas:
            lin = str(i).replace("['","").replace("']","").split(";")
            if(lin[0] == self.edit_id.text()):
                self.edit_serie.setText(lin[1])
                self.edit_nome.setText(lin[2])
                self.edit_tipo.setText(lin[3])
                self.edit_desc.setText(lin[4])
                self.edit_local.setText(lin[5])
                self.edit_dataf.setText(lin[6])
                self.edit_dataq.setText(lin[7])



# app = QApplication(sys.argv)
# # Instância da classe CadastroCliente para inicializar a janela
# tela = Patrimonio()
# # Exibir a tela durante a execução
# tela.show()
# # Ao clicar no botão fechar a janela deve fechar e sair da memoria
# app.exec()