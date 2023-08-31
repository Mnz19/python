import datetime

def dataNascimento(dia, mes, ano):
    idade = datetime.datetime.now().year - ano
    if datetime.datetime.now().day == dia and datetime.datetime.now().month == mes:
        return ("Feliz {} anos de vida!".format(idade))
    else:
        return("Você tem {} anos".format(idade))

dia = int(input("DIA: "))
mes = int(input("MES: "))
ano = int(input("ANO: "))

print(dataNascimento(dia,mes,ano))