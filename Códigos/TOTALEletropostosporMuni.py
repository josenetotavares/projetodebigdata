import pandas as pd
import matplotlib.pyplot as plt

# Carregar o arquivo Excel
df = pd.read_excel('Eletropostos_por_Municipios_Corrigido.xlsx', engine='openpyxl')

# Limpar os dados: remover espaços em branco dos nomes das colunas e das linhas
df.columns = df.columns.str.strip()
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

# Criar manualmente o dataframe com os dados corrigidos
data = {
    'Município': ['São Paulo', 'Rio de Janeiro', 'Brasília', 'Curitiba', 'Porto Alegre', 'Goiânia', 'Florianópolis', 'Campinas', 'Fortaleza', 'Salvador'],
    'Estado': ['SP', 'RJ', 'DF', 'PR', 'RS', 'GO', 'SC', 'SP', 'CE', 'BA'],
    'AC (Recarga lenta)': [1586, 774, 397, 294, 252, 206, 198, 187, 190, 178],
    'OC (Recarga rápida)': [155, 74, 91, 94, 26, 35, 22, 29, 25, 28],
    'Total': [1741, 848, 488, 388, 278, 241, 220, 216, 215, 206],
    'MarketShare': ['11.74%', '5.72%', '3.29%', '2.62%', '1.87%', '1.63%', '1.48%', '1.46%', '1.45%', '1.39%']
}
df_corrected = pd.DataFrame(data)

# Gerar um gráfico de barras para o total de eletropostos por município
plt.figure(figsize=(12, 8))
plt.bar(df_corrected['Município'], df_corrected['Total'])
plt.xlabel('Município')
plt.ylabel('Total de Eletropostos')
plt.title('Total de Eletropostos por Município')
plt.xticks(rotation=90)
plt.tight_layout()

# Salvar o gráfico como um arquivo de imagem
plt.savefig('eletropostos_por_municipio.png')

# Mostrar o gráfico
plt.show()

# Salvar o dataframe corrigido em um novo arquivo Excel
df_corrected.to_excel('Eletropostos_por_Municipios_Corrigido.xlsx', index=False)
