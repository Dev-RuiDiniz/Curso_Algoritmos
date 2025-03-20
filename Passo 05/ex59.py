# Crie um programa que leia o sexo e a idade de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) Qual a idade do homem mais velho.
# D) Qual a idade da mulher mais jovem.

maior18 = homens = idadehomem = idade = 0
mulherjovem = 999
sexo = ' '

while True:
    idade = int(input('Digite a idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
    if idade > 18:
        maior18 += 1
    if sexo == 'M':
        homens += 1
        if idade > idadehomem:
            idadehomem = idade
    if sexo == 'F':
        if idade < mulherjovem:
            mulherjovem = idade
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
    
print(f'{maior18} pessoas tem mais de 18 anos.')
print(f'{homens} homens foram cadastrados.')
print(f'A idade do homem mais velho é {idadehomem}.')
print(f'A idade da mulher mais jovem é {mulherjovem}.')
