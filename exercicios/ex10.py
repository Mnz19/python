def inverter(nome):
    return ("Seu nome invertido é {}".format(nome[::-1]))
nome = str(input("Digite uma palavra: "))

print(inverter(nome))