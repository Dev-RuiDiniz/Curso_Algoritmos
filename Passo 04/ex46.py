# Crie um programa que calcule e mostre na tela a soma dos numeros pares dentro de um intervalo escolhido pelo usuario.
# Solicita ao usuário o valor inicial e final

# Solicita ao usuário o valor inicial
valor_inicial = int(input('Digite o valor inicial: '))
# Solicita ao usuário o valor final
valor_final = int(input('Digite o valor final: '))
# Inicializa a variável soma
soma = 0
# Percorre o intervalo de valores
for i in range(valor_inicial, valor_final + 1):
    # Verifica se o número é par
    if i % 2 == 0:
        # Soma o número
        soma += i
# Exibe a soma dos números pares
print(f'A soma dos números pares entre {valor_inicial} e {valor_final} é {soma}')
