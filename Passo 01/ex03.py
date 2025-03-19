# Crie um programa que leia o nome e o salário de um funcionario, mostrando no final uma mensagem.

nome = str(input('Insira seu nome: '))
salario = float(input('Insira seu salário: '))

print(f'o funcionario {nome} tem um salário de R${salario:.2f} atualmente.')