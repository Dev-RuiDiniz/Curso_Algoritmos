# Faça uma função chamada Contador() que receba tres valores como parametro: o inicio, o fim e o intervalo. O programa principal deve solicitar esses valor e passa-lo a função que vai mostrar a contagem na tela.

def Contador(inicio, fim, intervalo):
    print(f"Contagem de {inicio} até {fim} de {intervalo} em {intervalo}:")
    
    if inicio < fim:  # Contagem crescente
        for numero in range(inicio, fim + 1, intervalo):
            print(numero, end=' ')
    else:  # Contagem decrescente
        for numero in range(inicio, fim - 1, -intervalo):
            print(numero, end=' ')
    print("\n" + "-" * 30)  # Linha decorativa

# Programa principal
print("Contador Personalizado")
ini = int(input("Digite o valor inicial: "))
fim = int(input("Digite o valor final: "))
intv = int(input("Digite o intervalo: "))

Contador(ini, fim, intv)