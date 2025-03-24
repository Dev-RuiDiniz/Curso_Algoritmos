# Crie um programa que leia o nome e a idade de 9 pessoas e guarde numa tupla e depois numa lista. No final mostre a lista completa e uma lista com apenas os nomes das pessoas menores de 18 anos.

# Cria lista para armazenar as pessoas
pessoas = []

# Lê os dados das 9 pessoas
for i in range(1, 10):
    print(f"\nCadastro da pessoa {i}:")
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    pessoas.append((nome, idade))  # Adiciona uma tupla (nome, idade) à lista

# Mostra a lista completa
print("\nLista completa de pessoas:")
for pessoa in pessoas:
    print(f"Nome: {pessoa[0]}, - Idade: {pessoa[1]}")

# Cria lista com nomes dos menores de 18 anos
menores = [pessoa[0] for pessoa in pessoas if pessoa[1] < 18]

# Mostra os nomes dos menores de 18 anos
print("Nomes dos menores de 18 anos:")
if menores:
    print(nome)
else:
    print("Não há menores de 18 anos na lista.")