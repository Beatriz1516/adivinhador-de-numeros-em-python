#importando documentos anteriores
import forca
import adivinhação

print("******************************************")
print("*************Escolha seu jogo*************")
print("******************************************")

#escolha de qual jogo que executar
print("[1] Forca [2] Adivinhação") 
jogo = int(input("Qual jogo?"))

if(jogo == 1):
    print("Jogando forca")
    forca.jogar()
elif(jogo == 2):
    print("Jogo de descobrir números")
    adivinhação.jogar()