# Uma locadora de carros precisa da sua ajuda para cobrar seus serviços. Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 90,00 por dia e R$ 0,20 por km rodado.  

km = float(input('Quantos km foram percorridos? '))
dias = int(input('Quantos dias o carro foi alugado? '))
preco = (km * 0.20) + (dias * 90)
print(f'O preço a pagar é R$ {preco:.2f}.')