# Crie uma função Somador( ) que receba varios valores e mostre soma entre eles. O Programa principal cria um loop que vai perguntando se deseja continuar adicionando mais valores na função.

def Somador(*valores):
    soma = sum(valores)
    print(f"\nValores informados: {valores}")
    print(f"Soma total: {soma}\n")
    return soma  # Retorna o valor da soma para uso posterior, se necessário

# Programa principal
print("=== SOMADOR FLEXÍVEL ===")
valores = []

while True:
    try:
        # Pede um novo valor
        valor = float(input("Digite um valor para somar (ou '0' para sair): "))
        
        if valor == 0:  # Condição de saída
            if len(valores) > 0:  # Só mostra resultado se tiver valores
                Somador(*valores)
            print("Programa encerrado.")
            break
            
        valores.append(valor)  # Adiciona o valor à lista
        
        # Pergunta se quer continuar
        continuar = input("Deseja adicionar mais valores? [S/N] ").strip().upper()
        if continuar != 'S':
            Somador(*valores)
            print("Programa encerrado.")
            break
            
    except ValueError:
        print("Valor inválido! Digite apenas números.")