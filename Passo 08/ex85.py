# Faça um algoritmo que leia o nome, genero e o salario de 5 funcionarios e guardes nume tupla, depois em uma lista. No final mostre os dados apenas das mulheres que ganhem acima de r$5000,00.

# Cria lista para armazenar os funcionários
funcionarios = []

# Lê os dados dos 5 funcionários
for i in range(1, 6):
    print(f"\nCadastro do funcionário {i}:")
    nome = input("Nome: ")
    genero = input("Gênero (M/F): ").upper()
    salario = float(input("Salário R$: "))
    funcionarios.append((nome, genero, salario))  # Adiciona tupla à lista

# Filtra mulheres com salário acima de R$5.000,00
mulheres_acima_5000 = [func for func in funcionarios if func[1] == 'F' and func[2] >= 5000]

# Mostra os resultados
print("\nMulheres com salário acima de R$5.000,00:")
if mulheres_acima_5000:
    for func in mulheres_acima_5000:
        print(f"Nome: {func[0]}, Gênero: {func[1]}, Salário: R${func[2]:.2f}")
else:
    print("Não há mulheres com salário acima de R$5.000,00 na lista.")

# Mostra a lista completa (opcional)
print("\nLista completa de funcionários:")
for func in funcionarios:
    print(f"Nome: {func[0]}, Gênero: {func[1]}, Salário: R${func[2]:.2f}")