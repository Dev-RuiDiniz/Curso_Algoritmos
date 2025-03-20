# Faça um aplicativo que leia o preço de 8 produtos. No final, mostre na tela:
# a) Qual é o total gasto na compra;
# b) Qual foi o produto mais barato;
# c) Qual foi o produto mais caro.

total = 0
mais_barato = 0
mais_caro = 0
for i in range(8):
    preco = float(input('Digite o preço do produto: '))
    total += preco
    if i == 0:
        mais_barato = preco
        mais_caro = preco
    else:
        if preco < mais_barato:
            mais_barato = preco
        if preco > mais_caro:
            mais_caro = preco
print(f'O total gasto na compra foi R${total:.2f}.')
print(f'O produto mais barato custou R${mais_barato:.2f}.')
print(f'O produto mais caro custou R${mais_caro:.2f}.')
