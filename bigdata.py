import pandas as pd



caminho_arquivo = ("CarrosEletricos.xlsx.xlsx")
tabela = pd.read_excel(caminho_arquivo)


print(tabela)
