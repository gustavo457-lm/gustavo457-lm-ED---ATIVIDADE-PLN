from pathlib import Path
import re

# Localiza a pasta onde o main.py está salvo
pastaAtual = Path(__file__).parent
caminhoArquivo1 = pastaAtual / "batman.txt"
caminhoArquivo2 = pastaAtual / "stopwords-pt.txt"
with open(caminhoArquivo1, "r", encoding="utf-8") as arquivo:
    textoBruto = arquivo.read()

with open(caminhoArquivo2, "r", encoding="utf-8") as arquivo:
    stopwordsBruto = arquivo.read()

def main ():
    #opções do Menu
    print("-----Leitor PLN em Python-----")
    print("1-Ler arquivo TXT e mostrar a quantidade de palavras")
    print("2-Remover as stopwords e mostrar dados estatísticos")
    #(2) palavrasOriginais, #stopwords, e #palavrasSemStopwords;")
    print("3-Gerar e imprimir as palavras mais frequentes")
    print("4-Gerar e imprimir os Hapaxes Legomenons (palavras de frequência única)")
    print("5-Mostrar o gráfico com a Curva de Zipf e os cortes de Luhn.")

    option = int(input("Selecione uma opção: "))
    match option:
        case 1:
            quantidadePalavras=0
            textoLimpo = re.split(r"[,;.?!/\s ]+", textoBruto)
            textoLimpo.pop(-1) #remove o valor vazio do final
            print(textoBruto)
            for palavra in textoLimpo:
                quantidadePalavras+=1
            print(f"Quantidade de palavras: {quantidadePalavras}")
        case 2:

            stopwordsMaiusculas = stopwordsBruto.title()
            stopwordsBrutoConcatenado = stopwordsBruto + stopwordsMaiusculas
            stopwords = re.split(r"[,;.?!/\s ]+", stopwordsBrutoConcatenado)

        #Originais     
            #(textolimpo)
        #Stopwords
            textoStopwords = []
        #Sem stopwords
            textoLimpoStopwords = []
            i=0
            while(i<len(textoLimpo)):
                bool = 0 #controle
                for j in range(len(stopwords)):
                    if (textoLimpo[i]==stopwords[j]):
                        textoStopwords.append(textoLimpo[i])
                        bool = 1
                        break
                if bool == 0:
                    textoLimpoStopwords.append(textoLimpo[i])
                i+=1
            print("Dados Estatísticos do texto")
            print("---------------------------")
            print("Palavras originais:")
            print(textoLimpo)
            print("---------------------------")
            print("Palavras sem Stopwords:")
            print(textoLimpoStopwords)
            print("---------------------------")
            print("Stopwords no texto:")
            print(textoStopwords)
        case _:
            print("")


# Método main
if __name__=='__main__':
    main()
