# Desenvolva um programa que leia o primeiro termo e a razão de uma PA (Progressão Aritmética) e mostre os 10 primeiros termos da PA e a soma de todos os valores da sequência.

# Importando a função sleep do módulo time
from time import sleep

print('Gerador de PA')
print('-=' * 10)
# Lendo o primeiro termo e a razão da PA
a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
# Inicializando o contador
c = 1
# Inicializando a soma
s = 0
# Inicializando o termo atual
an = a1
# Inicializando o número de termos
n = 10
while c <= n:
    print(f'{an}', end=' ')
    s += an
    an += r
    c += 1
    sleep(0.5)
print('FIM')
print(f'A soma dos termos é {s}')
