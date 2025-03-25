# Crie uma função que se chamara Media( ), ela vai receber duas notas dos alunos e retornar a media ao programa principal. Ele tambem de diser se o aluno foi aprovado, está de recuperação ou foi reprovado.

def Media(nota1, nota2):
    """Calcula a média de duas notas"""
    return (nota1 + nota2) / 2

# Programa principal
print("CÁLCULO DE MÉDIA ESCOLAR")

# Solicita as notas com tratamento de erros
try:
    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))
    
    # Verifica se as notas estão no intervalo válido (0 a 10)
    if 0 <= n1 <= 10 and 0 <= n2 <= 10:
        media = Media(n1, n2)
        print(f"\nMédia: {media:.1f}")
        
        # Verifica situação do aluno
        if media >= 7:
            print("Situação: Aprovado!")
        elif media >= 5:
            print("Situação: Recuperação")
        else:
            print("Situação: Reprovado")
    else:
        print("Erro: As notas devem estar entre 0 e 10")
        
except ValueError:
    print("Erro: Digite apenas valores numéricos!")