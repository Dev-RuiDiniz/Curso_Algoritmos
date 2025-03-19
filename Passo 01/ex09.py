# Faça um algoritmo que leia um valor em real e diga quanto a pessoa possui em dolar. 1 Dolar = 5.95

num = float(input('Insira um valor(R$): '))
resp = num / 5.95

print(f'Com {num:.2f} você pode comprar ${resp:.2f} dolares.')