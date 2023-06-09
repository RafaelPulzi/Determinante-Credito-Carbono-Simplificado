import random
from time import sleep
import pandas as pd
import requests
from openpyxl import Workbook

#Criacao de uma planilha
tabela = Workbook()
tabela.create_sheet('bdArvores')
bdarvores_page = tabela['bdArvores']

#Adicionando dados na tabela
bdarvores_page.append(['arvore', 'dap', 'altura'])
arvore = arvoresParaFor = 0

response = requests.get("https://api.coinbase.com/v2/prices/MCO2-BRL/spot")
data = response.json()
preco = float(data["data"]["amount"])

dados = {}



while True:
    print('''
            ======================================
                EMPREENDER CREDITOS DE CARBONO
            ======================================''')
    print('''
    [1] Quanto ganharia em creditos de carbono fazendo uma floresta (incluindo custos)
    [2] Qual foi sua absorcao total de CO2 + Quanto sua floresta gerou de creditos de carbono
    [0] Sair do Programa
    ''')
    escolherTratamento = int(input('Qual opcao voce deseja escolher: '))
    if escolherTratamento == 1:
        print('''
            ======================================
                  INGRESSAR GANHO DE CREDITOS
            ======================================''')
        while True:
            
            print('''
            DIGITE 0 Caso deseje voltar ao menu

            Escolha a sua especie;
            [1] Jatoba-da-Mata
            [2] Guapuruvu
            [3] Pau-jacaré\n''')

            especie = int(input('Qual especie de arvore deseja escolher: '))

            if especie == 1:
                dados = {'especie': 'Jatoba-da-Mata', 'espacoOcupadoM': 6.25, 'absorveCO2/ano': 0.12, 'precoSemente': 3, 'crecimentoMaximo/anos': 10}
            elif especie == 2:
                dados = {'especie': 'Guapuruvu', 'espacoOcupadoM': 2.10, 'absorveCO2/ano': 0.04, 'precoSemente': 0.75, 'crecimentoMaximo/anos': 21}
            elif especie == 3:
                 dados = {'especie': 'Pau-jacaré', 'espacoOcupadoM': 2.60, 'absorveCO2/ano': 0.04, 'precoSemente': 1.6, 'crecimentoMaximo/anos': 15}
            elif especie == 0:
                break
            else:
                print('[ERRO] NUMERO DIGITADO E INVALIDO, TENTE NOVAMENTE\n')

            area = float(input('Qual e a area que voce tem disponivel para a plantacao (m): '))

            N_Arvores = area/dados['espacoOcupadoM']
            gastos = N_Arvores*dados['precoSemente']
            tempoDeAbsorcao = dados['absorveCO2/ano']*N_Arvores*dados['crecimentoMaximo/anos']
            creditosDeCarbono = tempoDeAbsorcao/1000

            print(f'Numero de arvores que seram plantadas: {N_Arvores} Arvores')
            print(f'Voce ira gastar um total de: R${gastos}')
            print(f'Em {dados["crecimentoMaximo/anos"]} anos, voce tera absorvido; {tempoDeAbsorcao} T/Co2 ')
            print(f'Gerando em creditos de carbono (MCO2) um total de: R${creditosDeCarbono*preco}')

    elif escolherTratamento == 2:
        print('''
            ======================================
                MEDICAO DE CARBONO NAS ARVORES
            ======================================''')

        print('''
        Todos os valores digitados seram interpretados em uma tabela em ecxel, assim sendo, toda vez que um looping terminar os dados serao enviados para a tabela, assim que 
        finalizar o programa as tabelas junto de suas interpretacoes seram liberadas para download\n''')
        while True:
            
            arvoresDoLaco = quantidadeArvores = int(input('Quantas arvores temos dessa especie: '))

            dapmin = float(input('Digite o DAP minimo da arvore: '))
            dapmax = float(input('Digite o DAP maximo da arvore: '))
            if dapmin > dapmax or dapmax == str or dapmin == str:
                print('======= VALORES DIGITADOS INCORRETAMENTE =======\n')
                dapmin = float(input('Digite o DAP minimo da arvore: '))
                dapmax = float(input('Digite o DAP maximo da arvore: '))
            
            
            print('--------------------------------------------------------------------------')

            hmin = float(input('Digite a altura minima da arvore: '))
            hmax = float(input('Digite a altura maxima da arvore: '))
            if hmin > hmax or hmax == str or hmin == str:
                print('======= VALORES DIGITADOS INCORRETAMENTE =======\n')
                dapmin = float(input('Digite o DAP minimo da arvore: '))
                dapmax = float(input('Digite o DAP maximo da arvore: '))
            

            print('--------------------------------------------------------------------------')

            quantidadeArvores += quantidadeArvores
            

            for AdicionandoTabela in range(arvoresParaFor, arvoresDoLaco - 1):
                h = random.randint(hmin, hmax)
                dap = random.randint(dapmin, dapmax)
                arvore += 1
                bdarvores_page.append([arvore, dap, h])
            tabela.save(filename= 'BDinfoArvores.xlsx')
            df = pd.DataFrame(pd.read_excel("BDinfoArvores.xlsx")) 
            df
            read_file = pd.read_excel ("BDinfoArvores.xlsx", sheet_name="bdArvores") 
            read_file.to_csv ("dados.csv", index = None, header=True) 
            
            df = pd.DataFrame(pd.read_csv("dados.csv")) 
            df

            opcao = str(input('Deseja continuar[S/N]: ')).upper()
            if opcao == 'N':
                tabela = pd.read_csv("dados.csv", sep =",")
                tabela

                tabela['C02Evitado'] = (0.013840*(tabela['dap']**2.437632))*(tabela['altura']*0.428609) #Biomassa presa nos fustes em t ha
                tabela['C02Evitado'] = tabela['C02Evitado']*0.5 #EC
                tabela['C02Evitado'] = tabela['C02Evitado']*3.67 #Conversao para Co2 em t ha

                print(f'CARBONO EVITADO: {tabela["C02Evitado"].sum()}\n')
                creditosDeCarbono = (tabela['C02Evitado'].sum()/1000).tolist()

                print(f'CREDITOS DE CARBONO: R${creditosDeCarbono*preco}')
                voltarMenu = int(input('''
                [1] VOLTAR PARA O MENU
                [2] CRIAR OUTRA TABELA
                
                Qual sua escolha: '''))
                if voltarMenu == 1:
                    break
                elif voltarMenu == 2:
                    print('Aguarde um instante, estamos reformulando....')
                    sleep(5)
    
    elif escolherTratamento == 0:
        print('Obrigado, volte sempre ;)')
        break

    else:
        print('--[ERRO] NUMERO DIGITADO E INVALIDO, TENTE NOVAMENTE--\n')
        
        