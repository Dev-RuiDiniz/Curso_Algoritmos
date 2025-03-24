# Crie um programa que leia o genero e o peso de 8 pessoas, usando 'Break'. No final, mostre:
# Quantas pessoas são do sexo masculino.
# Quantas pessoas pesam mais de 90kg.
# Quantos homens tem mais de 100kg.
# Quantas mulheres tem menos de 60kg.
# O maior peso entre os homens.

cont = 0
homens = 0
mais_90kg = 0
mais_100kg_homem = 0
mulheres_60kg = 0
homem_maior_peso = 0

while True:
    genero = input('Informe o gênero da pessoa [M/F]: ').strip().upper()
    peso = float(input('Informe o peso da pessoa: '))
    cont += 1
    if genero == 'M':
        homens += 1
        if peso > 100:
            mais_100kg_homem += 1
        if peso > homem_maior_peso:
            homem_maior_peso = peso
    if peso > 90:
        mais_90kg += 1
    if genero == 'F' and peso < 60:
        mulheres_60kg += 1
    if cont == 8:
        break   

print('-'*30)
print('Resultado da pesquisa:')    
print('-'*30)
print(f'Quantidade de pessoas do sexo masculino: {homens}')
print(f'Quantidade de pessoas com mais de 90kg: {mais_90kg}')
print(f'Quantidade de homens com mais de 100kg: {mais_100kg_homem}')
print(f'Quantidade de mulheres com menos de 60kg: {mulheres_60kg}')
print(f'Maior peso entre os homens: {homem_maior_peso}kg')
print('-'*30)
