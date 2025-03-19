# Faça um programa que leia o ano de nascimento de um pessoa, calcule a idade dela e mostre se ela já pode ou não votar.

from datetime import date

ano_nascimento = int(input('Digite o ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento

if idade < 16:
    print(f'Com {idade} anos, você não pode votar.')
elif 16 <= idade < 18 or idade > 70:
    print(f'Com {idade} anos, o voto é opcional.')
else:
    print(f'Com {idade} anos, o voto é obrigatório.')
    