# Faça um programa usando 'While' que leia a idade devarias pessoas. A cada laço, pergunte se o usuário quer continuar ou não. No final, mostre na tela:
# Quantas idades foram digitadas;
# A média entre as idades;
# Qual foi a maior idade digitada;
# Qual foi a menor idade digitada.
# Quantas pessoas tem mais de 18 anos.

from time import sleep

print('Análise de idades:')
c = 0
s = 0
maior = 0
menor = 0
mais18 = 0
continuar = 'S'
while continuar == 'S':
    idade = int(input('Digite a idade: '))
    c += 1
    s += idade
    if c == 1:
        maior = idade
        menor = idade
    else:
        if idade > maior:
            maior = idade
        if idade < menor:
            menor = idade
    if idade > 18:
        mais18 += 1
    continuar = input('Deseja continuar? [S/N]: ').upper().strip()
    
print(f'Foram digitadas {c} idades.')
print(f'A média entre as idades é {s/c:.2f}.')
print(f'A maior idade digitada foi {maior} anos.')
print(f'A menor idade digitada foi {menor} anos.')
print(f'{mais18} pessoas tem mais de 18 anos.')
print('Fim da análise.')
sleep(1)
print('FIM!')