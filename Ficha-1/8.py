def funcao(competidores, quantidadePapel, quantidadeFolhas):
        return "Suficiente" if quantidadePapel >= competidores * quantidadeFolhas else "Insuficiente"

qtd_competidores = int(input("Informe a quantidade de competidores: "))
qtd_papel =  int(input("Informe a quantidade oferecida pela diretoura: "))
qtd_folhas = int(input("Informe a quantidade sujerida por competidor: "))

print(funcao(qtd_competidores,qtd_papel,qtd_folhas))