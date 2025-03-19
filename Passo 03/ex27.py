# Crie um programa que leia duas notas de um aluno, calcule a média e mostre na tela uma mensagem:
# - Aprovado (média >= 7)
# - Recuperação (média >= 5 e < 7)
# - Reprovado (média < 5)

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
if media >= 7:
    print('Aprovado')
elif media >= 5:
    print('Recuperação')
else:
    print('Reprovado')
