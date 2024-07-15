#importacoes
import pandas as pd
import math
import numpy as np
import sys


#Carregar dados
df = pd.read_csv("data_input/insurance.csv")
#print(data.head())
#print(df.columns)
#print(df['charges'])

#normalização usando min-max
def normalicao(dataframe):
    column = 'charges'
    dataframe[column] = (dataframe[column] - dataframe[column].min()) / (dataframe[column].max() - dataframe[column].min())
    #for column in dataframe.columns:
    #    print(column)
    #    dataframe[column] = (dataframe[column] - dataframe[column].min()) / (dataframe[column].max() - dataframe[column].min())


#estatisticas resumo
#contagem fumantes
def contagemFumantes(dataframe):
    return dataframe['smoker'].value_counts()['yes']

#médias
def mediaFumantesNW(dataframe):
    return (dataframe[(dataframe['smoker'] == 'yes') & (dataframe['region'] == 'northwest')])['charges'].mean()

def mediaFumanteSW(dataframe):
    return (dataframe[(dataframe['smoker'] == 'yes') & (dataframe['region'] == 'southeast')])['charges'].mean()

def mediaNaoFumantesNW(dataframe):
    return (dataframe[(dataframe['smoker'] == 'no') & (dataframe['region'] == 'northwest')])['charges'].mean()

def mediaNaoFumanteSW(dataframe):
    return (dataframe[(dataframe['smoker'] == 'no') & (dataframe['region'] == 'southeast')])['charges'].mean()


#contagem
def contFumantesNW(dataframe):
    #return 100
    return (dataframe[(dataframe['smoker'] == 'yes') & (dataframe['region'] == 'northwest')])['charges'].count()

def contFumanteSW(dataframe):
    return (dataframe[(dataframe['smoker'] == 'yes') & (dataframe['region'] == 'southeast')])['charges'].count()

def contNaoFumantesNW(dataframe):
    return (dataframe[(dataframe['smoker'] == 'no') & (dataframe['region'] == 'northwest')])['charges'].count()

def contNaoFumanteSW(dataframe):
    return (dataframe[(dataframe['smoker'] == 'no') & (dataframe['region'] == 'southeast')])['charges'].count()


#std
def stdFumantesNW(dataframe):
    return (dataframe[(dataframe['smoker'] == 'yes') & (dataframe['region'] == 'northwest')])['charges'].std()

def stdFumanteSW(dataframe):
    return (dataframe[(dataframe['smoker'] == 'yes') & (dataframe['region'] == 'southeast')])['charges'].std()

def stdNaoFumantesNW(dataframe):
    return (dataframe[(dataframe['smoker'] == 'no') & (dataframe['region'] == 'northwest')])['charges'].std()

def stdNaoFumanteSW(dataframe):
    return (dataframe[(dataframe['smoker'] == 'no') & (dataframe['region'] == 'southeast')])['charges'].std()




#previsaoDeUso
#funcoes score

#funcoesDP
def funcaoDP(resultado, epsilon, sensitividade):
    test = resultado + np.random.laplace(loc=0, scale=sensitividade/epsilon)
    return test


#funcoes estatistica
#estou fazendo na forca bruta verificando a sensiiblidade levando em conta cada coluna do dataframe
def sensibilidade(dataframe, funcao):
    resposta = 0.0
    for i in range(0,dataframe.shape[0]):
        tmp = dataframe.copy().drop(index=i)
        #print(funcao(tmp) )
        #print(funcao(dataframe))
        if abs(funcao(tmp) - funcao(dataframe)) > resposta:
            resposta = abs(funcao(tmp) - funcao(dataframe))  
    return resposta


#t-test unpaired two means
def ttest(x1mean, x2mean, s1, s2, n1, n2):
    t = (x1mean - x2mean) / math.sqrt((pow(s1,2)/n1)+(pow(s2,2)/n2))
    return t


def ttestDF1(dataframe):
    x1mean = mediaFumantesNW(dataframe)
    x2mean = mediaFumanteSW(dataframe)
    s1 = stdFumantesNW(dataframe)
    s2 = stdFumanteSW(dataframe)
    n1 = contFumantesNW(dataframe)
    n2 = contFumanteSW(dataframe)
    t = (x1mean - x2mean) / math.sqrt((pow(s1,2)/n1)+(pow(s2,2)/n2))
    return t

def ttestDF2(dataframe):
    x1mean = mediaNaoFumantesNW(dataframe)
    x2mean = mediaNaoFumanteSW(dataframe)
    s1 = stdNaoFumantesNW(dataframe)
    s2 = stdNaoFumanteSW(dataframe)
    n1 = contNaoFumantesNW(dataframe)
    n2 = contNaoFumanteSW(dataframe)
    t = (x1mean - x2mean) / math.sqrt((pow(s1,2)/n1)+(pow(s2,2)/n2))
    return t

