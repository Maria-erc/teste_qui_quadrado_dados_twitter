# teste_qui_quadrado_dados_twitter
Teste qui-quadrado de Pearson em dados oriundos do Twitter 


## Dados do Twitter
Primeiramente, utilizei o software Orange Data Mining, que através de uma API do Twitter, extraí tweets com essas 3 tags diferentes: "saúde púplica", "educação pública" e "segurança pública".  

Com o próprio Orange foi possível fazer a limpeza dos dados, retirando palavras desnecessárias dos tweets e também fazer uma análise de sentimentos, classificando cada tweet com uma numeração. Nessa classificação, números negativos, nulos e positivos simbolizam sentimentos negativos, neutros e positivos, respectivamente.
Essa análise de cada tag foi transferida para um arquivo csv.

## Objetivo
O objetico de usar esse modelo estatítico de Pearson foi para testar duas hipóteses:
- Hipótese nula: não há diferença de sentimentos em relação a essas três áreas governamentais
- Hipótese alternativa: há diferença de sentimentos em relação a essas três áreas governamentais

## Teste qui-quadrado de Pearson

Acrescentei no dataframe "df" o total de linhas e colunas, porque será preciso para o modelo estatístico.

~~~
df['total_lin'] = df.sum(axis=1) 

df.loc['total_col'] = [df.iloc[:, 0].sum(axis=0), df.iloc[:, 1].sum(axis=0), 
                       df.iloc[:, 2].sum(axis=0), df.iloc[:, 3].sum(axis=0)]
~~~~


Depois defini os dados observados, que são a contagem de sentimentos de cada tag, e os dados esperados, que são a multiplicação do total de linha pelo total de coluna, dividido pelo total.

~~~
dados_observados = df.iloc[0:3, 0:3]

dados_esperados = np.outer(df['total_lin'][0:3], df.loc['total_col'][0:3]) / 300
dados_esperados = pd.DataFrame(dados_esperados)
dados_esperados.columns = ['positivo', 'neutro', 'negativo']
dados_esperados.index = ['saude', 'segurança', 'educação']
~~~

Por fim, utilizei duas formas de calcular o test qui-quadrado.
- Calculando "na mão":
 ~~~
 qui_quadrado =  ((dados_observados-dados_esperados)**2/dados_esperados).sum().sum()
 print('\nqui quadrado')
 print(qui_quadrado)
 ~~~
 
 - Usando o módulo stats do python:
 ~~~
 print('\nquadro de análise:')
 print(stats.chi2_contingency(observed= dados_observados))
 ~~~
 Esse comando devolve o valor qui-quadrado, valor-p, graus de liberdade e os valores esperados.
 
 ## Conclusão
 
 O qui-quadrado caluclado (Xc) é aproximadamente 40.259226006191945.
 Utilizando o valor-p e os graus de liberdade, observou-se que o qui-quadrado tabelado (Xt) é 9,488.
 
 Assim Xc > Xe, rejeitando a Ho.
 
 Logo, prova-se estatisticamente que há diferença de sentimetnos, ou seja, há um descontentamento maior por determinada área do que as demais. 


