'''
1. Listas + Compreensão de Listas + Condicionais
Dada uma lista de números inteiros, crie um programa que gere duas listas novas.
• uma contendo apenas os números primos
• outra contendo os números não primos
'''

# Lista de números inteiros
minha_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 17, 19, 20]

# Função para verificar primo
def verificar_primo(n):
    # Números menores que 2 (0, 1 e negativos) não são primos
    if n < 2:
        return False
    
    # Testar a divisão de 2 até o número anterior a n (n-1)
    for i in range(2, n):
        if n % i == 0:
            return False # Se for divisível, não é primo
            
    return True # Se passou pelo loop sem dividir por ninguém, é primo

# Cria listas dos primos e não primos
lista_primos = [num for num in minha_lista if verificar_primo(num)]
lista_nao_primos = [num for num in minha_lista if not verificar_primo(num)]

# Printar os resultados
print(f"Números: {minha_lista}")
print(f"Primos: {lista_primos}")
print(f"Não Primos: {lista_nao_primos}")