def ttestflexivel(dataframe, funcmedia1, funcmedia2, funcstd1, funcstd2, funcn1, funcn2):
    x1mean = funcmedia1(dataframe)
    x2mean = funcmedia2(dataframe)
    s1 = funcstd1(dataframe)
    s2 = funcstd2(dataframe)
    n1 = funcn1(dataframe)
    n2 = funcn2(dataframe)
    t = (x1mean - x2mean) / math.sqrt((pow(s1,2)/n1)+(pow(s2,2)/n2))
    return t

def ttestcomTupla(dataframe, tupla):
    x1mean = tupla[0]
    x2mean = tupla[1]
    s1 = tupla[2]
    s2 = tupla[3]
    n1 = tupla[4]
    n2 = tupla[5]
    t = (x1mean - x2mean) / math.sqrt((pow(s1,2)/n1)+(pow(s2,2)/n2))
    return t


#antes da normalizacao
#medias antes da normalizacao
print("Valores antes da normalizacao")
print("mediaFumantesNW: %f" % mediaFumantesNW(df))
print(sensibilidade(df, mediaFumantesNW))
print("mediaFumanteSW: %f" % mediaFumanteSW(df))
print(sensibilidade(df, mediaFumanteSW))
print("mediaNaoFumantesNW: %f" % mediaNaoFumantesNW(df))
print(sensibilidade(df, mediaNaoFumantesNW))
print("mediaNaoFumanteSW: %f" % mediaNaoFumanteSW(df))
print(sensibilidade(df, mediaNaoFumanteSW))

#contagens
print("contFumantesNW: %f" % contFumantesNW(df))
print(sensibilidade(df, contFumantesNW))
print("contFumanteSW: %f" % contFumanteSW(df))
print(sensibilidade(df, contFumanteSW))
print("contNaoFumantesNW: %f" % contNaoFumantesNW(df))
print(sensibilidade(df, contNaoFumantesNW))
print("contNaoFumanteSW: %f" % contNaoFumanteSW(df))
print(sensibilidade(df, contNaoFumanteSW))

#desvio-padrao
print("stdFumantesNW: %f" % stdFumantesNW(df))
print(sensibilidade(df, stdFumantesNW))
print("stdFumanteSW: %f" % stdFumanteSW(df))
print(sensibilidade(df, stdFumanteSW))
print("stdNaoFumantesNW: %f" % stdNaoFumantesNW(df))
print(sensibilidade(df, stdNaoFumantesNW))
print("stdNaoFumanteSW: %f" % stdNaoFumanteSW(df))
print(sensibilidade(df, stdNaoFumanteSW))


#pos-normalizacao
normalicao(df)

#chamar programa
listaMetricas = []

#medias
print("Valores pos-normalizacao")
print("mediaFumantesNW: %f" % mediaFumantesNW(df))
print(sensibilidade(df, mediaFumantesNW))
listaMetricas.append((mediaFumantesNW, mediaFumantesNW(df), sensibilidade(df, mediaFumantesNW))) #0
print("mediaFumanteSW %f" % mediaFumanteSW(df))
print(sensibilidade(df, mediaFumanteSW))
listaMetricas.append((mediaFumanteSW, mediaFumanteSW(df), sensibilidade(df, mediaFumanteSW))) #1
print("mediaNaoFumantesNW: %f" % mediaNaoFumantesNW(df))
print(sensibilidade(df, mediaNaoFumantesNW))
listaMetricas.append((mediaNaoFumantesNW, mediaNaoFumantesNW(df), sensibilidade(df, mediaNaoFumantesNW))) #2
print("mediaNaoFumanteSW: %f" % mediaNaoFumanteSW(df))
print(sensibilidade(df, mediaNaoFumanteSW))
listaMetricas.append((mediaNaoFumanteSW, mediaNaoFumanteSW(df), sensibilidade(df, mediaNaoFumanteSW))) #3

#contagens
print("contFumantesNW: %f" % contFumantesNW(df))
print(sensibilidade(df, contFumantesNW))
listaMetricas.append((contFumantesNW, contFumantesNW(df), sensibilidade(df, contFumantesNW))) #4
print("contFumanteSW: %f" % contFumanteSW(df))
print(sensibilidade(df, contFumanteSW))
listaMetricas.append((contFumanteSW, contFumanteSW(df), sensibilidade(df, contFumanteSW))) #5
print("contNaoFumantesNW: %f" % contNaoFumantesNW(df))
print(sensibilidade(df, contNaoFumantesNW))
listaMetricas.append((contNaoFumantesNW, contNaoFumantesNW(df), sensibilidade(df, contNaoFumantesNW))) #6
print("contNaoFumanteSW: %f" % contNaoFumanteSW(df))
print(sensibilidade(df, contNaoFumanteSW))
listaMetricas.append((contNaoFumanteSW, contNaoFumanteSW(df), sensibilidade(df, contNaoFumanteSW))) #7

