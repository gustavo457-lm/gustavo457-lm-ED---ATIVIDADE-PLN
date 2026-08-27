from pathlib import Path
import re
import matplotlib.pyplot as plt
import numpy as np

pastaAtual = Path(__file__).parent
caminhoArquivo1 = pastaAtual / "batman.txt"
caminhoArquivo2 = pastaAtual / "stopwords-pt.txt"
with open(caminhoArquivo1, "r", encoding="utf-8") as arquivo:
    textoBruto = arquivo.read()

with open(caminhoArquivo2, "r", encoding="utf-8") as arquivo:
    stopwordsBruto = arquivo.read()

def limparTexto(textoBruto):
    textoLimpo = re.split(r"[,;.?!/()↑•\s ]+", textoBruto)
    if textoLimpo[-1] == '':
        textoLimpo.pop(-1) #remove o valor vazio do final
    return textoLimpo

def removeStopwords(textoLimpo, stopwordsBruto):
    stopwordsMaiusculas = stopwordsBruto.title()
    stopwordsBrutoConcatenado = stopwordsBruto + stopwordsMaiusculas
    stopwords = re.split(r"[,;.?!/()↑•\s ]+", stopwordsBrutoConcatenado)

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
    qntPalavras = 0
    for palavra in range(len(texto)):
        qntPalavras+=1
    return qntPalavras

def frequenciaComPalavrasSemRepetir(textoLimpo):
    Frequencias = []
    palavras_sem_repetir = []
    for i in range(len(textoLimpo)):
        if i == 0:
            palavra_atual = textoLimpo[i]
            palavras_sem_repetir.append(palavra_atual)
            Frequencias.append(textoLimpo.count(palavra_atual))
        if textoLimpo[i] not in palavras_sem_repetir:
            palavra_atual = textoLimpo[i]
            palavras_sem_repetir.append(palavra_atual)
            Frequencias.append(textoLimpo.count(palavra_atual))
    return Frequencias, palavras_sem_repetir

def maiorFrequencia(textoLimpoDeStopwords):
    Frequencias, p = frequenciaComPalavrasSemRepetir(textoLimpoDeStopwords)
    maiorFrequencia = 1
    for i in range(len(Frequencias)):
        if Frequencias[i] > maiorFrequencia:
            maiorFrequencia = Frequencias[i]
    return maiorFrequencia

def HapaxesLegomenons(texto):
    auxRepeticao = []
    for i in range(len(texto)):
        auxRepeticao.append(texto[i].lower())

    Frequencias, palavras_sem_repetir = frequenciaComPalavrasSemRepetir(auxRepeticao)
    HapaxesLegomenons = []

    for i in range(len(Frequencias)):
        if Frequencias[i] == 1:
            HapaxesLegomenons.append(palavras_sem_repetir[i])
    return HapaxesLegomenons

def topK(frequencia, palavras_sem_repetir, k, graphBool):
    n = len(frequencia)
    
    for i in range(n):
        for j in range(i + 1, n):
            if frequencia[j] > frequencia[i]:
                aux_freq = frequencia[i]
                frequencia[i] = frequencia[j]
                frequencia[j] = aux_freq
                                          
                aux_palavra = palavras_sem_repetir[i]
                palavras_sem_repetir[i] = palavras_sem_repetir[j]
                palavras_sem_repetir[j] = aux_palavra
    ranking = []
    if(graphBool == 0):
        print(f"TOP {k} palavras mais repetida")
    posicao = 1
    for i in range(k):
        if i < n:
            if i > 0 and frequencia[i] < frequencia[i-1]:
                posicao = i + 1
            item = f"{posicao}º posição: {palavras_sem_repetir[i]} ({frequencia[i]}x)"
            ranking.append(posicao)
        else:
            item = f"{posicao}º posição: inexistente"
        if(graphBool == 0):
            print(item)
    for i in range (k,n):
        if frequencia[i] < frequencia[i-1]:
            posicao = i + 1
            ranking.append(posicao)
    return ranking


