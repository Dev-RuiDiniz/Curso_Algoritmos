# Faça um programa que leia 7 números inteiros e no final mostre a soma entre eles.

soma = 0
for i in range(7):
    soma += int(input(f"Digite o {i + 1}º número: "))
print(f"A soma dos números é {soma}")

