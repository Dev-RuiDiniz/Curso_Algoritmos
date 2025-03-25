# Crie uma função, que gere quatro menssagens 'Aprendendo Python' entre duas linhas ('---------').

def gerador(mensagem, quantidade=1):
    linha = '-' * 30
    mensagem_repetida = "\n".join([mensagem] * quantidade)  # Repete a mensagem N vezes
    return f"{linha}\n{mensagem_repetida}\n{linha}"

print(gerador("Aprendendo Python!", 4))