# Escreva um programa que leia um numero qualquer e mostre na tela a sua tabuada, usando 'Break'.

from time import sleep

while True:
    n = int(input('Digite um número para ver sua tabuada: '))
    if n <= 0:
        break
    print('-' * 30)
    for c in range(1, 11):
        print(f'{n} x {c} = {n * c}')
        sleep(0.5)
    print('-' * 30)
print('Programa encerrado!')
print('FIM!')

