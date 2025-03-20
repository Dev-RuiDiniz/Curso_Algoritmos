# Crie um algoritmo que leia o valor incial de uma contagem regressiva, o valor final e o incremento, mostrando em seguida todos os valores no intervalo. Exemplo: 2 100 2 (de 2 até 100, contando de 2 em 2).
# O programa acima vai ter um problema quando digitarmos o primeiro valor maior que o ultimo. Resolva esse problema com uma condicional.


valor_inicial = int(input('Digite o valor inicial: '))
valor_final = int(input('Digite o valor final: '))
incremento = int(input('Digite o incremento: '))

if valor_inicial > valor_final:
    for i in range(valor_inicial, valor_final, -incremento):
        print(i, end=' ')
    print('Acabou!')
else:
    for i in range(valor_inicial, valor_final, +incremento):
        print(i, end=' ')
    print('Acabou!')