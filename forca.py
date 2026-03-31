import random

def apresentação_jogo():
    print("******************************************")
    print("********Bem-vindo ao jogo da forca********")
    print("******************************************")
def carrega_palavra_secreta():
#abre o arquivo de palavras aleatórias, fecha e gera uma leitura aleatória das palavras do arquivo
    arquivo = open("palavras_secretas.txt", "r")
    palavras = []
    for linha in arquivo:
        palavras.append(linha.strip().upper())
    arquivo.close()

    numero_palavras_secreta = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero_palavras_secreta].upper()
    return palavra_secreta
def inicializa_letras_acertadas(palavra):
#definição da palavra secreta e das letras acertadas
    return ["_" for letra in palavra]
def input_jogador():
        chute = input("Qual a letra?").upper()
        chute = chute.strip().upper()
        return chute
def marca_chute_correto(chute, palavra_secreta, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if(chute == letra):
            letras_acertadas[index]= letra
        index += 1
def mensagem_ganhador(palavra_secreta, letras_acertadas):
    print("Você acertou a palavra secreta! Era {}".format(palavra_secreta))
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-::      :-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        :::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
def zero_erros(letras_faltando, erros):
    print("Você não errou nenhuma vez, faltam {1} tentativas e {0} letras".format(letras_faltando, 6-erros))
def de_1_erro_ate_6(erros,letras_faltando):
    if (erros == 1):
        print("Você já errou {1} vez, faltam {2} tentativas e {0} letras".format(letras_faltando, erros, 6-erros))
    elif (erros < 6):
        print("Você já errou {1} vezes, faltam {2} tentativas e {0} letras".format(letras_faltando, erros, 6-erros))
def mensagem_perdedor(palavra_secreta):
    print("Você não conseguiu acertar a palavra secreta e foi enforcado! Era {0} :(".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def jogar():

    apresentação_jogo()
    print("DICA: A classe da palavra secreta é ANIMAIS")

    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

#definição das variáveis de acerto, erros e enforco
    enforcou = False
    acertou = False
    erros= 0

#definição da repetição do jogo, de entrada do chute e verificação de acerto
    while(not acertou and not enforcou):

        chute = input_jogador()

        if (chute in palavra_secreta):
            marca_chute_correto(chute, palavra_secreta, letras_acertadas)
        else: 
            erros += 1    
    
#se não tiver mais letras a serem encontradas, o jogador finaliza por acerto
        acertou = "_" not in letras_acertadas
        if (acertou):
            mensagem_ganhador(palavra_secreta, letras_acertadas)
            break
        print(letras_acertadas)

#repetição de quais letras falta descobrir, se erros < 6 (continua), se erros = 6 (enforcado)
        letras_faltando = (letras_acertadas.count("_"))
        if (erros == 0):
            zero_erros(letras_faltando, erros)
        elif (erros == 1 or erros < 6):
            de_1_erro_ate_6(erros,letras_faltando)
        else:
            mensagem_perdedor(palavra_secreta)
            break

#quando o arquivo for executar fora da função ele define name como main, e ele pode ser executado. Mas, quando o arquivo jogos for executado a pasta só será importada.
if(__name__ == "__main__"):
    jogar()