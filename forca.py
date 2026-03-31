import random

#define a função de jogar o jogo da forca
def jogar():
    print("******************************************")
    print("********Bem-vindo ao jogo da forca********")
    print("******************************************")
#abre o arquivo de palavras aleatórias, fecha e gera uma leitura aleatória das palavras do arquivo
    arquivo = open("palavras_secretas.txt", "r")
    palavras = []
    for linha in arquivo:
        palavras.append(linha.strip().upper())
    arquivo.close()

    numero_palavras_secreta = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero_palavras_secreta].upper()

#definição da palavra secreta e das letras acertadas
    letras_acertadas = ["_" for letra in palavra_secreta]
    
#definição das variáveis de acerto, erros e enforco
    enforcou = False
    acertou = False
    erros= 0

    print(letras_acertadas)

#definição da repetição do jogo, de entrada do chute e verificação de acerto
    while(not acertou and not enforcou):
        chute = input("Qual a letra?").upper()
        chute = chute.strip().upper()
        
        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index]= letra
                index += 1
        else: 
            erros += 1    
    
#se não tiver mais letras a serem encontradas, o jogador finaliza por acerto
        acertou = "_" not in letras_acertadas
        if (acertou):
            print("Você acertou a palavra secreta! Era {}".format(palavra_secreta))
            break
        print(letras_acertadas)

#repetição de quais letras falta descobrir, se erros < 6 (continua), se erros = 6 (enforcado)
        letras_faltando = (letras_acertadas.count("_"))
        if (erros == 0):
            print("Você não errou nenhuma vez, faltam {1} tentativas e {0} letras".format(letras_faltando, 6-erros))
        elif (erros == 1 or erros < 6):
            if (erros == 1):
                print("Você já errou {1} vez, faltam {2} tentativas e {0} letras".format(letras_faltando, erros, 6-erros))
            elif (erros < 6):
                print("Você já errou {1} vezes, faltam {2} tentativas e {0} letras".format(letras_faltando, erros, 6-erros))
        else:
            print("Você não conseguiu acertar a palavra secreta! Era {0} :(".format(palavra_secreta))
            if (print("Fim do jogo")):
                break

#quando o arquivo for executar fora da função ele define name como main, e ele pode ser executado. Mas, quando o arquivo jogos for executado a pasta só será importada.
if(__name__ == "__main__"):
    jogar()
