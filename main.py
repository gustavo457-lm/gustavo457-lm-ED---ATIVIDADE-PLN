from pathlib import Path
import re

def limparTexto(textoBruto):
    textoLimpo = re.split(r"[,;.?!/\s ]+", textoBruto)
    textoLimpo.pop(-1) #remove o valor vazio do final
    return textoLimpo

def removeStopwords(textoLimpo, stopwordsBruto):
    stopwordsMaiusculas = stopwordsBruto.title()
    stopwordsBrutoConcatenado = stopwordsBruto + stopwordsMaiusculas
    stopwords = re.split(r"[,;.?!/\s ]+", stopwordsBrutoConcatenado)

    textoStopwords = []
    textoLimpoDeStopwords = []
    i=0
    while(i<len(textoLimpo)):
        bool = 0 #controle
        for j in range(len(stopwords)):
            if (textoLimpo[i]==stopwords[j]):
                textoStopwords.append(textoLimpo[i])
                bool = 1
                break
        if bool == 0:
            textoLimpoDeStopwords.append(textoLimpo[i])
        i+=1
    return textoLimpoDeStopwords, textoStopwords

def quantidadePalavras(texto):
    quantidadePalavras = 0
    for palavra in range(len(texto)):
        quantidadePalavras+=1
    return quantidadePalavras
def frequenciaComPalavrasSemRepetir(textoLimpoDeStopwords):
    Frequencias = []
    palavras_sem_repetir = []
    for i in range(len(textoLimpoDeStopwords)):
        if i == 0:
            palavra_atual = textoLimpoDeStopwords[i]
            palavras_sem_repetir.append(palavra_atual)
            Frequencias.append(textoLimpoDeStopwords.count(palavra_atual))
        if textoLimpoDeStopwords[i] not in palavras_sem_repetir:
            palavra_atual = textoLimpoDeStopwords[i]
            palavras_sem_repetir.append(palavra_atual)
            Frequencias.append(textoLimpoDeStopwords.count(palavra_atual))
    return Frequencias, palavras_sem_repetir
def maiorF(textoLimpoDeStopwords):
    Frequencias, p = frequenciaComPalavrasSemRepetir(textoLimpoDeStopwords)
    maiorFrequencia = 1
    for i in range(len(Frequencias)):
        if Frequencias[i] > maiorFrequencia:
            maiorFrequencia = Frequencias[i]
    return maiorFrequencia
def HapaxesLegomenons(textoLimpoDeStopwords):
    Frequencias, palavras_sem_repetir = frequenciaComPalavrasSemRepetir(textoLimpoDeStopwords)
    HapaxesLegomenons = []
    for i in range(len(Frequencias)):
        if Frequencias[i] == 1:
            HapaxesLegomenons.append(palavras_sem_repetir[i])
    return HapaxesLegomenons
#def voltarAoMenu():
    print("Voltar ao menu ?")
    print("1-Sim")
    print("2-Não")
    voltar = 0
    while (voltar!=1 and voltar !=2):
        try:
            voltar = int(input("Selecione uma opção: "))
        except ValueError:
            voltar = -1
    if voltarAoMenu == 1:
        return 0
    else:
        return 6

