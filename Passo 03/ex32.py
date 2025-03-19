# Crie um jogo onde o computador vai sortear um número entre 1 e 5, o jogador vai tentar adivinhar qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o jogador venceu ou perdeu. O jogo continuará até o jogador acertar o número escolhido pelo computador.

from random import randint

print('Adivinhe o número')
print('O computador escolheu um número entre 1 e 5')

computador = randint(1, 5)
jogador = 0

while jogador != computador:
    jogador = int(input('Escolha um número: '))
    if jogador == computador:
        print('Parabéns! Você acertou.')
    else:
        print('Tente novamente.')
