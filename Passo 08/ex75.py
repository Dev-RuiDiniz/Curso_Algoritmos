# Crie um programa que preencha automaticamente um vetor numerico com 15 posiçoes com os primeiros 15 elementos da sequencia de fibonacci.

fibonacci = [0, 1]  # Inicia a sequência com os dois primeiros elementos

for i in range(2, 15):  # Começa do 2 porque já temos os dois primeiros
    proximo = fibonacci[i-1] + fibonacci[i-2]
    fibonacci.append(proximo)

print("Os 15 primeiros números de Fibonacci:")
print(fibonacci)