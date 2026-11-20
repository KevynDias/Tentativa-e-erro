#Defino um Numero secreto
numero_definido = 100
numero_chutado = 0
tentativas = 0
#jogador chuta um numero
#Chute muito alto ou muito baixo
while numero_chutado != numero_definido:
    print("Chute um numero")
    numero_chutado = int(input())
    if numero_chutado > numero_definido:
        print("Muito alto")
        print()
    elif numero_chutado < numero_definido:
        print("Muito baixo")
        print()
    elif numero_chutado == numero_definido:
        print("voce acertou")
        print()
    tentativas = tentativas + 1

print(f"Voce acertou em " + str(tentativas) + " tentativas")
