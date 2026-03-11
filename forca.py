#define a função de jogar o jogo da forca
def jogar():
    print("******************************************")
    print("********Bem-vindo ao jogo da forca********")
    print("******************************************")
    print("Fim de jogo")
    
#definição da palavra secreta 
    palavra_secreta = "abacate"
#definição das variáveis de acerto ou enforco
    enforcou = False
    acertou = False

#definição do laço de repetição para continuar jogando
    while(not enforcou and not acertou):
#definição da interação com o usuário, definição do input do chute
        chute = input("Qual a letra?")
#utiliza o for para verificar a sequência (de caracteres)
        for letra in palavra_secreta:
            if (chute == letra):
                print(chute)
                print("Não tem essa letra!")
                continue
                
        print("jogando...")

#quando o arquivo for executar fora da função ele define name como main, e ele pode ser executado. Mas, quando o arquivo jogos for executado a pasta só será importada.
if(__name__ == "__main__"):
    jogar()