# Crie um algoritmo que gere aleatoriamente um vetor com 20 posições entre 0 e 99. Depois mostre:
# a) A lista completa;
# b) A lista em ordem crescente;
# c) A lista me ordem decrescente.

import random

# Gera o vetor com 20 números aleatórios entre 0 e 99
vetor = [random.randint(0, 99) for _ in range(20)]

# a) Mostra a lista completa
print("a) Lista completa:")
print(vetor)

# b) Mostra a lista em ordem crescente
print("\nb) Lista em ordem crescente:")
print(sorted(vetor))

# c) Mostra a lista em ordem decrescente
print("\nc) Lista em ordem decrescente:")
print(sorted(vetor, reverse=True))