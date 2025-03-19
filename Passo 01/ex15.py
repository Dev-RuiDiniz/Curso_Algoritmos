# Crie um programa que leia o número de dias trabalhados em um mês e mostre o sálario de um funcionario, sabendo que ele trabalha 8 horas por dia e ganha R$ 25,00 por hora trabalhada.

dias = int(input('Digite o número de dias trabalhados: '))
salario = 8 * 25 * dias 
print(f'O salário do funcionário neste mês é R$ {salario:.2f}.')