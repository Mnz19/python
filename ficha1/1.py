#Função para retornar o valor absoluto
def valorAbsoluto(n):
    if n < 0:
        n = n*(-1)
    return n 
#Conversão para float / ENTTRADA
number = float(input("Digite um numero: "))
#SAIDA
print(valorAbsoluto(number))
