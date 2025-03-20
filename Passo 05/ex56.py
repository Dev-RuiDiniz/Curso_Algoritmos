# Crie um programa que leia vários numeros e no final mostre a somatoria entre eles. Se for digitado o valor 999 o programa deve parar e mostrar a somatoria sem o flag.

soma = 0
cont = 0
while True:
    num = int(input('Digite um número: '))
    if num == 999:
        break
    soma += num
    cont += 1
print(f'A soma dos {cont} números é {soma}.')
