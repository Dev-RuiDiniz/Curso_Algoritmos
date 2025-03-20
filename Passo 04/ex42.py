# Faça um algoritmo que pergunte ao usuario um numero inteiro e positivo qualquer e mostre uma contagem até esse valor.
# ex: 1 2 3 4 ... 35 Acabou!

n = int(input('Digite um número inteiro e positivo: '))
for i in range(1, n+1):
    print(i, end=' ')
print('Acabou!')
