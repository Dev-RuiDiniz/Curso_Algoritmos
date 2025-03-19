# Crie um programa que leia o tamanho de três segmentos de reta. Analise seus comprimentos e diga se é possível formar um triângulo com essas retas.

print('Digite o tamanho de três segmentos de reta: ')
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a < b + c and b < a + c and c < a + b:
    print('É possível formar um triângulo com esses segmentos de reta.')
else:
    print('Não é possível formar um triângulo com esses segmentos de reta.')