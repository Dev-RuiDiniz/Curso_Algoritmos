# Nume promoção exclusiva para o dia da mulher, uma loja quer dar descontos para todos, mas especialmente para mulheres. Faça um programa que leia o nome do cliente, seu genero e o valor da compra e informe o valor do desconto. O desconto para homens é de 5% e para mulheres é de 13%.   

nome = input("Digite o nome do cliente: ")
genero = input("Digite o genero do cliente (M/F): ").upper()
valor = float(input("Digite o valor da compra: ")) 
if genero == "M":
    desconto = valor * 0.05
else:
    desconto = valor * 0.13
valor_compra = valor - desconto
print(f"O valor da compra para o cliente {nome} é de R${valor_compra:.2f}.")
