import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

# Dados manuais extraídos dos prints
dados_veiculos = {
    'Ano': [2022]*2 + [2023]*12 + [2024]*12 + [2025]*4,
    'Mes': ['novembro', 'dezembro'] + ['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro'] +
           ['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro'] +
           ['janeiro','fevereiro','março','abril'],
    'Total': [4995, 5586, 4204, 4294, 5989, 6433, 6356, 6225, 7462, 9351, 8458, 9537,
              13163, 16279, 12026, 10451, 13613, 15206, 13612, 14396, 15312, 14674,
              14467, 16033, 17143, 12612, 12988, 14380, 14759, 0]  # corrigido aqui
}


dados_eletropostos = {
    'Ano': [2022, 2023, 2023, 2023, 2023, 2023, 2023, 2023, 2023, 2024, 2024, 2024, 2024, 2024, 2025],
    'Mes': ['outubro', 'maio', 'junho', 'agosto', 'dezembro', 'março', 'julho', 'agosto', 'novembro',
            'março', 'julho', 'agosto', 'novembro', 'fevereiro', 'fevereiro'],
    'Total': [2862, 3200, 3503, 3800, 4300, 7758, 8800, 10622, 12137,
              7758, 8800, 10622, 12137, 12888, 14827]
}

# Criar DataFrames
df_veiculos = pd.DataFrame(dados_veiculos)
df_eletropostos = pd.DataFrame(dados_eletropostos)

# Agrupar por ano (somando os totais)
veiculos_ano = df_veiculos.groupby('Ano')['Total'].sum().reset_index(name='Veiculos')
eletropostos_ano = df_eletropostos.groupby('Ano')['Total'].sum().reset_index(name='Eletropostos')

# Criar dataframe com dados reais combinados (para anos que existem em ambos)
df_real = pd.merge(veiculos_ano, eletropostos_ano, on='Ano', how='outer').sort_values('Ano').reset_index(drop=True)

# Regressão Linear - Veículos
X_v = veiculos_ano[['Ano']]
y_v = veiculos_ano['Veiculos']
modelo_v = LinearRegression().fit(X_v, y_v)

# Regressão Linear - Eletropostos
X_e = eletropostos_ano[['Ano']]
y_e = eletropostos_ano['Eletropostos']
modelo_e = LinearRegression().fit(X_e, y_e)

# Previsão para os próximos 10 anos (2026 a 2035)
anos_futuros = np.arange(2026, 2036).reshape(-1, 1)
proj_veiculos = modelo_v.predict(anos_futuros)
proj_eletropostos = modelo_e.predict(anos_futuros)

# Criar DataFrame com projeções
df_proj = pd.DataFrame({
    'Ano': anos_futuros.flatten(),
    'Veiculos': proj_veiculos,
    'Eletropostos': proj_eletropostos
})

# Concatenar dados reais e projetados
df_final = pd.concat([df_real, df_proj], ignore_index=True)

# Plotar gráfico
plt.figure(figsize=(12, 6))
plt.plot(df_final['Ano'], df_final['Veiculos'], marker='o', label='Veículos Elétricos Vendidos')
plt.plot(df_final['Ano'], df_final['Eletropostos'], marker='s', label='Eletropostos')
plt.title('Projeção de 10 Anos: Veículos Elétricos vs. Eletropostos')
plt.xlabel('Ano')
plt.ylabel('Quantidade')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()