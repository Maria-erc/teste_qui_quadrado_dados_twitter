#analisando dados de vacinas

#importando pacotes
import pandas as pd
import numpy as np
from scipy import stats
from scipy.stats import chi2_contingency

#importando dados
dados_saude = pd.read_excel('saude.xlsx')
dados_segur = pd.read_excel('seguranca.xlsx')
dados_educa = pd.read_excel('educacao.xlsx')

#selecionando coluna sentiment que contém os sentimentos
saude = dados_saude[['sentiment']]
educacao = dados_educa[['sentiment']]
seguranca = dados_segur[['sentiment']]

lista = []
lista_dfs = [saude, seguranca, educacao]

#loop para contar a quantidade de cada sentimento de cada df da lista_dfs
for df in lista_dfs:
    positivo = 0
    neutro = 0
    negativo = 0
    for item in df['sentiment']:
        if item > 0:
            positivo += 1
        if item < 0:
            negativo += 1
        if item == 0:
            neutro += 1
        
    sentimentos = [positivo, neutro, negativo]
    lista.append(sentimentos)

#dataframe com sentimentos
df = pd.DataFrame(lista, columns=['positivo', 'neutro', 'negativo'], 
index=['saude', 'segurança', 'educaçao'])

#preparando dados para cálculo do teste qui-quadrado
#acrescentando coluna de soma
df['total_lin'] = df.sum(axis=1) 

#acrescentando linha de soma
df.loc['total_col'] = [df.iloc[:, 0].sum(axis=0), df.iloc[:, 1].sum(axis=0), 
                       df.iloc[:, 2].sum(axis=0), df.iloc[:, 3].sum(axis=0)]

print('data frame de sentimentos')
print(df)

#dados observados
dados_observados = df.iloc[0:3, 0:3] # dados sem os totais

#dados esperados
dados_esperados = np.outer(df['total_lin'][0:3], df.loc['total_col'][0:3]) / 300
dados_esperados = pd.DataFrame(dados_esperados)
dados_esperados.columns = ['positivo', 'neutro', 'negativo']
dados_esperados.index = ['saude', 'segurança', 'educação']

#qui quadrado, valorp, graus de liberdade e os valores esperados
print('\nquadro de análise:')
print(stats.chi2_contingency(observed= dados_observados))