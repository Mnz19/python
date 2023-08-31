def meiaEntrada(idade, carteiraEstudante):
    if carteiraEstudante == True:
        return "Voce possui Meia entrada."
    else:
        if (idade <= 21) or (idade >= 65 ):
            return "Voce possui Meia entrada."
        else:
            return "Voce possui NÃO Meia entrada."
        
idade = int(input("Informe sua idade: "))
carteira = input("Possui carteira de estudante: [S/N] ").upper()
carteiraEstudante = True if carteira[0] == 'S' else  False

print(meiaEntrada(idade, carteiraEstudante))