def main ():
    #opções do Menu
    option = 0
    while(option!=6):
        try:
            print("-----Leitor PLN em Python-----")
            print("1-Ler arquivo TXT e mostrar a quantidade de palavras")
            print("2-Remover as stopwords e mostrar dados estatísticos")
    
            print("3-Gerar e imprimir as top(k) palavras mais frequentes")
            print("4-Gerar e imprimir os Hapaxes Legomenons (palavras de frequência única)")
            print("5-Mostrar o gráfico com a Curva de Zipf e os cortes de Luhn.")
            print("6-Encerrar programa ?")
            option = int(input("Selecione uma opção: "))
            print("------------------------------")
            match option:
                case 1:
                    pastaAtual = Path(__file__).parent
                    escolha = 0
                    while(escolha != 1 and escolha != 2):
                        print("1 - Acessar arquivo TXT na pasta do programa")
                        print("2 - Acessar arquivo TXT de qualquer pasta do computador")
                        escolha = int(input("Escolha uma das opções para a leitura do texto ser realizada: "))
                        print("------------------------------")
                        if escolha == 1: 
                            arquivoTXT = input("Digite o nome do arquivo TXT: ")
                            caminhoArquivo1 = pastaAtual / arquivoTXT

                        elif escolha == 2:
                            pasta = input("Digite o caminho da pasta: ")
                            arquivoTXT = input("Digite o nome do arquivo TXT: ")
                            # Localiza a pasta onde o main.py está salvo
                            caminhoPasta = Path(pasta)
                            caminhoArquivo1 = caminhoPasta / arquivoTXT
                            if not caminhoPasta.is_dir():
                                print("Pasta não encontrada!")
                                print("------------------------------")
                                continue
                        else: 
                            print("Escreva uma opção válida")
                    if not caminhoArquivo1.is_file():
                        print("Arquivo não encontrado!")
                        print("------------------------------")
                        continue

                    caminhoArquivo2 = pastaAtual / "stopwords-pt.txt"

                    with open(caminhoArquivo1, "r", encoding="utf-8") as arquivo:
                        textoBruto = arquivo.read()

                    with open(caminhoArquivo2, "r", encoding="utf-8") as arquivo:
                        stopwordsBruto = arquivo.read()
                    textoLimpo= limparTexto(textoBruto)
                    removeStopwords(textoLimpo, stopwordsBruto)
                    print("Texto original:")
                    print(textoBruto)
                    print("------------------------------")
                    print(f"Quantidade de palavras no texto: {quantidadePalavras(textoLimpo)}")
                    print("------------------------------")
                case 2:
                    try:
                        textoLimpoDeStopwords, textoStopwords = removeStopwords(textoLimpo, stopwordsBruto)
                        #print("------------------------------")
                        print("Dados Estatísticos do texto")
                        print("------------------------------")
                        print("Palavras originais:")
                        print(textoLimpo)
                        print(f"Quantidade de palavras originais: {quantidadePalavras(textoLimpo)}")
                        print("------------------------------")
                        print("Palavras sem Stopwords:")
                        print(textoLimpoDeStopwords)
                        print(f"Quantidade de palavras (sem stopwords): {quantidadePalavras(textoLimpoDeStopwords)}")
                        print("------------------------------")
                        print("Stopwords no texto:")
                        print(textoStopwords)
                        print(f"Quantidade de stopwords: {quantidadePalavras(textoStopwords)}")
                        print("------------------------------")
                    except UnboundLocalError:
                        print("Realize primeiro a leitura do arquivo TXT para ter acesso aos dados!")
                        print("------------------------------")
                case 3:
                    #Gerar e imprimir as palavras mais frequentes
                    try:
                        k = int(input("Qual o top(k) que deseja saber? "))
                        if k == 0:
                            print("Não existe colocações 0")
                        if k < 0:
                            print("Não existe colocações negativas")
                        posicao = 1
                        frequencia, palavras_sem_repetir = frequenciaComPalavrasSemRepetir(textoLimpoDeStopwords)
                        print(f"TOP {k} palavras mais repetidas: ")
                        frequencia.sort(reverse=True)
                        frequenciaSemRep = []
                        frequenciaSemRep.append(frequencia[0])
                        for i in range(1, len(frequencia)):
                            if frequencia[i] not in frequenciaSemRep:
                                frequenciaSemRep.append(frequencia[i])
                        while posicao < k:
                                for i in range(len(frequenciaSemRep)):
                                    vezesPosicao = 0
                                    for j in range(len(frequencia)):
                                        if frequencia[j] == frequenciaSemRep[i]:
                                            vezesPosicao+=1
                                            print(f"{posicao}º posição: {palavras_sem_repetir[j]}")
                                    posicao = posicao + vezesPosicao   
                                tamanhoDefrequenciaSemRep = tamanhoDefrequenciaSemRep - 1
                        if k > len(frequenciaSemRep):                        
                            for i in range(posicao, k+1):
                                print(f"{posicao}º: inexistente")
                                posicao = posicao + 1
                    except UnboundLocalError:
                        print("Primeiro retire as stopwords do texto!")
                        print("------------------------------")
                case 4:
                    #Gerar e imprimir os Hapaxes Legomenons (palavras de frequência única)"
                    try:
                        unicaRepeticao = HapaxesLegomenons(textoLimpoDeStopwords)
                        print(f"Os Hapaxes Legomenons são: {unicaRepeticao}")
                        print(f"Total de Hapaxes Legomenons: {len(unicaRepeticao)}")
                    except UnboundLocalError:
                        print("Primeiro retire as stopwords do texto!")
                        print("------------------------------")
                case 5:
                    print("")
                case 6:
                    print("Programa encerrado com sucesso!")
                case _:
                    print("------------------------------")
                    print("Digite um valor válido!!!")
                    print("------------------------------")
                
        except ValueError:
            option = -1

# Método main
if __name__=='__main__':
    main()
