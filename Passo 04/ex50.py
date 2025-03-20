# Desenvolva um programa que faça o sorteio de 20 numeros entre 0 e 10 e mostre na tela:
# a) quais foram os números sorteados;
# b) quantos números estão acima de 5;
# c) Quantos números são divisiveis por 3.

from random import randint
sorteados = []
acima5 = 0
div3 = 0
for i in range(20):
    num = randint(0, 10)
    sorteados.append(num)
    if num > 5:
        acima5 += 1
    if num % 3 == 0:
        div3 += 1
print(f'Os números sorteados foram: {sorteados}')
print(f'{acima5} números estão acima de 5.')
print(f'{div3} números são divisíveis por 3.')
