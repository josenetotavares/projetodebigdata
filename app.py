import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

st.set_page_config(layout="wide", page_title="Dashboard de Eletromobilidade")

# TÍTULO E INTRODUÇÃO
st.title("🚗📊 Dashboard de Eletromobilidade no Brasil: Projeções até 2035")
st.markdown("""
Este dashboard interativo apresenta **dados reais e projeções futuras** sobre:
- Crescimento de veículos elétricos e eletropostos
- Impacto ambiental (redução de CO₂)
- Queda no preço médio dos veículos

As informações são baseadas em dados da **ABVE** e em modelos de **regressão linear** para estimar as tendências até **2035**.
""")

# =====================
# DADOS E PROJEÇÕES: VEÍCULOS E ELETROPOSTOS
# =====================
dados_veiculos = {
    'Ano': [2022]*2 + [2023]*12 + [2024]*12 + [2025]*4,
    'Mes': ['novembro', 'dezembro'] + ['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro'] +
           ['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro'] +
           ['janeiro','fevereiro','março','abril'],
    'Total': [4995, 5586, 4204, 4294, 5989, 6433, 6356, 6225, 7462, 9351, 8458, 9537,
              13163, 16279, 12026, 10451, 13613, 15206, 13612, 14396, 15312, 14674,
              14467, 16033, 17143, 12612, 12988, 14380, 14759, 0]
}

dados_eletropostos = {
    'Ano': [2022, 2023, 2023, 2023, 2023, 2023, 2023, 2023, 2023, 2024, 2024, 2024, 2024, 2024, 2025],
    'Mes': ['outubro', 'maio', 'junho', 'agosto', 'dezembro', 'março', 'julho', 'agosto', 'novembro',
            'março', 'julho', 'agosto', 'novembro', 'fevereiro', 'fevereiro'],
    'Total': [2862, 3200, 3503, 3800, 4300, 7758, 8800, 10622, 12137,
              7758, 8800, 10622, 12137, 12888, 14827]
}

veic_df = pd.DataFrame(dados_veiculos)
eletro_df = pd.DataFrame(dados_eletropostos)

veiculos_ano = veic_df.groupby('Ano')['Total'].sum().reset_index(name='Veiculos')
eletropostos_ano = eletro_df.groupby('Ano')['Total'].sum().reset_index(name='Eletropostos')

df_real = pd.merge(veiculos_ano, eletropostos_ano, on='Ano', how='outer').sort_values('Ano').reset_index(drop=True)

# Projeções lineares
modelo_v = LinearRegression().fit(veiculos_ano[['Ano']], veiculos_ano['Veiculos'])
modelo_e = LinearRegression().fit(eletropostos_ano[['Ano']], eletropostos_ano['Eletropostos'])

anos_futuros = np.arange(2026, 2036).reshape(-1, 1)
proj_veiculos = modelo_v.predict(anos_futuros)
proj_eletropostos = modelo_e.predict(anos_futuros)

proj_df = pd.DataFrame({
    'Ano': anos_futuros.flatten(),
    'Veiculos': proj_veiculos,
    'Eletropostos': proj_eletropostos
})

df_total = pd.concat([df_real, proj_df], ignore_index=True)

# Gráfico de crescimento
st.header("🚘 Crescimento de Veículos Elétricos e Eletropostos (2022–2035)")
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(df_total['Ano'], df_total['Veiculos'], marker='o', label='Veículos Elétricos')
ax.plot(df_total['Ano'], df_total['Eletropostos'], marker='s', label='Eletropostos')
ax.set_xlabel("Ano")
ax.set_ylabel("Quantidade")
ax.set_title("Projeção de Crescimento")
ax.grid(True)
ax.legend()
st.pyplot(fig)
st.markdown("""
Este gráfico mostra a evolução real e a tendência futura da eletromobilidade no Brasil.  
As projeções (2026–2035) foram estimadas com **regressão linear** com base nos dados de 2022–2025.
""")

# Tabela de dados real + projeções
st.subheader("📊 Dados Completos: Veículos Elétricos e Eletropostos por Ano")
st.dataframe(df_total.style.format({'Veiculos': '{:.0f}', 'Eletropostos': '{:.0f}'}), use_container_width=True)

# =====================
# PROJEÇÃO DE CO2 EVITADO
# =====================
df_co2 = pd.read_excel("Projecoes/co2_evitado.xlsx")
df_co2 = df_co2.sort_values("Ano")

st.header("🌍 Projeção de CO₂ Evitado com Carros Elétricos")
fig2, ax2 = plt.subplots(figsize=(10, 5))
ax2.plot(df_co2['Ano'], df_co2['CO2_Evitado_ton'], marker='o', color='green')
ax2.set_title("CO₂ Evitado (em toneladas)")
ax2.set_xlabel("Ano")
ax2.set_ylabel("Toneladas de CO₂")
ax2.grid(True)
st.pyplot(fig2)
st.markdown("""
A projeção considera que **cada carro elétrico evita cerca de 1,5 tonelada de CO₂ por ano**.  
Com a expansão da frota, estima-se uma economia ambiental significativa até 2035.
""")

# =====================
# PREÇO MÉDIO DOS VEÍCULOS
# =====================
df_preco = pd.read_excel("Projecoes/preco_medio_veiculos.xlsx")
df_preco = df_preco.sort_values("Ano")

st.header("💰 Evolução do Preço Médio dos Veículos Elétricos no Brasil")
fig3, ax3 = plt.subplots(figsize=(10, 5))
ax3.plot(df_preco['Ano'], df_preco['Preco_Medio_R$'], marker='s', color='orange')
ax3.set_title("Preço Médio dos Carros Elétricos (R$)")
ax3.set_xlabel("Ano")
ax3.set_ylabel("R$")
ax3.grid(True)
st.pyplot(fig3)
st.markdown("""
Os dados indicam uma tendência de **queda gradual no preço médio** dos veículos elétricos.  
Esse fenômeno é impulsionado por avanços tecnológicos e aumento da produção em escala.
""")

# =====================
# RODAPÉ
# =====================
st.markdown("---")
st.markdown("""
Desenvolvido por **Luiz Felipe Barreto Silveira, José Angelo Tavares Neto, Everton Vitena Azevedo Da Conceição , Levi, Rui Romer Cupertino Sacramento Junior**.  
Trabalho acadêmico de Big Data com foco em eletromobilidade no Brasil.  
Fontes: **ABVE** e projeções próprias com base em análise de dados.
""")
