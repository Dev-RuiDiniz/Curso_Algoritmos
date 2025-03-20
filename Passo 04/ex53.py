# Faça um programa que leia a idade e o genero de 5 pessoas, mostrando no final:
# a) Quantos homens foram cadastrados
# b) Quantas mulheres foram cadastradas
# c) A média de idade do grupo
# d) A média de idade dos homens
# e) A média de idade das mulheres
# f) Quantas mulheres tem mais de 20 anos   

homens = 0
mulheres = 0
soma_idade = 0
soma_idade_homens = 0
soma_idade_mulheres = 0
mulheres_mais_20 = 0

for i in range(5):
    idade = int(input('Digite a idade: '))
    genero = input('Digite o genero (M/F): ').upper()

    soma_idade += idade

    if genero == 'M':
        homens += 1
        soma_idade_homens += idade
    elif genero == 'F':
        mulheres += 1
        soma_idade_mulheres += idade
        if idade > 20:
            mulheres_mais_20 += 1
            
media_idade = soma_idade / 5
media_idade_homens = soma_idade_homens / homens
media_idade_mulheres = soma_idade_mulheres / mulheres

print(f'Quantidade de homens: {homens}')
print(f'Quantidade de mulheres: {mulheres}')
print(f'Média de idade: {media_idade:.1f}')
print(f'Média de idade dos homens: {media_idade_homens:.1f}')
print(f'Média de idade das mulheres: {media_idade_mulheres:.1f}')
print(f'Quantidade de mulheres com mais de 20 anos: {mulheres_mais_20}')
