def verificar(num):
    if num == 0:
        return("{} é Igual a 0.".format(num))
    elif num > 0:
        return("{} é positivo.".format(num))
    elif num < 0:
        return("{} é negativo.".format(num))

num = int(input("Digite um numero: "))

print(verificar(num))