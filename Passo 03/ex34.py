# O indice de Massa Corporal (IMC) é um valor calculado baseado na altura e peso de uma pessoa. Crie um programa que leia o peso e a altura do usuário e exiba o IMC do usuário e classifique o IMC de acordo com a tabela abaixo:
# IMC Classificação
# Menor que 18,5 Abaixo do peso
# 18,5 a 24,9 Peso normal
# 25,0 a 29,9 Sobrepeso
# 30,0 a 34,9 Obesidade grau 1
# 35,0 a 39,9 Obesidade grau 2
# 40,0 ou mais Obesidade grau 3
# IMC = peso / altura ** 2

peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))
imc = peso / altura ** 2

if imc < 18.5:
    print(f'O seu IMC é {imc:.2f} e você está abaixo do peso.')
elif 18.5 <= imc < 25:
    print(f'O seu IMC é {imc:.2f} e você está com o peso normal.')
elif 25 <= imc < 30:
    print(f'O seu IMC é {imc:.2f} e você está com sobrepeso.')
elif 30 <= imc < 35:
    print(f'O seu IMC é {imc:.2f} e você está com obesidade grau 1.')
elif 35 <= imc < 40:
    print(f'O seu IMC é {imc:.2f} e você está com obesidade grau 2.')
else:
    print(f'O seu IMC é {imc:.2f} e você está com obesidade grau 3.')
    