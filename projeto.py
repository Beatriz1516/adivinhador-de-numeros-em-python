print("******************************************")
print("*Bem-vindo ao jogo de descobrir números*")
print("******************************************")

#definição das variáveis do número secreto, das tentativas e do número de rodadas
numero_secreto = 22
numero_tentativas = 3

#definição da função de laço (for utilizando o atributo range) para repetir a quantidade de rodadas (print das tentativas, definição do input, mostrar qual o número chutado e a função de acerto)
for rodada in range(1, numero_tentativas + 1):
#o python vai substituir as chaves pelos valores que estão dentro da função format. (string interpolation)
    print ("TENTATIVAS {} DE {}".format(rodada, numero_tentativas))
    chute = int(input("Digite o seu número entre 1 e 40: "))
    print ("Você digitou ", chute)
#define um laço que impede o jogador de chutar um número menor que 1 e maior que 40
    if (chute < 1 or chute > 40):
      print("***Você deve digitar um número entre 1 e 40!***")
#comando irmão do break, mas que faz o laço continue
      continue
#definição de variáveis de acerto (acertou, maior ou menor)
    acertou = chute == numero_secreto
    chute_menor = chute > numero_secreto
    chute_maior = chute < numero_secreto
#função de condição de acerto (acertou, maior que o número ou menor que o número)
    if (acertou):
          print ("Você acertou! :)")
#comando de parar e sair do laço caso o jogador acerte 
          break
    else:
        if (chute_menor):
          print("O número é menor que ", chute )
        elif(chute_maior):
          print("O número é maior que", chute )

print("Fim do jogo")