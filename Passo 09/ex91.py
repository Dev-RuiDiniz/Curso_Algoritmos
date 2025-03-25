# Desenvolva um algoritmo que leia dois valores e passe esses valores pra a função Maior() que vai vericar qual deles é o maior e mostra-lo na tela. Essa função retorna qual o valor maior ou se ambos os valores são iguais.

def Maior(a, b):
    if a > b:
        return f"O maior valor é: {a}"
    elif b > a:
        return f"O maior valor é: {b}"
    else:
        return "Os valores são iguais!"

valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

resultado = Maior(valor1, valor2)
print(resultado)