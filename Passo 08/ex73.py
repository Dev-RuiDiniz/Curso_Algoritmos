# Crie um programa que preencha automaticamente um vetor númerico com 10 posiçoes: 9, 8, 7, 6, 5, 4, 3, 2, 1, 0.

vetor1 = []
for i in range(9, -1, -1):  # Começa em 9, vai até 0 (não incluso -1), passo -1
    vetor1.append(i)
print("Vetor decrescente:", vetor1)