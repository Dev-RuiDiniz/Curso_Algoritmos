# Crie um algoritmo que leia a idade de 10 pessoas, mostrando no final:
# a) Quantas pessoas são maiores de idade;
# b) Quantas pessoas tem menos de 5 anos;
# c) Qual é a média de idade do grupo;
# d) Qual é a maior idade do grupo.

maiores_idade = 0
menores_5 = 0
total_idade = 0
maior_idade = 0
for i in range(10):
    idade = int(input('Digite a idade da pessoa: '))
    if idade >= 18:
        maiores_idade += 1
    if idade < 5:
        menores_5 += 1
    total_idade += idade
    if i == 0:
        maior_idade = idade
    else:
        if idade > maior_idade:
            maior_idade = idade
print(f'{maiores_idade} pessoas são maiores de idade.')
print(f'{menores_5} pessoas tem menos de 5 anos.')
print(f'A média de idade do grupo é {total_idade / 10:.2f}.')
print(f'A maior idade do grupo é {maior_idade}.')

