# Crie um algoritmo que leia a nota e o nome de 10 alunos e guarde-as em um vetor. No final, moster:
# a) Qual a Media da turma;
# b) Quantos alunos estão acima da media;
# c) Qual o nome e nota do aluno com maior nota;
# d) Em que posição a maior e a menos nota aparecem.

# Cria lista para armazenar os alunos (cada aluno é uma tupla (nome, nota))
turma = []

# Lê os dados dos 10 alunos
for i in range(10):
    nome = input(f"\nDigite o nome do aluno {i+1}: ")
    nota = float(input(f"Digite a nota do aluno {i+1}: "))
    turma.append((nome, nota))  # Adiciona uma tupla à lista

# Extrai as notas para cálculos
notas = [aluno[1] for aluno in turma]

# Mostra a lista completa da turma
print(turma)

# a) Calcula a média da turma
media = sum(notas) / len(notas)
print(f"\na) Média da turma: {media:.1f}")

# b) Conta alunos acima da média
acima_media = sum(1 for aluno in turma if aluno[1] > media)
print(f"b) Alunos acima da média: {acima_media}")

# c) Encontra aluno com maior nota
aluno_maior_nota = max(turma, key=lambda x: x[1])
print(f"c) Aluno com maior nota: {aluno_maior_nota[0]} (Nota: {aluno_maior_nota[1]:.1f})")

# d) Encontra posições da maior e menor nota
maior_nota = aluno_maior_nota[1]
menor_nota = min(notas)
pos_maior = [i for i, aluno in enumerate(turma) if aluno[1] == maior_nota]
pos_menor = [i for i, aluno in enumerate(turma) if aluno[1] == menor_nota]

print(f"d) Posição(ões) da maior nota: {pos_maior}")
print(f"   Posição(ões) da menor nota: {pos_menor}")