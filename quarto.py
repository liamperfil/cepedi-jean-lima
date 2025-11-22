'''
Listas + Loop + Operações Matemáticas
Implemente uma função que receba dois vetores (listas) de igual tamanho e retorne o
produto escalar entre eles, sem usar bibliotecas externas.
Exemplo:
A = [2, 3, 5]
B = [1, 4, 2]
→ Saída: 2*1 + 3*4 + 5*2 = 24
'''

def produto_escalar(lista_a, lista_b):
    # Variável para guardar a soma total
    total = 0
    
    # Tamanho da lista (quantos passos vamos dar)
    tamanho = len(lista_a)
    
    for i in range(tamanho):
        # Pega o número na posição 'i' da lista A
        valor_a = lista_a[i]
        
        # Pega o número na posição 'i' da lista B
        valor_b = lista_b[i]
        
        # Multiplica e soma ao total
        multiplicacao = valor_a * valor_b
        total = total + multiplicacao
        
    return total

A = [2, 3, 5]
B = [1, 4, 2]

resultado = produto_escalar(A, B)
print(f"O produto escalar é: {resultado}")