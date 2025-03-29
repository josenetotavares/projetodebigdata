import pandas as pd
import matplotlib.pyplot as plt



caminho_arquivo = r"C:\Users\José Angelo\Documents\projetodebigdata\taxa_rendimento_territorios-29-2023-EM.xlsx"
tabela = pd.read_excel(caminho_arquivo, sheet_name="estado")

tabela = tabela.dropna(subset=["aprovados","reprovados","abandonos"])

df_grouped = tabela.groupby("dependencia_id")[["aprovados","reprovados","abandonos"]].mean()

df_grouped.plot(kind="bar", stacked=True, colormap="viridis", figsize=(10,6))

plt.xlabel("Denpendência ID")
plt.ylabel("Percentual (%)")
plt.title("Taxa De Aprovados, Reprovados e Abandonos por Dependência ID")
plt.legend(title="Categoria")
plt.xticks(rotation=0)

plt.show(block=True)

