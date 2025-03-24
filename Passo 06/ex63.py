# Crie um programa usando 'While' que leia vários números. A cada laço, pergunte se o usúario quer continuar ou não. No final moste na tela:
# a) O somatorio de todos os valores digitados.
# b) A média dos valores digitados.
# c) O maior valor digitado.
# d) O menor valor digitado.
# e) A quantidade de números digitados.
# f) Quantos números são pares.
# g) Quantos números são ímpares.

from time import sleep

print('Digite vários números inteiros. Para encerrar digite 0.')
soma = 0
media = 0

maior = 0
menor = 0

qtd = 0
qtd_pares = 0
qtd_impares = 0

while True:
    num = int(input('Digite um número: '))
    if num == 0:
        break
    soma += num
    qtd += 1
    if num % 2 == 0:
        qtd_pares += 1
    else:
        qtd_impares += 1
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    media = soma / qtd
    print('Analisando...')
    sleep(1)
    
print(f'O somatório dos valores digitados é {soma}.')
print(f'A média dos valores digitados é {media:.2f}.')
print(f'O maior valor digitado foi {maior}.')
print(f'O menor valor digitado foi {menor}.')
print(f'Foram digitados {qtd} números.')
print(f'Foram digitados {qtd_pares} números pares.')
print(f'Foram digitados {qtd_impares} números ímpares.')
