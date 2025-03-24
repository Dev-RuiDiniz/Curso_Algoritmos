# Crie um programa que leia a idade de 8 pessoas e guarde-as em um vetor. No final mostre:
# a) Qual é a média de idade das pessoas cadastradas;
# b) Em quais posiçoes temos pessoas com mais de 25 anos;
# c) Qual foi a maior idade registrada;
# d) Em que posição está a maior idade registrada.

# Cria um vetor para armazenar as idades
idades = []

# Lê as idades das 8 pessoas
for i in range(8):
    idade = int(input(f"Digite a idade da pessoa {i+1}: "))
    idades.append(idade)

print(idades)
# a) Calcula a média de idade
media = sum(idades) / len(idades)
print(f"\na) Média de idade: {media:.1f} anos")

# b) Encontra posições com idade > 25 anos
posicoes_mais_25 = [i for i, idade in enumerate(idades) if idade > 25]
if posicoes_mais_25:
    print(f"b) Posições com idade > 25 anos: {posicoes_mais_25}")
else:
    print("b) Não há pessoas com mais de 25 anos no grupo")

# c) Encontra a maior idade
maior_idade = max(idades)
print(f"c) Maior idade registrada: {maior_idade} anos")

# d) Encontra a posição da maior idade
posicao_maior = [i for i, idade in enumerate(idades) if idade == maior_idade]
print(f"d) Posição(ões) da maior idade: {posicao_maior}")