def desconto(codigo, preco):
    codigo = str(codigo)
    if (codigo.endswith("00")):
        sale = preco*0.90
        return ("O produto ficará {}".format(sale))
    else: 
        return ("O produto ficará {}".format(preco))

codigo = str(input("Digite o codigo: "))
preco = float(input("preco: "))
print(codigo[-1])
print (desconto(codigo, preco))
