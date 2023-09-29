import pandas as pd

# Carregue os dados do CSV em um DataFrame
df = pd.read_csv('C:/Users/Pulzi/Desktop/Determinante-Credito-Carbono-Simplificado-main/teste/Dados usados para o estudo do parque villa lobos - Copia.csv')

# Cabeçalho
print('-' * 74)
print(f'{"nomes":^6}   {"dap":^13}   {"altura":^10}   {"arvore":^12}')
print('-' * 74)

# Formate as colunas para terem o tamanho desejado
df['nomes'] = df['nomes'].astype(str).str.center(6)
df['dap'] = df['dap'].apply(lambda x: f'{x:,.2f}').str.rjust(13)
df['altura'] = df['altura'].apply(lambda x: f'{x:,.2f}').str.rjust(10)
df['arvore'] = df['arvore'].apply(lambda x: f'{x:,.2f}').str.rjust(12)

# Imprima a tabela formatada no terminal
for index, row in df.iterrows():
    print(f'{row["nomes"]}   {row["dap"]}   {row["altura"]}   {row["arvore"]}')

print('-' * 74)
