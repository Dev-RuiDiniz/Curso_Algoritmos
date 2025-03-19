# Uma empresa precisa reajustar o salário dos seus funcionarios, dando um aumento de acordo com alguns fatores. Faça um programa que leia o salário atual, o gênero do funcionário e há quantos anos ele trabalha na empresa. No final, mostre o seu novo salário, baseando-se na tabela a seguir:
# - Mulheres
#     - menos de 15 anos de empresa: +5%
#     - de 15 até 20 anos de empresa: +12%
#     - mais de 20 anos de empresa: +23%
# - Homens
#    - menos de 20 anos de empresa: +3%
#    - de 20 até 30 anos de empresa: +13%
#    - mais de 30 anos de empresa: +25%

salario = float(input('Digite o salário atual: '))
genero = input('Digite o gênero do funcionário (F/M): ').upper()
anos = int(input('Digite há quantos anos ele trabalha na empresa: '))
if genero == 'F':
    if anos < 15:
        salario += salario * 0.05
    elif anos < 20:
        salario += salario * 0.12
    else:
        salario += salario * 0.23
else:
    if anos < 20:
        salario += salario * 0.03
    elif anos < 30:
        salario += salario * 0.13
    else:
        salario += salario * 0.25
print(f'O novo salário será de R${salario:.2f}')
