# Crie um algoritmo que leia o valor incial de uma contagem regressiva, o valor final e o incremento, mostrando em seguida todos os valores no intervalo. Exemplo: 2 100 2 (de 2 até 100, contando de 2 em 2).

valor_inicial = int(input('Digite o valor inicial: '))
valor_final = int(input('Digite o valor final: '))
incremento = int(input('Digite o incremento: '))
for i in range(valor_inicial, valor_final, +incremento):
    print(i, end=' ')
print('Acabou!')
    