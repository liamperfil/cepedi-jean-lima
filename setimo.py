'''
Processamento de Dados com Loops + Dicionários Avançados
Receba uma lista de dicionários representando livros:
livros = [
{"titulo": "A", "ano": 2020, "preco": 45},
{"titulo": "B", "ano": 2024, "preco": 80},
{"titulo": "C", "ano": 2020, "preco": 50},
{"titulo": "D", "ano": 2022, "preco": 40}
]
Crie um programa que agrupe e mostre os livros por ano em ordem cronológica, exibindo
também o preço médio de cada ano.
'''

livros = [
    {"titulo": "A", "ano": 2020, "preco": 45},
    {"titulo": "B", "ano": 2024, "preco": 80},
    {"titulo": "C", "ano": 2020, "preco": 50},
    {"titulo": "D", "ano": 2022, "preco": 40}
]

# Cria dicionário onde a CHAVE será o Ano e o VALOR será uma Lista de Preços
livros_por_ano = {}

for livro in livros:
    ano_atual = livro["ano"]
    preco_atual = livro["preco"]
    
    # Se o ano ainda não está no dicionário, cria a chave com uma lista vazia
    if ano_atual not in livros_por_ano:
        livros_por_ano[ano_atual] = []
    
    # Adiciona o preço na lista daquele ano
    livros_por_ano[ano_atual].append(preco_atual)

# Organizar todas as chaves (anos) do menor para o maior
anos_ordenados = sorted(livros_por_ano.keys())

print("Preços por Ano:")

# Exibir Cálculo da Média
for ano in anos_ordenados:
    lista_de_precos = livros_por_ano[ano]
    
    # Cálculo da média: soma de todos os preços / quantidade de livros
    soma = sum(lista_de_precos)
    quantidade = len(lista_de_precos)
    media = soma / quantidade
    
    print(f"Ano: {ano} - Média de Preço: R$ {media:.2f}")