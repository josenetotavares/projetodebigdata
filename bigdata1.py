import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Dicionário de mapeamento dos meses em português para o número correspondente
meses_pt_br = {
    "janeiro": "01", "fevereiro": "02", "março": "03", "abril": "04", "maio": "05",
    "junho": "06", "julho": "07", "agosto": "08", "setembro": "09", "outubro": "10",
    "novembro": "11", "dezembro": "12"
}

# Função para substituir o mês por número
def substituir_mes_por_numero(mes_ano):
    mes, ano = mes_ano.split('/')
    mes_numero = meses_pt_br.get(mes.lower(), None)
    if mes_numero:
        return f'{mes_numero}/{ano}'
    else:
        return mes_ano  # Caso não encontre, retorna o valor original

# Dados
dados = {
    "Mês/Ano": [
        "março/25", "fevereiro/25", "janeiro/25", "dezembro/24", "novembro/24", 
        "outubro/24", "setembro/24", "agosto/24", "julho/24", "junho/24", 
        "maio/24", "abril/24", "março/24", "fevereiro/24", "janeiro/24", 
        "dezembro/23", "novembro/23", "outubro/23", "setembro/23", "agosto/23", 
        "julho/23", "junho/23", "maio/23", "abril/23", "março/23", "fevereiro/23", 
        "janeiro/23", "dezembro/22", "novembro/22", "outubro/22", "setembro/22", 
        "agosto/22", "julho/22", "junho/22", "maio/22", "abril/22", "março/22", 
        "fevereiro/22", "janeiro/22"
    ],
    "BEV": [
        4801, 4492, 3700, 4368, 5417, 6109, 4699, 5115, 4703, 5190, 
        5175, 6705, 6137, 3639, 4358, 6018, 3197, 2370, 1830, 1167, 
        950, 618, 615, 565, 587, 638, 755, 897, 727, 637, 1412, 949, 
        442, 1090, 556, 459, 520, 402, 366
    ],
    "PHEV": [
        6944, 5884, 6701, 10521, 6922, 5961, 4869, 5781, 6659, 5047, 
        3882, 3735, 3128, 3594, 3910, 5353, 4003, 3429, 3028, 3700, 
        2597, 2394, 2424, 1162, 2095, 1227, 1637, 1290, 802, 1158, 
        2288, 884, 837, 859, 836, 701, 506, 691, 651
    ],
    "HEV": [
        979000, 1148000, 1545000, 1622000, 1330000, 1391000, 1235000, 1323000, 
        977000, 1239000, 1360000, 1454000, 1221000, 869000, 1251000, 1478000, 
        1017000, 1006000, 794000, 1028000, 1000000, 523000, 482000, 233000, 
        346000, 296000, 108000, 191000, 142000, 66000, 287000, 184000, 
        157000, 198000, 257000, 76000, 38000, 212000, 191000
    ],
    "Total": [
        17909, 16237, 16502, 21634, 17143, 16033, 13265, 14667, 15312, 
        14396, 13612, 15206, 13613, 10451, 12026, 16279, 10601, 9537, 
        8458, 9351, 7462, 6225, 6435, 4793, 5989, 4294, 4503, 5586, 
        4995, 4460, 6391, 4249, 3136, 4073, 3387, 3124, 3851, 3435, 2557
    ]
}

# Criando o DataFrame
df = pd.DataFrame(dados)

# Substituindo os meses por números
df['Mês/Ano'] = df['Mês/Ano'].apply(substituir_mes_por_numero)

# Convertendo para datetime
df['Mês/Ano'] = pd.to_datetime(df['Mês/Ano'], format='%m/%y')

# Usando o Seaborn para melhorar o estilo do gráfico
sns.set(style="whitegrid")

# Plotando os gráficos
plt.figure(figsize=(12, 8))

# Plotando cada tipo de veículo com cores e marcadores diferentes
plt.plot(df['Mês/Ano'], df['BEV'], label='BEV', marker='o', color='blue', markersize=6, linewidth=2)
plt.plot(df['Mês/Ano'], df['PHEV'], label='PHEV', marker='x', color='orange', markersize=6, linewidth=2)
plt.plot(df['Mês/Ano'], df['HEV'], label='HEV', marker='s', color='green', markersize=6, linewidth=2)
plt.plot(df['Mês/Ano'], df['Total'], label='Total', marker='d', color='red', markersize=6, linewidth=2)

# Personalizando o gráfico
plt.xlabel('Mês/Ano', fontsize=14)
plt.ylabel('Quantidade de Veículos', fontsize=14)
plt.title('Evolução de Tipos de Veículos (BEV, PHEV, HEV) e Total ao Longo do Tempo', fontsize=16)
plt.xticks(rotation=45, ha='right')
plt.legend(title='Categorias', fontsize=12)
plt.tight_layout()

# Exibindo o gráfico
plt.show()


