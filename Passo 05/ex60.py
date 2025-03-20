# Desenvolva um algoritmo que leia o nome e o genero de varias pessoas. O programa vai perguntar se o usuario quer ou nao continuar. No final, mostre:
# a) O nome da pessoa mais velha
# b) O nome da mulher mais jovem
# c) A media de idade do grupo
# d) Quantos homens tem mais de 30 anos
# e) Quantas mulheres tem menos de 18 anos

# Inicialização de variáveis
nome = ''
genero = ''
idade = 0
mais_velho = 0
mais_velho_nome = ''
mulher_mais_jovem = 0
mulher_mais_jovem_nome = ''
media_idade = 0
media_idade_total = 0
homens_mais_30 = 0
mulheres_menos_18 = 0
contador = 0

# Início do loop

while True:
    nome = input('Digite o nome: ')
    genero = input('Digite o genero (M/F): ').upper()
    idade = int(input('Digite a idade: '))

    if idade > mais_velho:
        mais_velho = idade
        mais_velho_nome = nome

    if genero == 'F' and idade < mulher_mais_jovem:
        mulher_mais_jovem = idade
        mulher_mais_jovem_nome = nome

    media_idade_total += idade

    if genero == 'M' and idade > 30:
        homens_mais_30 += 1

    if genero == 'F' and idade < 18:
        mulheres_menos_18 += 1

    contador += 1

    continuar = input('Deseja continuar? (S/N) ').upper()
    if continuar == 'N':
        break
    
media_idade = media_idade_total / contador

print(f'O nome da pessoa mais velha é {mais_velho_nome}')
print(f'O nome da mulher mais jovem é {mulher_mais_jovem_nome}')
print(f'A média de idade do grupo é {media_idade}')
print(f'Quantidade de homens com mais de 30 anos: {homens_mais_30}')
print(f'Quantidade de mulheres com menos de 18 anos: {mulheres_menos_18}')