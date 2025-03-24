# Crie um programa que preencha automaticamente um vetor numerico com 10 posições: 5, 3, 5, 3, 5, 3, 5, 3, 5, 3.

vetor1 = []
for i in range(10):
    if i % 2 == 0:  # Posições pares (0, 2, 4...)
        vetor1.append(5)
    else:           # Posições ímpares (1, 3, 5...)
        vetor1.append(3)
print("Vetor alternado: ", vetor1)