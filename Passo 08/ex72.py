# Crie um programa que preencha automaticamente um vetor numéricos com 10 posiçoes usando logica, com os seguintes valores: 5, 10, 15, 20, 25, 30, 35, 40, 45, 50.

vetor = []
for i in range(1, 11):
    vetor.append(i * 5)
print("Vetor preenchido:", vetor)