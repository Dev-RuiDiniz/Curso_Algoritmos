# Crie uma função que se chamara Media( ), ela vai receber duas notas dos alunos e retornar a media ao programa principal.

def Media(*notas):
    """Calcula a média de quantas notas forem informadas"""
    return sum(notas) / len(notas)

# Uso:
notas = []
while len(notas) < 2:  # Pede pelo menos 2 notas
    try:
        nota = float(input(f"Digite a {len(notas)+1}ª nota: "))
        if 0 <= nota <= 10:
            notas.append(nota)
        else:
            print("Nota deve estar entre 0 e 10!")
    except ValueError:
        print("Digite apenas números!")

media = Media(*notas)
print(f"Média: {media:.1f}")