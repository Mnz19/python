#importando a biblioteca math para utilar os comandos pow e sqrt
import math

#Função para achar as 2 raizes da função do segundo grau.
def funcaoSegundoGrau(a,b,c):
    delta = (pow(b,2)) - (4 * a * c)
    if delta < 0:
        return ("A equação não possui valores reais.")
    else:
        if delta == 0:
            x = -b/(2*a)
            return ("O resultado de delta é {}, logo a função terá apenas uma raiz que é {}".format(delta,x))
        else:
            x1 = (-b + math.sqrt(delta))/(2*a)
            x2 = (-b - math.sqrt(delta))/(2*a)
            return ("O resultado de delta é {}, logo a função terá duas raìzes que são {} e {} ".format(delta, x1, x2))

#Transformação para float / ENTRADA
a = float(input("Digite o valor do coeficiente a:"))
b = float(input("Digite o valor do coeficiente b:"))
c = float(input("Digite o valor do coeficiente c:"))

#SAIDA
print(funcaoSegundoGrau(a,b,c))
