# Faça um sistema que preencha 30 posiçoes de um vetor com numeros aleatorios entre 0 e 15. Depois disso peça para o usuario digitar um numero chave e o programa deve mostrar se esse numeros existe ou não e em quais posiçoes ele ocupa no vetor e quantas vezes ele aparece no vetor.

import random

# Preenche o vetor com 30 números aleatórios entre 0 e 15
vetor = [random.randint(0, 15) for _ in range(30)]

# Solicita o número chave ao usuário
numero_chave = int(input("\nDigite um número chave entre 0 e 15: "))

# Mostra o vetor gerado
print("Vetor gerado:")
print(vetor)

# Verifica se o número está no vetor
if numero_chave in vetor:
    # Encontra todas as posições onde o número aparece
    posicoes = [i for i, num in enumerate(vetor) if num == numero_chave]
    quantidade = len(posicoes)
    
    print(f"\nO número {numero_chave} foi encontrado no vetor.")
    print(f"Quantidade de vezes que aparece: {quantidade}")
    print(f"Posições onde aparece: {posicoes}")
else:
    print(f"\nO número {numero_chave} não foi encontrado no vetor.")