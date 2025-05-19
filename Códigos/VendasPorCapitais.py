import pandas as pd
import matplotlib.pyplot as plt

# Carregar o arquivo Excel
df = pd.read_excel('Vendas_por_Capitais (1).xlsx', engine='openpyxl')

# Limpar os dados: remover espaços em branco dos nomes das colunas e das linhas
df.columns = df.columns.str.strip()
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

# Converter a coluna 'Quantidade' para numérico, forçando erros para NaN
df['Quantidade'] = pd.to_numeric(df['Quantidade'], errors='coerce')

# Remover linhas com valores NaN na coluna 'Quantidade'
df = df.dropna(subset=['Quantidade'])

# Gerar um gráfico de barras para a quantidade de veículos vendidos por capitais
plt.figure(figsize=(12, 8))
plt.bar(df['Capitais'], df['Quantidade'])
plt.xlabel('Capitais')
plt.ylabel('Quantidade')
plt.title('Quantidade de Veículos Vendidos por Capitais')
plt.xticks(rotation=90)
plt.tight_layout()

# Salvar o gráfico como um arquivo de imagem
plt.savefig('vendas_por_capitais.png')

# Mostrar o gráfico
plt.show()
