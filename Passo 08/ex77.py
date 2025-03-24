# Faça um programa que leia o nome de 7 pessoas e guarde-os em um vetor. No final mostre a listagem inversa dos nomes colocados.

# Cria um vetor vazio para armazenar os nomes
nomes = []

# Lê os 7 nomes
for i in range(7):
    nome = input(f"Digite o nome da pessoa {i+1}: ")
    nomes.append(nome)
    
# lista invertida
print("\nLista completa invertida:", nomes[::-1])