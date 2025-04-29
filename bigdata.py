import pandas as pd
import matplotlib.pyplot as plt

# Ler o arquivo
caminho_arquivo = r"C:\Users\José Angelo\Documents\projetodebigdata\Serie_Historica_de_Veículos_Elétrificados_(2022-2025).xlsx"
tabela = pd.read_excel(caminho_arquivo)

# Inverter para mostrar do mês mais antigo para o mais recente
tabela = tabela.iloc[::-1]

# Criar o gráfico
plt.figure(figsize=(14, 8))

# Plotar cada tipo de veículo com uma cor
plt.plot(tabela['Mês/Ano'], tabela['BEV'], marker='o', label='BEV (100% elétrico)', color='deepskyblue')
plt.plot(tabela['Mês/Ano'], tabela['PHEV'], marker='o', label='PHEV (híbrido plug-in)', color='limegreen')
plt.plot(tabela['Mês/Ano'], tabela['HEV'], marker='o', label='HEV (híbrido comum)', color='orange')
plt.plot(tabela['Mês/Ano'], tabela['HEV FLEX'], marker='o', label='HEV FLEX (híbrido flex)', color='gold')
plt.plot(tabela['Mês/Ano'], tabela['MHEV'], marker='o', label='MHEV (híbrido leve)', color='violet')
plt.plot(tabela['Mês/Ano'], tabela['Total'], marker='o', label='Total de Veículos', color='black', linewidth=3, linestyle='--')

# Configurações do gráfico
plt.title('Evolução dos Veículos Elétricos por Tipo', fontsize=18)
plt.xlabel('Mês/Ano', fontsize=14)
plt.ylabel('Quantidade de Veículos', fontsize=14)
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(fontsize=12)
plt.tight_layout()
plt.show()


