import numpy as np

import mixem

from mixem.distribution import NormalDistribution


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
#organiza os dados
def generate_data():

    dist_params = []
    weights = []
    for i in range(len(instancias)):
        forPush = []
        atributos = instancias[i].split(',')
        for b in range(2):
            forPush.append(getValor(atributos[b]))
        dist_params.append(forPush)
        weights.append(1/len(instancias))
    data = np.zeros(len(instancias))
    for i in range(len(instancias)):

        dpi = np.random.choice(range(len(dist_params)), p=weights)
        mu, sigma = dist_params[dpi]
        data[i] = np.random.normal(loc=mu, scale=sigma)
    return data

#retorna o resultado
def recover(data):
    mu = np.mean(data)
    sigma = np.var(data)
    init_params = [

        (mu + 0.1, sigma),

        (mu - 0.1, sigma)

    ]
    weight, distributions, ll = mixem.em(data, [NormalDistribution(mu, sigma) for mu_sigma in init_params])
    print(weight, distributions, ll)

print('gerando dados')
data = generate_data()
print('calculando')
recover(data)
