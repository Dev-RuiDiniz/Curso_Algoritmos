# Faça um algoritmo que pergunte a distancia que um passageiro deseja percorrer em km. Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até 200 km, e R$ 0,45 para viagens mais longas.

distancia = float(input('Digite a distância que deseja percorrer em km: '))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print(f'O preço da passagem é R$ {preco:.2f}.')