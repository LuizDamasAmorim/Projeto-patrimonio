from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
import sys

class Patrimonio(QWidget):
    def __init__(self):
        super().__init__()

        # Vamos configurar a geometria da tela. Setando os valores de posição X e Y, além de largura e altura

        self.setGeometry(10,30,400,300)

        # Texto para a barra de título
        self.setWindowTitle("Cadastro de equipamentos")

        # gerenciador de layout vertical
        self.layout_v = QVBoxLayout()


        # Labels para o ID do equipamento
        self.label_id = QLabel("Id do equipamento:")
        self.label_id.setStyleSheet("QLabel{font-size:12pt}")
        # Lineedit para o ID do equipamento
        self.edit_id = QLineEdit()
        self.edit_id.setStyleSheet("QLineEdit{font-size:12pt}")
        # Adicionar a label id e o lineedit ao layout vertical 
        self.layout_v.addWidget(self.label_id)
        self.layout_v.addWidget(self.edit_id)
        


        # Labels para o número de série 
        self.label_serie = QLabel("Número de série:")
        self.label_serie.setStyleSheet("QLabel{font-size:12pt}")
        # Lineedit para o número de série
        self.edit_serie = QLineEdit()
        self.edit_serie.setStyleSheet("QLineEdit{font-size:12pt}")
        # Adicionar a label serie e o lineedit ao layout vertical 
        self.layout_v.addWidget(self.label_serie)
        self.layout_v.addWidget(self.edit_serie)



        # Labels para o nome do cliente
        self.label_nome = QLabel("Nome do equipamento:")
        self.label_nome.setStyleSheet("QLabel{font-size:12pt}")
        # Lineedit para o nome do cliente
        self.edit_nome = QLineEdit()
        self.edit_nome.setStyleSheet("QLineEdit{font-size:12pt}")
        # Adicionar a label nome e o lineedit ao layout vertical 
        self.layout_v.addWidget(self.label_nome)
        self.layout_v.addWidget(self.edit_nome)



        # Labels para o tipo de produto
        self.label_tipo = QLabel("Tipo de produto:")
        self.label_tipo.setStyleSheet("QLabel{font-size:12pt}")
        # Lineedit para o tipo de produto
        self.edit_tipo = QLineEdit()
        self.edit_tipo.setStyleSheet("QLineEdit{font-size:12pt}")
        # Adicionar a label tipo e o lineedit ao layout vertical 
        self.layout_v.addWidget(self.label_tipo)
        self.layout_v.addWidget(self.edit_tipo)



        # Labels para a descrição do produto
        self.label_desc = QLabel("Descrição do produto:")
        self.label_desc.setStyleSheet("QLabel{font-size:12pt}")
        # Lineedit para a descrição do produto
        self.edit_desc = QLineEdit()
        self.edit_desc.setStyleSheet("QLineEdit{font-size:12pt}")
        # Adicionar a label desc e o lineedit ao layout vertical 
        self.layout_v.addWidget(self.label_desc)
        self.layout_v.addWidget(self.edit_desc)



        # Labels para a localização do produto
        self.label_local = QLabel("Localização do produto:")
        self.label_local.setStyleSheet("QLabel{font-size:12pt}")
        # Lineedit para a localização do produto
        self.edit_local = QLineEdit()
        self.edit_local.setStyleSheet("QLineEdit{font-size:12pt}")
        # Adicionar a label local e o lineedit ao layout vertical 
        self.layout_v.addWidget(self.label_local)
        self.layout_v.addWidget(self.edit_local)



        # Labels para a data de fabricação do produto
        self.label_dataf = QLabel("Data de fabricação do produto:")
        self.label_dataf.setStyleSheet("QLabel{font-size:12pt}")
        # Lineedit para a data de fabricação do produto
        self.edit_dataf = QLineEdit()
        self.edit_dataf.setStyleSheet("QLineEdit{font-size:12pt}")
        # Adicionar a label dataf e o lineedit ao layout vertical 
        self.layout_v.addWidget(self.label_dataf)
        self.layout_v.addWidget(self.edit_dataf)



        # Labels para a data de aquisição do produto
        self.label_dataq = QLabel("Data de aquisição do produto:")
        self.label_dataq.setStyleSheet("QLabel{font-size:12pt}")
        # Lineedit para a data de aquisição do produto
        self.edit_dataq = QLineEdit()
        self.edit_dataq.setStyleSheet("QLineEdit{font-size:12pt}")
        # Adicionar a label dataq e o lineedit ao layout vertical 
        self.layout_v.addWidget(self.label_dataq)
        self.layout_v.addWidget(self.edit_dataq)


# _______________________________________________________________________________________________________________________

        self.button = QPushButton("Cadastrar")
        self.button.setStyleSheet("QPushButton{background-color:black; color:white; font-size:12pt; font-weight:bold}")
        # Chamar a função de cadastro do cliente ao clicar no botão
        self.button.clicked.connect(self.cadastrar)


        # Adicionar a label cadastrar e o lineedit ao layout vertical
        self.layout_v.addWidget(self.button)

        # Adicionar layout_v a tela
        self.setLayout(self.layout_v)

    def cadastrar(self):
        if(self.edit_id.text()=="" or self.edit_serie.text()=="" or self.edit_nome.text()=="" or self.edit_tipo.text()=="" or self.edit_desc.text()=="" or self.edit_local.text()=="" or self.edit_dataf.text()=="" or self.edit_dataq.text()==""):
            QMessageBox.critical(self, "Erro", "Você deve preencher todos os campos")
        else:
        # Vamos criar uma variável que fará refêrencia a um arquivo de texto
            arquivo = open("patrimonio.csv", "+a", encoding="utf8") 
            arquivo.write(f"{self.edit_id.text()};")
            arquivo.write(f"{self.edit_serie.text()};")
            arquivo.write(f"{self.edit_nome.text()};")
            arquivo.write(f"{self.edit_tipo.text()};")
            arquivo.write(f"{self.edit_desc.text()};")
            arquivo.write(f"{self.edit_local.text()};")
            arquivo.write(f"{self.edit_dataf.text()};")
            arquivo.write(f"{self.edit_dataq.text()}\n")
            arquivo.close()

            #Exibe uma mensagem de aviso  
            QMessageBox.information(self,"Salvo","Os dados do patrimônio foram salvos",) #Da para colocar após isso com uma "," a parte de botões (quais botões aparecem na mensagem de aviso).
 

# app = QApplication(sys.argv)

# # Instância da classe CadastroCliente para iniciar a janela

# tela = Patrimonio()

# # Exibir a tela durante a execução 

# tela.show()

# # Ao clicar no botão fechar a tela deve fechar e sair da memória 

# app.exec()