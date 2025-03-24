# Desenvolva um programa que gere aleatoriamente 10 numeros inteiros e guarde-os em um vetor. No final mostre o vetor completo e em que posição os numeros pares estão armazenados.

import random

# Gera 10 números inteiros aleatórios entre 0 e 50
numeros = [random.randint(0, 50) for _ in range(10)]

# Mostra o vetor completo
print("Vetor gerado:")
print(numeros)

# Encontra as posições dos números pares
posicoes_pares = [pos for pos, num in enumerate(numeros) if num % 2 == 0]

# Mostra os resultados
if posicoes_pares:
    print("\nNúmeros pares aparecem nas posições:", posicoes_pares)
    print("Valores pares correspondentes:", [numeros[pos] for pos in posicoes_pares])
else:
    print("\nNão foram encontrados números pares no vetor.")