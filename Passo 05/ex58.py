# Crie um programa que leia varias idades de alunos de uma turma. O programa vai parar quando digitas 999. No final mostre:
# quantos alunos tem na turma
# quantos são maiores de idade 
# quantos são menores de idade
# média de idade da turma.

print('Digite a idade dos alunos da turma. Para encerrar digite 999.')
idade = 0
maiores = 0
menores = 0
soma = 0
cont = 0
while idade != 999:
    idade = int(input('Digite a idade do aluno: '))
    if idade != 999:
        if idade >= 18:
            maiores += 1
        else:
            menores += 1
        soma += idade
        cont += 1
print(f'A turma tem {cont} alunos.')
print(f'{maiores} são maiores de idade.')
print(f'{menores} são menores de idade.')
print(f'A média de idade da turma é {soma / cont:.2f} anos.')
