import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
import numpy as np

# Carregar os arquivos Excel
df_vendas = pd.read_excel('Vendas_por_municipios.xlsx', engine='openpyxl')
df_eletropostos = pd.read_excel('Eletropostos_por_Municipios_Corrigido.xlsx', engine='openpyxl')

# Limpar os dados: remover espaços em branco dos nomes das colunas e das linhas
df_vendas.columns = df_vendas.columns.str.strip()
df_vendas = df_vendas.applymap(lambda x: x.strip() if isinstance(x, str) else x)

df_eletropostos.columns = df_eletropostos.columns.str.strip()
df_eletropostos = df_eletropostos.applymap(lambda x: x.strip() if isinstance(x, str) else x)

# Mesclar os dataframes em 'Município' e 'Estado'
df_merged = pd.merge(df_vendas, df_eletropostos, on=['Município', 'Estado'])

# Converter as colunas 'Quantidade' e 'Total' para numérico, forçando erros para NaN
df_merged['Quantidade'] = pd.to_numeric(df_merged['Quantidade'], errors='coerce')
df_merged['Total'] = pd.to_numeric(df_merged['Total'], errors='coerce')

# Remover linhas com valores NaN nas colunas 'Quantidade' ou 'Total'
df_merged = df_merged.dropna(subset=['Quantidade', 'Total'])

# Ordenar o dataframe por 'Quantidade' para garantir que as linhas sejam plotadas corretamente
df_merged = df_merged.sort_values(by='Quantidade')

# Gerar um gráfico de linhas para a relação entre vendas de veículos e eletropostos
plt.figure(figsize=(14, 10))
sns.lineplot(data=df_merged, x='Quantidade', y='Total', marker='o')

# Anotar cada ponto com o nome da cidade
for i in range(df_merged.shape[0]):
    plt.text(df_merged['Quantidade'].iloc[i], df_merged['Total'].iloc[i], df_merged['Município'].iloc[i], fontsize=9)

plt.xlabel('Quantidade de Veículos Vendidos')
plt.ylabel('Total de Eletropostos')
plt.title('Relação entre Vendas de Veículos e Eletropostos por Município')
plt.grid(True)
plt.tight_layout()

# Salvar o gráfico como um arquivo de imagem
plt.savefig('relacao_vendas_eletropostos_linhas_anotado.png')

# Mostrar o gráfico
plt.show()

# Projeção de 10 anos

# Adicionar uma coluna de ano ao dataframe
df_merged['Ano'] = 2023

# Criar um dataframe para armazenar as projeções
df_projecao = pd.DataFrame()

for municipio in df_merged['Município'].unique():
    df_municipio = df_merged[df_merged['Município'] == municipio]
    
    # Ajustar um modelo de regressão linear para prever a quantidade de veículos vendidos e o total de eletropostos
    modelo_quantidade = LinearRegression()
    modelo_total = LinearRegression()
    
    X = np.array(df_municipio['Ano']).reshape(-1, 1)
    y_quantidade = df_municipio['Quantidade']
    y_total = df_municipio['Total']
    
    modelo_quantidade.fit(X, y_quantidade)
    modelo_total.fit(X, y_total)
    
    # Fazer previsões para os próximos 10 anos
    anos_futuros = np.arange(2024, 2034).reshape(-1, 1)
    previsoes_quantidade = modelo_quantidade.predict(anos_futuros)
    previsoes_total = modelo_total.predict(anos_futuros)
    
    # Criar um dataframe com as previsões e adicionar ao dataframe de projeções
    df_previsoes = pd.DataFrame({
        'Município': municipio,
        'Ano': anos_futuros.flatten(),
        'Quantidade': previsoes_quantidade,
        'Total': previsoes_total
    })
    
    df_projecao = pd.concat([df_projecao, df_previsoes])

# Concatenar o dataframe original com o dataframe de projeções
df_final = pd.concat([df_merged, df_projecao])

# Gerar um gráfico de linhas para a relação entre vendas de veículos e eletropostos com projeções
plt.figure(figsize=(14, 10))
sns.lineplot(data=df_final, x='Ano', y='Quantidade', hue='Município', marker='o')

plt.xlabel('Ano')
plt.ylabel('Quantidade de Veículos Vendidos')
plt.title('Projeção de 10 Anos da Relação entre Vendas de Veículos e Eletropostos por Município')
plt.grid(True)
plt.tight_layout()

# Salvar o gráfico como um arquivo de imagem
plt.savefig('projecao_vendas_eletropostos_linhas.png')

# Mostrar o gráfico
plt.show()
