# Desenvolva um algoritmo que moster uma contagem regressiva de 30 a 0, marcando em vermelho os numeros que forem divisiveis por 4.

from time import sleep
from termcolor import colored

for i in range(30, -1, -1):
    if i % 4 == 0:
        print(colored(i, 'red'))
    else:
        print(i)
    sleep(1)
print('Fim da contagem regressiva.')

