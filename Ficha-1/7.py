def vencedor(C, Ce, Cs, Fv, Fe, Fs):
    pontos_cormengo = (int(C) * 3) + int(Ce)
    pontos_flaminthias = (int(Fv) * 3) + int(Fe)
    
    if pontos_cormengo > pontos_flaminthias:
        return "Cormengo"
    elif pontos_cormengo < pontos_flaminthias:
        return "Flaminthias"
    else:
        if int(Cs) == int(Fs):
            return "Empate"
        elif int(Cs) > int(Fs):
            return "Cormengo" 
        else:
            return "Flaminthias"

c = input("Informe o número de Vitórias do Cormengo: ")
ce = input("Informe o número de Empates do Cormengo: ")
cs = input("Informe o Saldo de gols do Cormengo: ")
fv = input("Informe o número de Vitórias do Flaminthias: ")
fe = input("Informe o número de Empates do Flaminthias: ")
fs = input("Informe o Saldo de gols do Flaminthias: ")
            
print(vencedor(c, ce, cs, fv, fe, fs))
