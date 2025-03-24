# Desenvolva um programa usando 'Break' que mostre natela a seguinte contagem: 100 95 90 85 80 75 70 65 60 55 50 45 40 35 30 25 20 15 10 5 0 FIM!

from time import sleep

print('Contagem regressiva para o lançamento do foguete:')
c = 100
while c >= 0:
    print(c)
    sleep(0.5)
    c -= 5
    if c == 0:
        print('FIM!')
        break
print('BOOM !')
