# Desenvolva um lógica que leia os valores A, B e C de uma equação do segundo grau e mostre o valor de Delta.

# Solicita os coeficientes da equação
a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))

# Calcula o delta (Δ)
delta = b**2 - 4*a*c

# Exibe o resultado
print(f"O valor de Δ (delta) é {delta:.2f}")