def grafico(frequencia,textoLimpo):
    a, stopwords = removeStopwords(textoLimpo, stopwordsBruto)
    b, stopwordsSemRep = frequenciaComPalavrasSemRepetir(stopwords)
    hapaxesGraph = HapaxesLegomenons(textoLimpo)
    x = []
    for i in range(len(frequencia)):
        x.append(i)
    y = frequencia
    plt.figure(figsize=(9, 5))
    plt.plot(x, y, label='Curva de Zipf', color='blue', linewidth=2)
    
    plt.title('Curva de Zipf e os cortes de Luhn')
    plt.xlabel('Ranking')
    plt.ylabel('Frequência')
    plt.legend()
    print(len(stopwordsSemRep))

    plt.axvline(x=len(hapaxesGraph), color='red', linestyle=':', linewidth=2, label='Corte Inferior')
    plt.axvline(x=len(stopwordsSemRep), color='green', linestyle=':', linewidth=2, label='Corte Superior')
    
 
    # Mostrar o gráfico
    plt.show()
    #plt.axvline(x=corte_inferior, color='green', linestyle=':', linewidth=2, label='Corte Inferior')
def main ():
    #opções do Menu
    option = 0
    controlStop = 0
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
                    textoLimpo = limparTexto(textoBruto)
                    print("Texto original:")
                    print(textoBruto)
                    print("------------------------------")
                    print(f"Quantidade de palavras no texto: {quantidadePalavras(textoLimpo)}")
                    print("------------------------------")
                    
                case 2:
                    try:
                        textoLimpoDeStopwords, textoStopwords = removeStopwords(textoLimpo, stopwordsBruto)
                        controlStop = 1
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
                        try:
                            k = int(input("Qual o top(k) que deseja saber? "))
                            if k == 0:
                                print("Não existe colocações 0")
                            if k < 0:
                                print("Não existe colocações negativas")
                        except ValueError:
                            print("Escolha um valor válido de colocação")
                            
        

                        frequencia = []
                        palavras_sem_repetir = []   
                        if (controlStop == 1):
                            auxRepeticao = []
                            for i in range(len(textoLimpoDeStopwords)):
                                auxRepeticao.append(textoLimpoDeStopwords[i].lower())
                            frequencia, palavras_sem_repetir = frequenciaComPalavrasSemRepetir(auxRepeticao) #semStopwords            
                        else:
                            frequencia, palavras_sem_repetir = frequenciaComPalavrasSemRepetir(textoLimpo)  #comStopwords

                        graphBool = 0
                        ranking = topK(frequencia, palavras_sem_repetir, k, graphBool)
                       
                    except UnboundLocalError:
                        print("Realize primeiro a leitura do arquivo TXT para ter acesso aos dados!")
                        print("------------------------------")
                case 4:
                    #Gerar e imprimir os Hapaxes Legomenons (palavras de frequência única)"
                    try:
                        unicaRepeticao = HapaxesLegomenons(textoLimpo)
                        print(f"Os Hapaxes Legomenons são: {unicaRepeticao}")
                        print(f"Total de Hapaxes Legomenons: {len(unicaRepeticao)}")
                    except UnboundLocalError:
                        print("Realize primeiro a leitura do arquivo TXT para ter acesso aos dados!")
                        print("------------------------------")
                case 5:
                    try:
                        frequencia = []
                        palavras_sem_repetir = []
                        if (controlStop == 1):
                            frequencia, palavras_sem_repetir = frequenciaComPalavrasSemRepetir(textoLimpoDeStopwords) #semStopwords
                        else:
                            frequencia, palavras_sem_repetir = frequenciaComPalavrasSemRepetir(textoLimpo)  #comStopwords
                        graphBool = 1
                        k = 1
                        ranking = topK(frequencia, palavras_sem_repetir, k, graphBool)
                        grafico(frequencia, textoLimpo)
                    except UnboundLocalError:
                        print("Realize primeiro a leitura do arquivo TXT para ter acesso aos dados!")
                        print("------------------------------")
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
