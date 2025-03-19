# Desenvolva um programa que leia o nome de um funcionario, seu salário, quantos anos ele trabalha na empresa e mostre seu novo salário, e mostre seu novo salário reajustando com os valores a seguir:
## Para quem tem até 3 anos de empresa: 3%
## Para quem tem mais de 3 e menos de 10 anos de empresa: 12.5%
## Para quem tem mais de 10 anos de empresa: 20%

nome = input('Digite o nome do funcionário: ')
salario = float(input('Digite o salário do funcionário: '))
anos = int(input('Digite quantos anos o funcionário trabalha na empresa: '))
if anos <= 3:
    salario += salario * 0.03
elif anos < 10:
    salario += salario * 0.125
else:
    salario += salario * 0.2
print(f'O novo salário de {nome} com base no seu tempo {anos} anos de empresa é R${salario:.2f}.')