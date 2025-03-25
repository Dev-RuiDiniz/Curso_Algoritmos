# Crie um função chamada ParOuImpar(), que vai receber um numero inteiro e dizer se é par ou impar.

def ParOuImpar(numero):
    if numero % 2 == 0:
        return f"{numero} é par!"
    else:
        return f"{numero} é ímpar!"

num = int(input("Digite um número inteiro: "))
print(ParOuImpar(num))