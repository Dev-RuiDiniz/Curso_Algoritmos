# Crie um programa que preencha automaticamente um vetor com 7 numeros gerados aleatoriamente e depois mostre na tela.

import random

# Gera 7 números entre 0 e 50
personalizados = [random.randint(0, 50) for _ in range(7)]
print("Números:", personalizados)