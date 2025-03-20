# Crie um programa que leia 6 numeros inteiros e no final mostre quantos deles são pares e quantos são impares.

pares = 0
impares = 0

for i in range(6):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
print(f'Você digitou {pares} números pares e {impares} números ímpares.')