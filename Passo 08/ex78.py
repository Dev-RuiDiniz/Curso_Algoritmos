# Escreva um programa que gere 15 numeros aleatorios, guarde-os em um vetor. No final mostre o vetor inteiro na tela e em seguida mostre em que posiçoes aparecem os valores multiplos de 10.

import random

# Gera 15 números aleatórios entre 0 e 100
numeros = [random.randint(0, 100) for _ in range(15)]

# Mostra o vetor completo
print("Vetor gerado:")
print(numeros)

# Encontra as posições dos múltiplos de 10
posicoes_multiplos_10 = [i for i, num in enumerate(numeros) if num % 10 == 0 and num != 0]

# Mostra os resultados
if posicoes_multiplos_10:
    print("\nMúltiplos de 10 aparecem nas posições:", posicoes_multiplos_10)
    print("Valores correspondentes:", [numeros[i] for i in posicoes_multiplos_10])
else:
    print("\nNão foram encontrados múltiplos de 10 no vetor.")