'''
Dicionários + Filtragem + Loops
Crie um programa que analise o dicionário abaixo e determine qual categoria é a mais
cara em média:
produtos = {
"Alimentação": [12.50, 8.99, 15.30],
"Limpeza": [5.20, 7.80],
"Higiene": [10.00, 12.00, 9.50, 14.00]
}
O programa deve exibir:
• categoria vencedora
• média formatada com 2 casas decimais
'''

# Dicionário de produtos e preços
produtos = {
    "Alimentação": [12.50, 8.99, 15.30],
    "Limpeza": [5.20, 7.80],
    "Higiene": [10.00, 12.00, 9.50, 14.00]
}

# Dicionário para armazenar a média dos preços por categoria
media_categorias = {}

# Calcula a média dos preços para cada categoria
for categoria, precos in produtos.items():
    media = sum(precos) / len(precos)
    media_categorias[categoria] = media

# Encontra a categoria com a maior média de preços
categoria_vencedora = max(media_categorias, key=media_categorias.get)
media_vencedora = media_categorias[categoria_vencedora]

# Exibe a categoria vencedora e sua média formatada com 2 casas decimais
print(f"Categoria vencedora: {categoria_vencedora}")
print(f"Média: {media_vencedora:.2f}")