**Projeto: Empreendedor de Créditos de Carbono**

Este programa Python oferece funcionalidades relacionadas ao empreendimento em créditos de carbono, incluindo cálculos de ganhos em créditos de carbono ao plantar árvores, medição de absorção de CO2 pelas árvores plantadas e exibição de dados em tabelas Excel. Ele inclui opções para:

1. **Quanto Ganhar em Créditos de Carbono ao Plantar Árvores:**
   - O usuário pode escolher uma espécie de árvore (Jatoba-da-Mata, Guapuruvu ou Pau-jacaré).
   - O usuário insere a área disponível para plantação em metros quadrados.
   - O programa calcula o número de árvores que podem ser plantadas, os gastos associados, o tempo de absorção de CO2, a absorção total de CO2 e os créditos de carbono gerados. 
   - Os resultados são formatados em uma tabela e podem ser exportados para um arquivo Excel.

2. **Medição de Carbono nas Árvores Plantadas:**
   - O usuário insere o número de árvores de uma espécie específica que deseja medir.
   - Para cada árvore, o usuário insere o diâmetro à altura do peito (DAP) mínimo e máximo e a altura mínima e máxima.
   - Os dados de DAP e altura são gerados aleatoriamente dentro dos intervalos fornecidos.
   - O programa calcula o carbono evitado em toneladas por hectare (T/ha) e os créditos de carbono correspondentes.
  
3. **Exibição de Dados das Tabelas:**
   - O usuário pode visualizar dados das tabelas existentes que contêm informações sobre árvores plantadas, DAP, altura, carbono evitado e créditos de carbono gerados.

4. **Sair do Programa:**
   - Encerra o programa.

## Dependências e Instalação

Antes de executar o programa, você deve instalar as seguintes bibliotecas Python usando o `pip`:

1. **Bibliotecas Padrão:**

    - `random`: Biblioteca padrão do Python para geração de números aleatórios.
    - `time`: Biblioteca padrão do Python para manipulação de tempo.
    - `os`: Biblioteca padrão do Python para interação com o sistema operacional/terminal.
    - `glob`: Biblioteca padrão do Python para encontrar todos os caminhos que correspondem a um padrão de acordo com as regras usadas no shell Unix.

2. **Bibliotecas Externas:**

   - `pandas - (1.5.0)`: Biblioteca para manipulação e análise de dados. Para instalar, execute o seguinte comando:

     ```sh
     pip install pandas==1.5.0
     ```

   - `openpyxl (3.0.10)`: Biblioteca para ler e escrever arquivos Excel (.xlsx). Para instalar, execute o seguinte comando:

     ```sh
     pip install openpyxl==3.0.10
     ```

   - `requests (2.28.1)`: Biblioteca para fazer solicitações HTTP. Para instalar, execute o seguinte comando:

     ```sh
     pip install requests==2.28.1
     ```

Certifique-se de instalar essas bibliotecas externas antes de executar o programa para evitar quaisquer erros de importação.

## Arquivo `funcoes.py`

O programa também depende de um arquivo chamado `funcoes.py`, que deve estar no mesmo diretório. Este arquivo contém duas funções, `tabela_criacao` e `tabela_leitura`, que são usadas para criar e ler tabelas Excel, respectivamente. Certifique-se de que o arquivo `funcoes.py` esteja presente e as funções estejam corretamente definidas.

## Instruções de Uso

1. Execute o programa Python após instalar as bibliotecas externas e garantir que o arquivo `funcoes.py` esteja no mesmo diretório.

2. O programa exibirá um menu com várias opções relacionadas a créditos de carbono. Escolha a opção desejada digitando o número correspondente e pressionando Enter.

3. Siga as instruções fornecidas pelo programa para inserir dados ou visualizar informações conforme a opção selecionada.

## Observações

- Certifique-se de inserir valores válidos quando solicitado pelo programa para evitar erros.
- Os dados das tabelas são armazenados em arquivos Excel no diretório `./Tabelas`. Certifique-se de que esse diretório exista no mesmo local onde você está executando o programa.

Aproveite o uso do programa e contribua para a causa dos créditos de carbono!


**Instruções de Uso:**
1. Execute o programa e escolha uma das opções do menu.
2. Siga as instruções para inserir dados ou visualizar informações conforme a opção selecionada.

**Observações:**
- O programa assume que o usuário fornece valores válidos para os dados inseridos.
- Os dados das tabelas são armazenados em arquivos Excel no diretório `./Tabelas`.
- Lembre-se de que o programa estiver dando erro, talvez você não tenha iniciado o ambiente virtual, apenas substitua este comando com o caminho da sua maquian
    ```sh
    /caminho/para/sua/venv/Scripts/activate
    ```
