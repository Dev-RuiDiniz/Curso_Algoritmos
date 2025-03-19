# Escreva um sistema que leia uma distancia e metros e a converta para outras medidas

dist = float(input('Insira uma distancia (m): '))

print(f'A distancia {dist} corresponde a:\
    {dist/1000}km\
    {dist/100}hm\
    {dist/10}dam\
    {dist*10}dm\
    {dist*100}cm\
    {dist*1000}mm')
