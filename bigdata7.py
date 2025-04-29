import pandas as pd
import matplotlib.pyplot as plt

# Carregar o arquivo Excel
df = pd.read_excel('Evolução_de_Eletropostos_Corrigido.xlsx', engine='openpyxl')

# Limpar os dados: remover espaços em branco dos nomes das colunas e das linhas
df.columns = df.columns.str.strip()
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

# Criar manualmente o dataframe com os dados corrigidos
data = {
    'Ano': [2025, 2024, 2024, 2024, 2024, 2023, 2023, 2023, 2023, 2022, 2022, 2021, 2021],
    'Mês': ['fevereiro', 'novembro', 'agosto', 'julho', 'março', 'dezembro', 'agosto', 'junho', 'maio', 'outubro', 'fevereiro', 'dezembro', 'março'],
    'Total': [14827, 12137, 10622, 8800, 7758, 4300, 3800, 3503, 3200, 2862, 1250, 800, 500],
    'Evolucao': [22.16, 14.26, 20.70, 13.43, 80.42, 13.16, 8.48, 9.47, 11.81, 128.96, 56.25, 60.00, 42.86]
}
df_corrected = pd.DataFrame(data)

# Gerar um gráfico de linha para a evolução dos eletropostos ao longo do tempo
plt.figure(figsize=(12, 8))
plt.plot(df_corrected['Ano'].astype(str) + ' ' + df_corrected['Mês'], df_corrected['Total'], marker='o')
plt.xlabel('Ano Mês')
plt.ylabel('Total de Eletropostos')
plt.title('Evolução de Eletropostos')
plt.xticks(rotation=45)
plt.tight_layout()

# Salvar o gráfico como um arquivo de imagem
plt.savefig('evolucao_de_eletropostos.png')

# Mostrar o gráfico
plt.show()

# Salvar o dataframe corrigido em um novo arquivo Excel
df_corrected.to_excel('Evolução_de_Eletropostos_Corrigido.xlsx', index=False)
