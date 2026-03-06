#importando documentos anteriores
import forca
import adivinhação
#define a função que roda todo o código de escolha de jogos
def escolha_de_jogo ():
    print("******************************************")
    print("*************Escolha seu jogo*************")
    print("******************************************")

    #escolha de qual jogo que executar
    print("[1] Forca [2] Adivinhação") 
    jogo = int(input("Qual jogo?"))
    #função de escolha de qual jogo o jogador quer jogar
    if(jogo == 1):
        print("Jogando forca")
    #o nome do módulo/arquivo antes da função
        forca.jogar()
    elif(jogo == 2):
        print("Jogo de descobrir números")
    #o nome do módulo/arquivo antes da função
        adivinhação.jogar()

if(__name__ == "__main__"):
    escolha_de_jogo()