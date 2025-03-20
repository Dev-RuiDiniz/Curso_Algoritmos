# Desenvolva um aplicativo que leia o salario e o genero de varios funcionarios. O aplicativo deve perguntar ao usuario se deseja continuar. No final, o aplicativo deve exibir o salario total pago aos homens e as mulheres e media salarial dos homens e das mulheres.

salario_total_homens = 0
salario_total_mulheres = 0
quantidade_homens = 0
quantidade_mulheres = 0
continuar = True

while continuar:
    salario = float(input("Informe o salario: "))
    genero = input("Informe o genero (M/F): ")

    if genero.upper() == "M":
        salario_total_homens += salario
        quantidade_homens += 1
    elif genero.upper() == "F":
        salario_total_mulheres += salario
        quantidade_mulheres += 1
    else:
        print("Genero invalido!")
        
    continuar = input("Deseja continuar? (S/N): ").upper() == "S"
    
media_salarial_homens = salario_total_homens / quantidade_homens
media_salarial_mulheres = salario_total_mulheres / quantidade_mulheres

print(f"Salario total pago aos homens: {salario_total_homens:.2f}")
print(f"Salario total pago as mulheres: {salario_total_mulheres:.2f}")
print(f"Media salarial dos homens: {media_salarial_homens:.2f}")
print(f"Media salarial das mulheres: {media_salarial_mulheres:.2f}")