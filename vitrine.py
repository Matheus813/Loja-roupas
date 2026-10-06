# Etapa 2: os dados da loja em tipos e coleções (Aula 3)

# tupla: a lista de tamanhos não muda
TAMANHOS = ("PP", "P", "M", "G", "GG")

# lista de dicionários: um por produto
vitrine = [
    {"nome": "Camiseta básica", "preco": 39.90, "tamanhos": "M"},
    {"nome": "Calca jeans", "preco": 129.90, "tamanhos": "G"},
    {"nome": "Moleton", "preco": 159.90, "tamanhos": "P"},
]

# lista de pares (nome, quantidade)
carrinho = [("Camiseta básica", 3), ("Calca jeans", 1)]

# dicionário: nome -> preço

precos = {}
for produto in vitrine:
    precos[produto["nome"]] = produto["preco"]

total = 0
for nome, quantidade in carrinho: 
    total = total + precos[nome] * quantidade

print("peças na vitrine:", len(vitrine))
print("total do carrinho: R$", round(total, 2))

print(vitrine[1]["preco"])
print(TAMANHOS[-1])
print(len(carrinho))
print(precos["Moleton"] * 2)