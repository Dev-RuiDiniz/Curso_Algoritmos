# Desenvolva um algoritmo que leia varios valores e passe esses valores pra a função Maior() que vai vericar qual deles é o maior e mostra-lo na tela. Essa função retorna qual o valor maior ou se ambos os valores são iguais.

def Maior(*valores):
   
    if not valores:  # Se nenhum valor foi passado
        return "Nenhum valor foi informado"
    
    maior = valores[0]
    todos_iguais = True
    
    for valor in valores:
        if valor > maior:
            maior = valor
            todos_iguais = False
        elif valor < maior:
            todos_iguais = False
    
    if todos_iguais:
        return f"Todos os {len(valores)} valores são iguais a {maior}"
    else:
        return f"O maior valor é {maior}"

# Programa principal
valores = []
print("Identificador do Maior Valor (digite 'fim' para terminar)")

while True:
    entrada = input("Digite um número (ou 'fim' para encerrar): ").strip().lower()
    
    if entrada == 'fim':
        if len(valores) == 0:
            print("Nenhum valor foi informado!")
        break
    
    try:
        numero = float(entrada)
        valores.append(numero)
    except ValueError:
        print("Valor inválido! Digite apenas números ou 'fim'.")

if valores:
    resultado = Maior(*valores)
    print("\n" + "="*40)
    print(f"Valores informados: {valores}")
    print(resultado)
    print("="*40)