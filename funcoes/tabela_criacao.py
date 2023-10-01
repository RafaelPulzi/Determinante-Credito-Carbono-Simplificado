import os
from openpyxl import Workbook

def criar_tabela():
    diretorio = "./Tabelas"  # Diretório atual, você pode alterar se desejar
    nome_base = "BDinfoArvores"
    extensao = ".xlsx"
    contador = 1

    while True:
        nome_tabela = f"{nome_base}_{contador}{extensao}"
        caminho_tabela = os.path.join(diretorio, nome_tabela)
        if not os.path.exists(caminho_tabela):
            tabela = Workbook()
            bdarvores_page = tabela.create_sheet('bdArvores')
            bdarvores_page.append(['arvore', 'dap', 'altura'])  # Adicione os cabeçalhos à nova tabela
            tabela.save(filename=caminho_tabela)
            return caminho_tabela
        contador += 1