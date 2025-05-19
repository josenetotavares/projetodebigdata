import pandas as pd
import matplotlib.pyplot as plt

# Carregar o arquivo Excel
df = pd.read_excel('Vendas_Grupo_de_veiculos_eletrificados.xlsx', engine='openpyxl')

# Limpar os dados: remover espaços em branco dos nomes das colunas e das linhas
df.columns = df.columns.str.strip()
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

# Converter a coluna 'Quantidade' para numérico, forçando erros para NaN
df['Quantidade'] = pd.to_numeric(df['Quantidade'], errors='coerce')

# Remover linhas com valores NaN na coluna 'Quantidade'
df = df.dropna(subset=['Quantidade'])

# Gerar um gráfico de barras para a quantidade de veículos vendidos por fabricante
plt.figure(figsize=(12, 8))
plt.bar(df['Fabricante'], df['Quantidade'])
plt.xlabel('Fabricante')
plt.ylabel('Quantidade')
plt.title('Quantidade de Veículos Vendidos por Fabricante')
plt.xticks(rotation=90)
plt.tight_layout()

# Salvar o gráfico como um arquivo de imagem
plt.savefig('vendas_por_fabricante.png')

# Mostrar o gráfico
plt.show()
