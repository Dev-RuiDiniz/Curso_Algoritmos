# uma empresa de aluguel de carros precisa cobrar pelos seus serviços. O aluguel de um carro custa R$ 90 por dia de um carro popular e R$ 150 por dia de um carro de luxo. Além disso, o cliente paga R$ 0,20 por quilômetro rodado até 100km e R$ 0,10 cada km adicional com um carro popular e R$ 0,30 por quilômetro rodado até 200 km e R$ 0,25 cada km adicional com um carro de luxo. Escreva um programa que leia o tipo de carro alugado (popular ou luxo), a quantidade de dias que o carro foi alugado e a quantidade de quilômetros rodados. O programa deve calcular o preço a pagar pelo aluguel do carro.
# Aluguel de carro popular: R$ 90 por dia + R$ 0,20 por km até 100km e R$ 0,10 por km adicional
# Aluguel de carro de luxo: R$ 150 por dia + R$ 0,30 por km até 200km e R$ 0,25 por km adicional

tipo = input('Qual o tipo de carro alugado (popular ou luxo)? ')
dias = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos quilômetros rodados? '))
if tipo == 'popular':
    preco = 90 * dias
    if km <= 100:
        preco += 0.20 * km
    else:
        preco += 0.20 * 100 + 0.10 * (km - 100)
else:
    preco = 150 * dias
    if km <= 200:
        preco += 0.30 * km
    else:
        preco += 0.30 * 200 + 0.25 * (km - 200)
print(f'O preço a pagar pelo aluguel do carro é R$ {preco:.2f}')
