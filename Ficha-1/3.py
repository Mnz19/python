#Função para repetir a palavra
def repetir_palavra(palavra):
    sequencia = palavra * 3
    return sequencia
#ENTRADA
entrada = input("Digite uma palavra: ")
#SAIDA
resultado = repetir_palavra(entrada)
print(resultado)
