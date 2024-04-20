pessoa = {"nome": "Guilherme", "idade": 28}
print(pessoa)

pessoa = dict(nome="Guilherme", idade=28)
print(pessoa)

pessoa["telefone"] = "3333-1234"  # {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}
print(pessoa)

familia = {"nome_pai":"Siza", "nome_mae": "Marta", "filho1":"Judah", "filho2":"Levi"}

print (familia["nome_pai"])

familia ["nome_pai"] = "Rafael Siza"

print (familia["nome_pai"])
