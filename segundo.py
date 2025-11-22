'''
Você recebe uma lista de tuplas contendo (nome, nota) de alunos.
Crie um programa que:
• transforme os dados em um dicionário
• se o aluno já existir, calcule a média das notas recebidas
• exiba os alunos em ordem crescente de média
Exemplo de entrada:
[("Ana", 8), ("João", 7), ("Ana", 10), ("Bia", 9)]
'''

# Lista de tuplas (nome, nota)
dados_alunos = [("Ana", 8), ("João", 7), ("Ana", 10), ("Bia", 9)]

# Dicionário para armazenar soma das notas e contagem de notas
notas_alunos = {}
for nome, nota in dados_alunos:
    if nome in notas_alunos:
        notas_alunos[nome]['soma'] += nota
        notas_alunos[nome]['contagem'] += 1
    else:
        notas_alunos[nome] = {'soma': nota, 'contagem': 1}

# Calcula a média das notas
media_alunos = {nome: info['soma'] / info['contagem'] for nome, info in notas_alunos.items()}

# Ordena os alunos pela média das notas
alunos_ordenados = dict(sorted(media_alunos.items(), key=lambda item: item[1]))

# Exibe os alunos em ordem crescente de média
for nome, media in alunos_ordenados.items():
    print(f"{nome}: {media:.2f}")