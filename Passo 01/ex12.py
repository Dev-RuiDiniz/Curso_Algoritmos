# Crie um programa que leia o preço de um produto, calcule e mostre o seu Preço Promocional, com 5% de desconto.

# Solicita o preço do produto
preco = float(input("Digite o preço do produto: R$ "))

# Calcula o desconto de 5%
desconto = preco * 0.05
preco_promocional = preco - desconto

# Exibe o resultado
print(f"O preço original do produto é R${preco:.2f}")
print(f"Com 5% de desconto, o novo preço é R${preco_promocional:.2f}")
