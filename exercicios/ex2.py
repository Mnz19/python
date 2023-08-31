def frase(nome, idade):
    frase =  "Olá "+nome+", meu nome é python e eu tenho "+str(2 * idade)+" anos"
    return frase

nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

print(frase(nome, idade))
