# Escreva um programa para calcular a redução de tempo de vida de um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o total em dias.

cigarros = int(input('Quantos cigarros você fuma por dia? '))
anos = int(input('Há quantos anos você fuma? '))
dias = anos * 365
perda = cigarros * 10 * dias
perda = perda / 1440
print(f'Você perdeu {perda:.0f} dias de vida.')