# Crie um programa que mostre na tela a seguinte contagem, usado uma estrutura 'While':
# 10 9 8 7 6 5 4 3 2 1 0 BOOM!

# Importando a função sleep do módulo time
from time import sleep

print('Contagem regressiva para o lançamento do foguete:')
c = 10
while c >= 0:
    print(c)
    sleep(1)
    c -= 1
print('BOOM!')
