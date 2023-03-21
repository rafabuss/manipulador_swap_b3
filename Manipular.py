from datetime import date
#from datetime import datetime 
from datetime import timedelta
import random

def cpf():
    def calcula_digito(digs):
       s = 0
       qtd = len(digs)
       for i in range(qtd):
          s += n[i] * (1+qtd-i)
       res = 11 - s % 11
       if res >= 10: return 0
       return res                                                                              
    n = [random.randrange(10) for i in range(9)]
    n.append(calcula_digito(n))
    n.append(calcula_digito(n))
    return "%d%d%d%d%d%d%d%d%d%d%d" % tuple(n)

def DefiniCampos(linhaatualcampo):
    global desccampo
    #global tipocaracter
    global tamanhocampo
    global required
    global posicao1campo
    global posicao2campo
    global valornovo
    desccampo = linhaatualcampo[4:37].replace(" ", "")
    tipocaraccampo = linhaatualcampo[37:39].replace(" ", "")
    tamanhocampo = linhaatualcampo[40:43].replace(" ", "")
    required = linhaatualcampo[45:46].replace(" ", "")
    posicao1campo = int(linhaatualcampo[47:53].replace(" ", ""))
    posicao2campo = int(linhaatualcampo[54:63].replace(" ", ""))
    valornovo = linhaatualcampo[63:73].replace(" ", "")
    #match tipocaraccampo:
    #    case 'X':
    #        tipocaracter = 'Alpha'
    #    case 'X1':
    #        tipocaracter = 'Alphanumeric'
    #    case '9':
    #        tipocaracter = 'Numeric'
    if required == 'S':
        required = True
    else:
        required = False

def alterarvalor(linha,posicao1,posicao2,novovalor,dataatual):
    if novovalor == 'Atual':
        novovalor = dataatual
    elif (len(novovalor) != 8) and (novovalor != '') and (novovalor.isnumeric()):
        plusdays = int(novovalor)
        dataatual = date.today() + timedelta(days=plusdays)
        novovalor = str(dataatual).replace("-", "")
    elif novovalor == 'CPF':
        novovalor = '   ' + cpf()
    elif novovalor == 'MATERABM':
        novovalor = novovalor + '            '
    if (novovalor == '') or (novovalor == 'N/Alterar'):
        linhanova = linha
    else:
        linhanova = linha[:posicao1 - 1] + novovalor + linha[posicao2:]
    
    print(linhanova)
    return linhanova

## Lê arquivo com a declaração dos campos
arqcampos = open("CamposSwapAlterar.txt")
linhasCampos = arqcampos.readlines()
##

data_atual = date.today()
data_atual_format = str(data_atual).replace("-", "")

arq = open("TESTE.txt")
linhas = arq.readlines()
linhaheader = linhas[0]
for campoatual in linhasCampos:
    if campoatual == linhasCampos[3]:
        break
    if campoatual != linhasCampos[0]:
        DefiniCampos(campoatual)
        linhaheader = alterarvalor(linhaheader,posicao1campo,posicao2campo,valornovo,data_atual_format)

for linhaatual in linhas:
    if linhaatual != linhas[0]:
        for campoatual in linhasCampos:
            if campoatual not in (linhasCampos[0],linhasCampos[1],linhasCampos[2],linhasCampos[3]):
                DefiniCampos(campoatual)
                linhaatual = alterarvalor(linhaatual,posicao1campo,posicao2campo,valornovo,data_atual_format)

NovoArquivo = open('NovoTeste1.txt', 'w')
NovoArquivo.write(linhaheader)
NovoArquivo.write(linhaatual)
NovoArquivo.close()