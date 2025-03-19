# Escreva um programa que leia o ano de nascimento de um rapaz e mostre a sua situação em relação ao alistamento militar.
# - Se estiver antes dos 18 anos, mostre em quantos anos faltam para o alistamento.
# - Se já tiver passado do tempo do alistamento, mostre quantos anos já se passaram do prazo.
# - Se estiver na idade do alistamento, mostre que é hora de se alistar. 

from datetime import date

ano_nascimento = int(input('Digite o ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento

if idade < 18:
    print(f'Faltam {18 - idade} anos para o alistamento.')
elif idade > 18:
    print(f'Já passaram {idade - 18} anos do prazo de alistamento.')
else:
    print('Está na hora de se alistar.')
