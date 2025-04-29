import pandas as pd
import matplotlib.pyplot as plt

# Carregar o arquivo Excel
df = pd.read_excel('Vendas_de_veiculos_eletrificados.xlsx', engine='openpyxl')

# Ordenar os dados pela quantidade em ordem decrescente para melhor visualização
df_sorted = df.sort_values(by='Quantidade', ascending=False)

# Selecionar os 10 principais modelos para um gráfico mais conciso
df_top10 = df_sorted.head(10)

# Plotar os dados
plt.figure(figsize=(12, 8))
bars = plt.bar(df_top10['Modelo'], df_top10['Quantidade'], color='skyblue')
plt.xlabel('Modelos')
plt.ylabel('Quantidade de Vendas')
plt.title('Top 10 Vendas de Veículos Eletrificados')
plt.xticks(rotation=45)

# Adicionar rótulos de dados no topo das barras
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.5, round(yval, 2), ha='center', va='bottom')

plt.tight_layout()

# Salvar o gráfico como um arquivo de imagem
plt.savefig('top10_vendas_veiculos_eletrificados.png')

# Mostrar o gráfico
plt.show()
