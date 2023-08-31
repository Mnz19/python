def min_max(val1, val2):
    return min(val1, val2), max(val1, val2)

num1 = float(input("Informe o primeiro valor: "))
num2 = float(input("Informe o segundo valor: "))

minimo, maximo = min_max(num1, num2)
print(f"O valor mínimo é: {minimo}")
print(f"O valor máximo é: {maximo}")
