# Crie uma função, que gere a menssagem 'Aprendendo Python' entre duas linhas ('---------').

def gerador(mensagem):
    linha = '-' * 30  # Você pode ajustar o número de traços conforme necessário
    return f"{linha}\n{mensagem}\n{linha}"

print(gerador("Aprendendo Python!"))