def fatorial(n):
    if (n == 0):
        return 1
    else:
        return n * fatorial(n - 1)


print('CALCULO PARA FATORIAL')
n = int(input('Digite o numero: '))

resultado = fatorial(n)

print("O fatorial de {} é {}".format(n, resultado))

