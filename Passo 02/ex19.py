# Crie um algoritmo que leia o nome e duas notas de um aluno, calcule a média e mostre o resultado. No final. análise se a média é maior ou igual a 6.0 e mostre a mensagem "Aprovado", caso contrário "Reprovado".

nome = input('Digite o nome do aluno: ')
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2

if media >= 6:
    print(f'O aluno {nome} foi aprovado com média {media:.2f}')
else:
    print(f'O aluno {nome} foi reprovado com média {media:.2f}')
    