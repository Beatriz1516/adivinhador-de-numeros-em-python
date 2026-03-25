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
    while(not acertou and not enforcou):
        chute = input("Qual a letra?")
        chute = chute.strip()
        
        index = 1
#utiliza o for para verificar a sequência (de caracteres)
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                print("A letra {1} tem na posição {0}.".format(index, letra.upper()))
            index = index + 1      
                      
        print("jogando...")

#quando o arquivo for executar fora da função ele define name como main, e ele pode ser executado. Mas, quando o arquivo jogos for executado a pasta só será importada.
if(__name__ == "__main__"):
    jogar()