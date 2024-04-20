#qdo usar?
# quando eu quero criar uma nova lista com base na lista "mae". mas gostaria uma modificacao.


# Filtrar lista
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]  #primeira parte do comprehension é "numero" em sgeuida é a iteração/
print(pares)

# Modificar valores
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = [numero**2 for numero in numeros]
print(quadrado)
