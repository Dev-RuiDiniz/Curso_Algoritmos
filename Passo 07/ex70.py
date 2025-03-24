# Faça um programa que mostre os 10 primeiros termos da sequência de Fibonacci.

from time import sleep

print('Sequência de Fibonacci:')
n = 10
t1 = 0
t2 = 1
c = 3
print(f'{t1} -> {t2}', end=' -> ')
while c <= n:
    t3 = t1 + t2
    print(t3, end=' -> ')
    t1 = t2
    t2 = t3
    c += 1
    sleep(1)
print('FIM')
