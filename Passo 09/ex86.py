# Crie uma função, que gere uma menssagem entre duas linhas ('---------').

def gerador(mensagem):
    linha = '-' * 30  # Você pode ajustar o número de traços conforme necessário
    return f"{linha}\n{mensagem}\n{linha}"

print(gerador("Olá, mundo!"))