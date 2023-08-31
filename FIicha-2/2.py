def numero_sorte(idade):
    return (((((idade * 4) + 8)*60)/240) + 22) - idade

nome = input("Informe seu nome: ")
idade = int(input("Informe sua idade: "))

result = numero_sorte(idade)
print(f"Parabéns {nome}, seu numero da sorte é {result}")