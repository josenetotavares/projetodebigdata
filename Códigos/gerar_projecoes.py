import pandas as pd

# Projeção: Veículos elétricos e eletropostos (2022 a 2035)
anos = list(range(2022, 2026)) + list(range(2026, 2036))
veiculos = [10581, 103711, 158407, 54739] + [127915, 147081, 166246, 185412, 204577, 223742, 242908, 262073, 281239, 300404]
eletropostos = [10000, 15000, 18000, 20000] + [22000, 25000, 28000, 31000, 34000, 37000, 40000, 43000, 46000, 49000]

df_proj_veiculos = pd.DataFrame({
    'Ano': anos,
    'Veiculos': veiculos,
    'Eletropostos': eletropostos
})
df_proj_veiculos.to_csv('Projecao_Veiculos_Eletropostos.csv', index=False)

# Projeção de CO₂ evitado (2026 a 2030)
df_proj_co2 = pd.DataFrame({
    'Ano': list(range(2026, 2031)),
    'CO2_Evitado_ton': [294204.50, 338285.38, 382366.26, 426447.14, 470528.02]
})
df_proj_co2.to_csv('Projecao_CO2_Evitado.csv', index=False)

# Projeção de preços médios (2026 a 2030)
df_proj_preco = pd.DataFrame({
    'Ano': list(range(2026, 2031)),
    'Preco_Medio_R$mil': [210.0, 200.0, 190.0, 180.0, 170.0]
})
df_proj_preco.to_csv('Projecao_Preco_Medio.csv', index=False)

print("Arquivos gerados com sucesso!")
