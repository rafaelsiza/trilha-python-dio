carros = ["gol", "celta", "palio"]

for carro in carros:
    print(carro)


for indice, carro in enumerate(carros):    #para saber o indice dentro da interacao. o enumerate retorna dois valores: 1 o contador (que comeca em zero) e outro o item da iteracao.
    print(f"{indice}: {carro}")
