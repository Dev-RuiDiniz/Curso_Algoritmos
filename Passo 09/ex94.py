#  Crie uma função chamada Fibonacci( ) que vai receber um unico valor inteiro como parametro que vai definir quantos termos da sequencia serao mostrados. O programa principal deve pedir o valor valor e executar a função.

def Fibonacci(quantidade):
    a, b = 0, 1
    print(f"Sequência de Fibonacci com {quantidade} termos:")
    
    for _ in range(quantidade):
        print(a, end=' → ')
        a, b = b, a + b
    print("FIM")

# Programa principal
try:
    n = int(input("Quantos termos da sequência de Fibonacci deseja mostrar? "))
    if n <= 0:
        print("Por favor, digite um número inteiro positivo!")
    else:
        Fibonacci(n)
except ValueError:
    print("Erro: Por favor, digite um número inteiro válido!")