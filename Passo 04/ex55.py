#  Crie um jogo onde o computador vai sortear um número entre 1 e 10, o jogador vai tentar adivinhar qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o jogador venceu ou perdeu. O jogo continuará até o jogador acertar ou errar quatro vezes.
# O Programa vai mostrar um contador com a quantidade de tentativa restanta antes de cada tentativa.
# No final vai mostrar se o jogador falhou ou acertou e quantas tentativas foram necessárias.

from random import randint

print('Adivinhe o número')
print('O computador escolheu um número entre 1 e 10')

computador = randint(1, 10)
jogador = 0
tentativas = 0

while tentativas < 4:
    tentativas += 1
    print(f'Tentativa {tentativas}')
    jogador = int(input('Escolha um número: '))
    if jogador == computador:
        print('Parabéns! Você acertou.')
        print(f'Foram necessárias {tentativas} tentativas.')
        break
    else:
        print('Tente novamente.')
else:
    print(f'Você falhou. O número escolhido pelo computador foi {computador}.')
    