'''
Biblioteca Externa (collections) + Contagem
Usando Counter da biblioteca collections, escreva um programa que receba uma frase do
usuário e exiba:
• o 3° caractere mais frequente
• e quantas vezes ele aparece
Caso hajam empates ou menos de 3 caracteres únicos, trate adequadamente com
mensagens claras.
'''

from collections import Counter
def terceiro_caractere_mais_frequente(frase):
    # Remove espaços e converte para minúsculas
    frase = frase.replace(" ", "").lower()
    
    # Conta a frequência de cada caractere
    contador = Counter(frase)
    
    # Obtém os caracteres mais comuns
    mais_comuns = contador.most_common()
    
    if len(mais_comuns) < 3:
        return "A frase não possui caracteres suficientes para determinar o 3° mais frequente."
    
    terceiro_caractere, frequencia = mais_comuns[2]
    return f"O 3° caractere mais frequente é '{terceiro_caractere}' que aparece {frequencia} vezes."

entrada_usuario = input("Digite uma frase: ")
resultado = terceiro_caractere_mais_frequente(entrada_usuario)
print(resultado)