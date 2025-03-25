# Crie uma função, que gere quatro menssagens 'Aprendendo Python' entre duas linhas ('---------').
# Crie pelo menos 3 modelos de borda que podem ser escolhidos.

def gerador(mensagem, quantidade=1, borda=1):
    # Define os estilos de borda disponíveis
    bordas = {
        1: '-' * 30,                # Padrão: linha simples
        2: '=' * 30,                # Linha dupla (estilo mais forte)
        3: '-~' * 15,               # Padrão decorativo alternado
        4: '★' * 15,               # Bordas com estrelas
        5: '♦' * 15,                # Bordas com diamantes
    }
    
    linha = bordas.get(borda, '-' * 30)  # Usa a borda escolhida ou padrão se inválida
    mensagem_repetida = "\n".join([mensagem] * quantidade)
    return f"{linha}\n{mensagem_repetida}\n{linha}"

print(gerador("Python é incrível!", 2, 1))  # Borda 1 (linha simples)
print(gerador("Aprendendo funções", 3, 2))  # Borda 2 (linha dupla)
print(gerador("Borda decorativa!", 1, 3))   # Borda 3 (padrão alternado)
print(gerador("Borda estrelada", 1, 4))     # Borda 4 (estrelas)
print(gerador("Borda de diamantes", 1, 5))  # Borda 5 (diamantes)