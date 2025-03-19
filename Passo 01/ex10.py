# faça um algoritmo que leia a largura e a altura de uma parede, calcule e mostre a área a ser pintada e a quantidade de tinta necessaria para o serviço, sabendo que cada litro de tinta pinta uma área de 2m².

larg = float(input('Insira a largura(m) da parede: '))
alt = float(input('Insira a altura(m) da parede: '))
area = larg * alt

print(f'Com base de área de {area}m² seram necessarios {area/2}lts de tinta para pintar a parede.')