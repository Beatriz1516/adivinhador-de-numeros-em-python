print("*********************************")
print("Bem vindo ao jogo de descobrir números!")
print("*********************************")

#definição das variáveis do número secreto, das tentativas e do número de rodadas
numero_secreto = 22
total_de_tentativas = 3
rodada = 1

#definição da função de laço para repetir a quantidade de rodadas (print das tentativas, definição do input, mostrar qual o número chutado e a função de acerto)
while (rodada <= total_de_tentativas):
    print("Tentativa", rodada, "de", total_de_tentativas)
    chute = int(input("Digite o seu número: "))
    print("Você digitou " , chute)
     #definição de variáveis de acerto (acertou, maior ou menor)
    acertou = chute == numero_secreto
    chute_maior = chute > numero_secreto
    chute_menor = chute < numero_secreto
    #função de condição de acerto (acertou, maior que o número ou menor que o número)
    if(acertou):
        print("Parabéns! Você acertou! :)")
    else:
        if(chute_maior):
            print("O seu chute foi maior do que o número secreto!")
        elif(chute_menor):
            print("O seu chute foi menor do que o número secreto!")
    #definição da métrica do número de rodadas (a cada nova tentativa é mostrado em qual rodada a tentativa se encontra)      
    rodada = rodada + 1

print("Fim do jogo")
