# Crie uma função soma que receba do valores e mostre o resultado.

def soma():
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        print(f"\nResultado: {num1} + {num2} = {num1 + num2}")
    except ValueError:  # Se digitar texto em vez de número
        print("Erro: Digite apenas números!")

soma()