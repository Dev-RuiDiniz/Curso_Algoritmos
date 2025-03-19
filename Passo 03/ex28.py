# Faça um programa que leia a largura e o comprimento de um terreno retangular, calculando e mostrando a sua área em metros quadrados. O programa tambem deve mostrar a classificação desse terreno, de acordo com a tabela abaixo:
# Área menor que 100 metros quadrados: TERRENO POPULAR
# Área entre 100 e 500 metros quadrados: TERRENO MASTER
# Área maior que 500 metros quadrados: TERRENO VIP

largura = float(input('Digite a largura do terreno: '))
comprimento = float(input('Digite o comprimento do terreno: '))
area = largura * comprimento

if area < 100:
    print(f'Seu terreno com {area}m² é um TERRENO POPULAR.')
elif area <= 500:
    print(f'Seu terreno com {area}m² é um TERRENO MASTER.')
else:
    print(f'Seu terreno com {area}m² é um TERRENO VIP.')
