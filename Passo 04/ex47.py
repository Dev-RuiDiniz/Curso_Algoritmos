# Desenvolva um aprocativo que mostre na tela o resultado da expressa: soma de 0 a 500 de 50 em 50.
# A soma de 0 + 50 + 100 + 150 + 200 + 250 + 300 + 350 + 400 + 450 + 500 = 2750

soma = 0
for i in range(0, 501, 50):
    soma += i
print(f' A Soma é {soma}')

