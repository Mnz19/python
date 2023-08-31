def verificar(nome):
    qtd = len(nome)
    return ("O seu nome tem {} e começa com a letra {}".format(qtd, nome[0]))
nome = str(input("Digite seu nome: "))

print(verificar(nome))