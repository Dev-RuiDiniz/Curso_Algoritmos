# Escreva um programa para aprovar um empréstimo bancário para compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input('Qual o valor da casa? R$ '))
salario = float(input('Qual o seu salário? R$ '))
anos = int(input('Em quantos anos você vai pagar? '))
prestacao = casa / (anos * 12)
if prestacao > salario * 0.3:
    print('Empréstimo negado!')
else:
    print(f'Para pagar uma casa de R$ {casa:.2f} em {anos} anos, a prestação será de R$ {prestacao:.2f}.')
    print('Empréstimo aprovado!')
    
