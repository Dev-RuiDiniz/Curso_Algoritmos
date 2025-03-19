# Um programa de vida saudavel quer dar pontos de atividades fisicas que podem ser trocados por dinheiro. O sistema funciona assim:
# - Cada hora de atividade fisica no mês vale uma quantidade de pontos:
#   - 1 a 10 horas: 5 pontos por hora
#   - 11 a 20 horas: 10 pontos por hora
#   - 21 a 30 horas: 15 pontos por hora
#   - 31 ou mais horas: 20 pontos por hora  
# - Cada ponto pode ser trocado por R$ 0,05
# - O programa deve perguntar quantas horas de atividade fisica a pessoa fez no mês e mostrar quantos pontos ela ganhou e quanto dinheiro ela ganhou
# - O programa deve perguntar se a pessoa quer continuar e, se sim, repetir o processo

def calcular_pontos(horas):
    if horas <= 10:
        return horas * 5
    elif horas <= 20:
        return horas * 10
    elif horas <= 30:
        return horas * 15
    else:
        return horas * 20
    
def calcular_dinheiro(pontos):
    return pontos * 0.05  

while True:
    horas = int(input("Quantas horas de atividade fisica você fez no mês? "))
    pontos = calcular_pontos(horas)
    dinheiro = calcular_dinheiro(pontos)
    print(f"Você ganhou {pontos} pontos e R$ {dinheiro:.2f}")
    continuar = input("Deseja continuar? (s/n) ")
    if continuar.lower() != "s":
        break
print("Obrigado por usar o programa!")

# Para testar o programa, você pode rodar o código e digitar a quantidade de horas de atividade fisica que você fez no mês. O programa vai calcular quantos pontos você ganhou e quanto dinheiro você ganhou. Depois, ele vai perguntar se você quer continuar. Se você digitar "s", o programa vai perguntar novamente quantas horas de atividade fisica você fez no mês. Se você digitar "n", o programa vai parar.