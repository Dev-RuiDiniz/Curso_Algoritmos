# Desenvolva um programa usando 'Break' que mostre natela a seguinte contagem: 0 5 10 15 20 25 30 35 40 45 50 55 60 65 70 75 80 85 90 95 100 FIM!

from time import sleep

print('Contagem de 0 a 100 de 5 em 5:')
c = 0
while c <= 100:
    print(c)
    sleep(0.5)
    c += 5
    if c > 100:
        break
print('FIM!')
