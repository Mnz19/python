def substituição_caracter(s, x, i):
    if i < 0 or i >= len(s):
        return "O índice fornecido está fora dos limites da string."
    
    nova_str = s[:i] + x + s[i+1:]
    return nova_str

string = input("Digite a string: ")
caracter = input("Digite o caractere de substituição: ")
i = int(input("Digite o índice (entre 0 e o comprimento da string - 1): "))

result = substituição_caracter(string, caracter, i)
print("Nova string após a substituição:", result)
