# Faça um programa usando 'Break' que leia um numero inteiro e mostre na tela uma contagem ate o valor digitado começando de zero:

from time import sleep

c = 0   
x = int(input('Digite um número inteiro: '))
while True:
    print(c)
    sleep(0.5)
    c += 1
    if c == x+1:
        break
    
print('Fim da contagem!')
