def concatenar(a, b):
    return a[5::] + b[:5:]

a = input("Digite uma palavra: ")
b = input("Digite outra palavra: ")

while len(a) < 15 or len(b) < 15:
    if len(a) < 15:
        a = input("Digite a primeira palavra novamente: ")
    else:
        b = input("Digite a segunda palavra novamente: ")
        
print(concatenar(a,b))