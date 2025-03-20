# Desenvolva um aplicativo que leia o peso e altura de 7 pessoas, mostrando no final:
# a) Qual foi a média de altura do grupo
# b) Qual foi a média de peso do grupo
# c) Quantas pessoas pesam mais de 90kg
# d) Quantas pessoas pesam menos de 50kg e tem menos de 1.60cm de altura
# e) Quantas pessoas tem mais de 1.90cm de altura e pesam mais de 90kg

# Variables
height = 0
weight = 0
count = 0
count_weight = 0
count_height = 0
count_weight_height = 0

# Loop
for i in range(1, 8):
    height = float(input(f"Digite a altura da {i}ª pessoa(cm): "))
    weight = float(input(f"Digite o peso da {i}ª pessoa(kg): "))
    count += 1

    # Average height
    count_height += height

    # Average weight
    count_weight += weight

    # People with more than 90kg
    if weight > 90:
        count_weight_height += 1

    # People with less than 50kg and less than 1.60cm
    if weight < 50 and height < 160:
        count_weight += 1

    # People with more than 1.90cm and more than 90kg
    if height > 190 and weight > 90:
        count_weight_height += 1
        
# Results
print(f"A média de altura do grupo é: {count_height / count:.1f}")
print(f"A média de peso do grupo é: {count_weight / count:.1f}")
print(f"Quantidade de pessoas que pesam mais de 90kg: {count_weight_height:.1f}")
print(f"Quantidade de pessoas que pesam menos de 50kg e tem menos de 1.60cm de altura: {count_weight}")
print(f"Quantidade de pessoas que tem mais de 1.90cm de altura e pesam mais de 90kg: {count_weight_height}")