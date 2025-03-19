# Crie um jogo de Jokenpô (Pedra, Papel e Tesoura)

from random import randint

print('Jokenpô')
print('1 - Pedra')
print('2 - Papel')
print('3 - Tesoura')

jogador = int(input('Escolha uma opção: '))
computador = randint(1, 3)

# Dicionário para mapear números às escolhas
opcoes = {1: 'Pedra', 2: 'Papel', 3: 'Tesoura'}

if jogador in opcoes:
    print(f'Jogador escolheu: {opcoes[jogador]}')
    print(f'Computador escolheu: {opcoes[computador]}')

    if jogador == computador:
        print('Empate')
    elif (jogador == 1 and computador == 3) or \
         (jogador == 2 and computador == 1) or \
         (jogador == 3 and computador == 2):
        print('Jogador venceu')
    else:
        print('Computador venceu')
else:
    print('Opção inválida')
