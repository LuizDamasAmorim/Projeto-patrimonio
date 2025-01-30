import csv

# Abir o arquivo csv e atribuir a uma variável

arquivo = open("patrimonio.csv", "r",encoding="utf8")
linhas = csv.reader(arquivo)


for i in linhas:
    lin = str(i).replace("['","").replace("']","").split(";")

    if(lin[0]=="45"):
        print(lin)