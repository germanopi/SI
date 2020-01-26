import knn_kv as knn
#os imports
#como essa biblioteca usa números, estou fazendo uma maneira de converter as entradas q não sejam números
def getValor(a):
    #parte dos atributos comuns
    if a=='a':
        return 0
    elif a=='b':
        return 1
    elif a=='c':
        return 2
    elif a=='d':
        return 3
    elif a=='e':
        return 4
    elif a=='f':
        return 5
    elif a=='g':
        return 6
    elif a=='h':
        return 7
    #parte do resultado 
    elif a=='draw':
        return -1
    elif a=='zero':
        return 0
    elif a=='one':
        return 1
    elif a=='two':
        return 2
    elif a=='three':
        return 3
    elif a=='four':
        return 4
    elif a=='five':
        return 5
    elif a=='six':
        return 6
    elif a=='seven':
        return 7
    elif a=='eight':
        return 8
    elif a=='nine':
        return 9
    elif a=='ten':
        return 10
    elif a=='eleven':
        return 11
    elif a=='twelve':
        return 12
    elif a=='thirteen':
        return 13
    elif a=='fourteen':
        return 14
    elif a=='fifteen':
        return 15
    elif a=='sixteen':
        return 16
    else:
        return int(a)
    
def voltarValor(a):
    if a==-1:
        return 'draw'
    elif a==0:
        return 'zero'
    elif a==1:
        return 'one'
    elif a==2:
        return 'two'
    elif a==3:
        return 'three'
    elif a==4:
        return 'four'
    elif a==5:
        return 'five'
    elif a==6:
        return 'six'
    elif a==7:
        return 'seven'
    elif a==8:
        return 'eight'
    elif a==9:
        return 'nine'
    elif a==10:
        return 'ten'
    elif a==11:
        return 'eleven'
    elif a==12:
        return 'twelve'
    elif a==13:
        return 'thirteen'
    elif a==14:
        return 'fourteen'
    elif a==15:
        return 'fifteen'
    elif a==16:
        return 'sixteen'
    else:
        return 'outro'


#abrindo o arquivo
with open('krkopt.csv') as file:
	arquivo = file.read()

#separando em lista por instancia
instancias = arquivo.split("\n")[:-1]

#o array dos dados organizados para o algoritmo
dadosTreino = []
dadosTeste = []
for i in range((3*len(instancias))//4):#primeira metade
    #cada atributo da instancia
    atributos = instancias[i].split(',')
    pushar = {'features': [], 'result': getValor(atributos[6])}
    for b in range(6):
        pushar['features'].append(getValor(atributos[b]))
    dadosTreino.append(pushar)

for i in range(((3*len(instancias))//4)+1,len(instancias)):#segunda metade
    #cada atributo da instancia
    atributos = instancias[i].split(',')
    pushar = {'features': [], 'result': atributos[6]}
    for b in range(6):
        pushar['features'].append(getValor(atributos[b]))
    dadosTeste.append(pushar)

#função para fazer o teste dependendo do número de vizinhos
def verificar(vizinhos):
    print('KNN com k =', vizinhos)
    acertos = 0
    total = 0
    for i in range(len(dadosTeste)):
        total = total + 1
        resultado = int(knn.weightedknn(dadosTreino, dadosTeste[i]['features'], k=vizinhos, weightf=knn.inverseweight))
        resultado = voltarValor(resultado)
        acertou = (resultado == dadosTeste[i]['result'])
        if acertou:
            acertos = acertos + 1
        #use a linha abaixo para ir vendo o resultado por instancia
        #print('o resultado foi: ', resultado, 'o esperado era: ', dadosTeste[i]['result'], acertou)
    acuracia = (acertos*100) / total
    acuracia = str(acuracia)
    print('A ACURÁCIA É DE: '+acuracia+'%.')

verificar(5)