#desvio-padrao
print("stdFumantesNW: %f" % stdFumantesNW(df))
print(sensibilidade(df, stdFumantesNW))
listaMetricas.append((stdFumantesNW, stdFumantesNW(df), sensibilidade(df, stdFumantesNW))) #8
print("stdFumanteSW: %f" % stdFumanteSW(df))
print(sensibilidade(df, stdFumanteSW))
listaMetricas.append((stdFumanteSW, stdFumanteSW(df), sensibilidade(df, stdFumanteSW))) #9
print("stdNaoFumantesNW: %f" % stdNaoFumantesNW(df))
print(sensibilidade(df, stdNaoFumantesNW))
listaMetricas.append((stdNaoFumantesNW, stdNaoFumantesNW(df), sensibilidade(df, stdNaoFumantesNW))) #10
print("stdNaoFumanteSW: %f" % stdNaoFumanteSW(df))
print(sensibilidade(df, stdNaoFumanteSW))
listaMetricas.append((stdNaoFumanteSW, stdNaoFumanteSW(df), sensibilidade(df, stdNaoFumanteSW))) #11

#print('t-test variaveis')
#rint('x1 - %f' % listaMetricas[0][1])
#print('x2 - %f' % listaMetricas[1][1])
#print('s1" - %f' % listaMetricas[8][1])
#print('s2 - %f' % listaMetricas[9][1])
#print('n1 - %f' % listaMetricas[4][1])
#print('n2 - %f' % listaMetricas[5][1])
#print(ttest(listaMetricas[0][1], listaMetricas[1][1], listaMetricas[8][1], listaMetricas[9][1], listaMetricas[4][1], listaMetricas[5][1])) 


listaEquacoes = []
tfum = (listaMetricas[0][1], listaMetricas[1][1], listaMetricas[8][1], listaMetricas[9][1], listaMetricas[4][1], listaMetricas[5][1])
tnfum = (listaMetricas[2][1], listaMetricas[3][1], listaMetricas[10][1], listaMetricas[11][1], listaMetricas[6][1], listaMetricas[7][1]) 

print('t-test ')
print('t-fumante: %f' % ttestcomTupla(df, tfum))
print('t-nfumante: %f'% ttestcomTupla(df, tnfum))


def gerarsequenciasvalidasrecursiva(listadesequencias, lista, nivel, nivelmax, epislonGlobal):
    if sum(lista) > epislonGlobal:
        return
    if nivel == nivelmax and sum(lista) != epislonGlobal:
        return
    if nivel == nivelmax and sum(lista) == epislonGlobal:
        listadesequencias.append(lista)
        return
    for i in range(1,21):
        listatemp = list(lista)
        listatemp.append(0.5*i)
        gerarsequenciasvalidasrecursiva(listadesequencias, listatemp, nivel+1, nivelmax, epislonGlobal)
    return


sequencias = []
gerarsequenciasvalidasrecursiva(sequencias, [], 0, 12, 12.0)
print('Total se sequencias %d\n' % len(sequencias))

print('Iniciando testes')
score = sys.float_info.max
for s in sequencias:
    print(s, end='; ')
    resultadosEstatisticas = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]  #12 estatisticas
    resultadosEquacoes = [0.0, 0.0]
    metrica = 0.0
    for i in range(0,1000):
        tempEstatistica = []
        for re in range(0,12):
            tempEstatistica.append(funcaoDP(listaMetricas[re][1], s[re], listaMetricas[re][2]))
            resultadosEstatisticas[re] = resultadosEstatisticas[re] + abs(tempEstatistica[re] - listaMetricas[re][1])
        
        tempEquacao = []
        tuplafum = (tempEstatistica[0], tempEstatistica[1], tempEstatistica[8], tempEstatistica[9], tempEstatistica[4], tempEstatistica[5])
        tuplanfum = (tempEstatistica[2], tempEstatistica[3], tempEstatistica[10], tempEstatistica[11], tempEstatistica[6], tempEstatistica[7])
        tempEquacao.append(ttestcomTupla(df, tuplafum))
        tempEquacao.append(ttestcomTupla(df, tuplanfum))
        resultadosEquacoes[0] = resultadosEquacoes[0] + abs(tempEquacao[0] - ttestcomTupla(df, tfum))
        resultadosEquacoes[1] = resultadosEquacoes[1] + abs(tempEquacao[1] - ttestcomTupla(df, tnfum))

    
    for f in resultadosEstatisticas:
        metrica = metrica + (f / 1000.0)

    metrica = metrica + (resultadosEquacoes[0] / 1000.0)
    metrica = metrica + (resultadosEquacoes[1] / 1000.0)

    if(score > metrica / 14.0):
        score = metrica / 14.0
    print(metrica / 14.0)

print("menor metrica %f" % score)