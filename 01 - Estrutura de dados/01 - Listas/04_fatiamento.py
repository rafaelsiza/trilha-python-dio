lista = ["p", "y", "t", "h", "o", "n"]

print(lista[2:])  # ["t", "h", "o", "n"] # inicial a partir de 2; o "":"" indica até o final
print(lista[:2])  # ["p", "y"]  # no final vc sempre reduz por -1
print(lista[1:3])  # ["y", "t"]
print(lista[0:3:2])  # ["p", "t"] # inicial, por zero, poderia ser omitido; fui de 0 a 3, porem o item final diz para saltar de dois em dois. lembre-se sempre de abater -1 do final.
print(lista[::])  # ["p", "y", "t", "h", "o", "n"] # vazio-inicio vazio-fim copia exata da lista 
print(lista[::-1])  # ["n", "o", "h", "t", "y", "p"] #espelhar uma sequencia, vazio no inicio, no fim e -1 
