#define a função de jogar o jogo da forca
def jogar():
    print("******************************************")
    print("********Bem-vindo ao jogo da forca********")
    print("******************************************")
    
#definição da palavra secreta 
    palavra_secreta = "paracetamol"
    letras_acertadas = ["_","_","_","_","_","_","_","_","_","_","_"]
    
#definição das variáveis de acerto ou enforco
    enforcou = False
    acertou = False

    print(letras_acertadas)

#definição do laço de repetição para continuar jogando
    while(not acertou and not enforcou):
        chute = input("Qual a letra?")
        chute = chute.strip()
        
        index = 0
#utiliza o for para verificar a sequência (de caracteres)
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
              letras_acertadas[index]= letra
            index = index + 1      
        
        print(letras_acertadas)
#retorna quantas letras ainda não foram encontradas
        letras_faltando = (letras_acertadas.count("_"))
        print("Ainda faltam acertar {} letras".format(letras_faltando))

#quando o arquivo for executar fora da função ele define name como main, e ele pode ser executado. Mas, quando o arquivo jogos for executado a pasta só será importada.
if(__name__ == "__main__"):
    jogar()