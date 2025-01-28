from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
import sys

class Localizacao(QWidget):
    def __init__(self):
        super().__init__()

        # Vamos configurar a geometria da tela. Setando os valores de posição X e Y, além de largura e altura

        self.setGeometry(10,30,400,300)

        # Texto para a barra de título
        self.setWindowTitle("Cadastro de equipamentos")

        # gerenciador de layout vertical
        self.layout_v = QVBoxLayout()


        #ID do equipamento
        self.label_id = QLabel("Id do equipamento:")
        self.label_id.setStyleSheet("QLabel{font-size:12pt}")
        self.edit_id = QLineEdit()
        self.edit_id.setStyleSheet("QLineEdit{font-size:12pt}")
        self.layout_v.addWidget(self.label_id)
        self.layout_v.addWidget(self.edit_id)
        


        #empresa
        self.label_empresa = QLabel("Nome da Empresa:")
        self.label_empresa.setStyleSheet("QLabel{font-size:12pt}")
        self.edit_empresa = QLineEdit()
        self.edit_empresa.setStyleSheet("QLineEdit{font-size:12pt}")
        self.layout_v.addWidget(self.label_empresa)
        self.layout_v.addWidget(self.edit_empresa)



        #logradouro
        self.label_logradouro = QLabel("Logradouro:")
        self.label_logradouro.setStyleSheet("QLabel{font-size:12pt}")
        self.edit_logradouro = QLineEdit()
        self.edit_logradouro.setStyleSheet("QLineEdit{font-size:12pt}")
        self.layout_v.addWidget(self.label_logradouro)
        self.layout_v.addWidget(self.edit_logradouro)



        #numero
        self.label_numero = QLabel("Número do equipamento:")
        self.label_numero.setStyleSheet("QLabel{font-size:12pt}")
        self.edit_numero = QLineEdit()
        self.edit_numero.setStyleSheet("QLineEdit{font-size:12pt}")
        self.layout_v.addWidget(self.label_numero)
        self.layout_v.addWidget(self.edit_numero)


        #predio
        self.label_predio = QLabel("Prédio:")
        self.label_predio.setStyleSheet("QLabel{font-size:12pt}")
        self.edit_predio = QLineEdit()
        self.edit_predio.setStyleSheet("QLineEdit{font-size:12pt}")
        self.layout_v.addWidget(self.label_predio)
        self.layout_v.addWidget(self.edit_predio)



        #andar
        self.label_andar = QLabel("Andar:")
        self.label_andar.setStyleSheet("QLabel{font-size:12pt}")
        self.edit_andar = QLineEdit()
        self.edit_andar.setStyleSheet("QLineEdit{font-size:12pt}")
        self.layout_v.addWidget(self.label_andar)
        self.layout_v.addWidget(self.edit_andar)


        #sala
        self.label_sala = QLabel("Sala do equipamento:")
        self.label_sala.setStyleSheet("QLabel{font-size:12pt}")
        self.edit_sala = QLineEdit()
        self.edit_sala.setStyleSheet("QLineEdit{font-size:12pt}")
        self.layout_v.addWidget(self.label_sala)
        self.layout_v.addWidget(self.edit_sala)


# _______________________________________________________________________________________________________________________

        self.button = QPushButton("Localizar")
        self.button.setStyleSheet("QPushButton{background-color:darkgreen; color:white; font-size:12pt; font-weight:bold}")
        # Chamar a função de cadastro do cliente ao clicar no botão
        self.button.clicked.connect(self.cadastrar)


        # Adicionar a label cadastrar e o lineedit ao layout vertical
        self.layout_v.addWidget(self.button)

        # Adicionar layout_v a tela
        self.setLayout(self.layout_v)

    def cadastrar(self):
        if(self.edit_id.text()=="" or self.edit_empresa.text()=="" or self.edit_logradouro.text()=="" or self.edit_numero.text()=="" or self.edit_predio.text()=="" or self.edit_andar.text()=="" or self.edit_sala.text()=="" ):
            QMessageBox.critical(self, "Erro", "Você deve preencher todos os campos")
        else:
            # Vamos criar uma variável que fará refêrencia a um arquivo de texto
            arquivo = open("localizacao.txt", "+a", encoding="utf8") 
            arquivo.write(f"ID: {self.edit_id.text()}\n")
            arquivo.write(f"Nome da Empresa: {self.edit_empresa.text()}\n")
            arquivo.write(f"Logradouro: {self.edit_logradouro.text()}\n")
            arquivo.write(f"Número do produto: {self.edit_numero.text()}\n")
            arquivo.write(f"Prédio: {self.edit_predio.text()}\n")
            arquivo.write(f"Andar: {self.edit_andar.text()}\n")
            arquivo.write(f"Sala do equipamento: {self.edit_sala.text()}\n")
            arquivo.write(f"-----------------------------------------\n")
            arquivo.close()

            #Exibe uma mensagem de aviso  
            QMessageBox.information(self,"Salvo","Os dados do patrimônio foram salvos",) #Da para colocar após isso com uma "," a parte de botões (quais botões aparecem na mensagem de aviso).

# app = QApplication(sys.argv)

# # Instância da classe CadastroCliente para iniciar a janela

# tela = Localizacao()

# # Exibir a tela durante a execução 

# tela.show()

# # Ao clicar no botão fechar a tela deve fechar e sair da memória 

# app.exec()