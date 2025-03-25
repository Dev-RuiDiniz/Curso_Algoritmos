# Crie uma função chamada Potencia( ) que vai receber dois paramentros: base e expoente. Apos isso ela vai calcular o resultado da exponenciação.

def Potencia(base, expoente):
    """Calcula a potência de um número"""
    return base ** expoente

# Programa principal
print("CALCULADORA DE POTÊNCIAS")

try:
    b = float(input("Digite a base: "))
    e = float(input("Digite o expoente: "))
    
    resultado = Potencia(b, e)
    print(f"\nResultado: {b}^{e} = {resultado}")
    
except ValueError:
    print("Erro: Digite apenas números!")