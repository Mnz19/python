def soma(x,y):
    string = "A soma entre "+str(x)+ " e "+str(y) + " é"
    result = x + y
    return ("{} {}".format(string, result))

x = int(input("n1: "))
y = int(input("n1: "))

print(soma(x,y))


