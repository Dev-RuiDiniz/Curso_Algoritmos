# Crie um função chamda SuperSomador( ) que vai receber dois numeros e fazer a somar de todos o numeros no intervalo entre eles.

def SuperSomador(inicio, fim):
    """Soma todos os números no intervalo entre início e fim (inclusive)"""
    if inicio > fim:  # Se os números estiverem em ordem decrescente
        inicio, fim = fim, inicio  # Inverte os valores
        
    soma = 0
    for numero in range(inicio, fim + 1):
        soma += numero
    return soma

# Programa principal
print("SUPER SOMADOR DE INTERVALOS")
print("Digite dois números para somar todos os valores entre eles")

try:
    num1 = int(input("Primeiro número: "))
    num2 = int(input("Segundo número: "))
    
    resultado = SuperSomador(num1, num2)
    print(f"\nA soma de todos os números entre {num1} e {num2} é: {resultado}")
    
except ValueError:
    print("Erro: Por favor, digite apenas números inteiros!")