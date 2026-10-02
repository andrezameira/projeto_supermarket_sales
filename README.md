# Análise de Vendas de Supermercado

Projeto de análise de dados de vendas de uma rede de supermercados, desenvolvido com **PostgreSQL, SQL, Python e Pandas**. O fluxo parte dos dados originais, armazena-os em uma camada bruta (*Raw*), realiza a limpeza e transformação dos registros e gera métricas e visualizações para responder a perguntas de negócio.

## Objetivo

Organizar e analisar os registros de vendas para compreender o desempenho das filiais, das linhas de produto e das formas de pagamento, além de identificar padrões de venda e avaliar a satisfação dos clientes.

## Fonte dos dados

O projeto utiliza o dataset público **Supermarket Sales**, disponibilizado no Kaggle:

[Supermarket Sales — Kaggle](https://www.kaggle.com/datasets/faresashraf1001/supermarket-sales)

O arquivo de origem é um CSV delimitado por vírgulas. Ele contém informações sobre filial, cidade, produto, preço, quantidade, data e horário da venda, forma de pagamento, valor total e avaliação do cliente, entre outros campos.

## Tecnologias utilizadas

- **PostgreSQL** — armazenamento dos dados e execução de consultas SQL.
- **SQL** — criação do banco e das tabelas, consultas e exportações.
- **Python** — execução das etapas de leitura, transformação e análise.
- **Pandas** — inspeção, limpeza, tipagem e transformação dos dados.
- **matplotlib** — criação dos gráficos, se aplicável.
- **Git e GitHub** — controle de versão e disponibilização do projeto.

## Organização do repositório

```text
.
├── sql/
│   ├── 01_criar_banco.sql
│   ├── 02_criar_tabelas.sql
│   └── 03_consultas.sql
├── src/
│   ├── 01_leitura_dados.py
│   ├── 02_etl_vendas.py
│   └── 03_estatistica.py
├── data/
│   ├── raw/
│   │   └── [arquivo CSV original, se incluído]
│   └── processed/
│       └── vendas_tratadas.csv
├── resultados/
│   ├── [arquivos de resultados]
│   └── [gráficos]
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Arquitetura do projeto

O fluxo segue uma organização inspirada na **Arquitetura Medallion**, com as seguintes etapas:

1. **Raw (bruta):** cópia dos dados originais carregada no PostgreSQL sem alterações intencionais no conteúdo.
2. **Processed:** dados limpos e tipados com Python e Pandas, com verificações de integridade e criação de colunas derivadas.
3. **Resultados:** métricas, respostas às perguntas de negócio e visualizações salvas na pasta `resultados/`.

## Etapas do pipeline

### 1. Criação do banco e das tabelas

Os scripts da pasta `sql/` preparam o banco PostgreSQL e as tabelas necessárias:

- `sql/01_criar_banco.sql` — criação do banco de dados.
- `sql/02_criar_tabelas.sql` — criação das tabelas das camadas Raw e Processed, com chaves e restrições.
- `sql/03_consultas.sql` — consultas para explorar e agregar os dados e, quando aplicável, exportá-los para CSV.

Execute os scripts na ordem indicada, utilizando uma ferramenta compatível com PostgreSQL, como `psql` ou um cliente gráfico.

### 2. Extração e carga dos dados brutos

Coloque o CSV original em `data/raw/` com o nome esperado pelo projeto: **`supermarket_sales`**.

Os dados são carregados para a tabela **`raw_vendas`** por meio do script `src/01_leitura_dados.py. A camada Raw preserva os valores de origem para possibilitar rastreabilidade e comparação com os dados tratados.

### 3. Leitura, Limpeza e transformação

O script `src/02_etl_vendas.py` prepara os dados para análise. Conforme implementado, essa etapa pode incluir:

- padronização dos nomes das colunas;
- conversão de datas, horários e valores numéricos;
- verificação e tratamento de valores ausentes;
- identificação ou remoção de registros duplicados;
- validação da integridade dos dados;
- criação de colunas derivadas;
- exportação do resultado para `data/processed/vendas_tratadas.csv`.

### 4. Análise e geração de resultados

O script `src/03_estatistica.py` calcula estatísticas descritivas, responde às perguntas de negócio e gera gráficos. Os arquivos produzidos ficam em `resultados/`.

## Perguntas de negócio

A análise foi planejada para responder às seguintes perguntas:

1. Qual filial apresentou o maior faturamento?
2. Qual filial realizou a maior quantidade de vendas?
3. Qual linha de produto apresentou o maior faturamento?
4. Qual linha de produto recebeu a melhor avaliação média?
5. Qual foi a forma de pagamento mais utilizada?
6. Qual foi o valor médio das vendas?
7. Qual foi a maior venda registrada?
8. Em qual dia da semana ocorreu a maior quantidade de vendas?

## Dicionário de dados — camada tratada

| Coluna | Tipo esperado | Descrição / validação |
|---|---|---|
| `id_venda` | `VARCHAR(50)` | Identificador único; chave primária e obrigatório |
| `Filial` | `VARCHAR(10)` | Identificação da filial; obrigatório |
| `Cidade` | `VARCHAR(100)` | Cidade da filial; obrigatório |
| `tipo_cliente` | `VARCHAR(50)` | Tipo de cliente |
| `Gênero` | `VARCHAR(20)` | Gênero informado no registro |
| `linha_produto` | `VARCHAR(150)` | Categoria ou linha do produto; obrigatório |
| `preco_unitario` | `NUMERIC(10,2)` | Preço unitário; maior ou igual a zero |
| `Quantidade` | `INTEGER` | Quantidade de itens; maior que zero |
| `Imposto` | `NUMERIC(10,2)` | Valor do imposto; maior ou igual a zero |
| `valor_total` | `NUMERIC(12,2)` | Valor total da venda; calculado ou conferido |
| `data_venda` | `DATE` | Data convertida do arquivo de origem |
| `hora_venda` | `TIME` | Horário convertido do arquivo de origem |
| `forma_pagamento` | `VARCHAR(50)` | Forma de pagamento; obrigatório |
| `custo_mercadoria` | `NUMERIC(12,2)` | Custo da mercadoria; maior ou igual a zero |
| `margem_percentual` | `NUMERIC(10,2)` | Margem percentual |
| `receita_bruta` | `NUMERIC(12,2)` | Receita bruta; maior ou igual a zero |
| `Avaliação` | `NUMERIC(4,2)` | Avaliação do cliente, validada entre 0 e 10 |

## Requisitos

- PostgreSQL 
- Python 
- Git
- Acesso ao arquivo CSV do dataset

As bibliotecas Python utilizadas estão listadas em `requirements.txt`.

## Configuração e execução

### Pré-requisitos

- Python 3.13 (ou compatível)
- PostgreSQL instalado e em execução
- Arquivo `supermarket_sales.csv` salvo em `data/raw/`

### 1. Obter o projeto

git clone https://github.com/andrezameira/projeto_supermarket_sales.git
cd projeto_supermarket_sales

### 2. Configurar o ambiente Python

python -m venv .venv

Ative o ambiente virtual:

# Windows (PowerShell)
.venv\Scripts\Activate.ps1

# Linux ou macOS
source .venv/bin/activate

Instale as dependências:
pip install -r requirements.txt

### 3. Criar o banco de dados

No PostgreSQL (psql ou DBeaver), crie apenas o banco:
CREATE DATABASE supermarket;

Os schemas `raw` e `processed` e as tabelas são criados automaticamente pelo pipeline.

### 4. Configurar as credenciais

Crie um arquivo `.env` na raiz do projeto, a partir do modelo `.env.example`:
SUPERMARKET_USUARIO=seu_usuario
SUPERMARKET_SENHA=sua_senha
SUPERMARKET_HOST=localhost
SUPERMARKET_PORTA=5432
SUPERMARKET_BANCO=supermarket

O arquivo `.env` não deve ser versionado.

### 5. Executar o pipeline

A partir da raiz do projeto:
python src/run_etl.py

O pipeline executa, em ordem:

1. Criação dos schemas `raw` e `processed`
2. Carga do CSV na tabela `raw.raw_vendas`
3. Tratamento dos dados e gravação em `processed.vendas_tratadas`
4. Geração das análises estatísticas e dos gráficos

### Saídas geradas

- `data/processed/vendas_tratadas.csv`
- `resultado/graficos/` (gráficos em PNG)
- `resultado/estatistica/metricas.csv`

### Principais resultados da análise

| Pergunta | Resultado |
|---|---|
| Filial com maior faturamento | **giza** |
| Filial com maior quantidade de vendas | **alex** |
| Linha de produto com maior faturamento | **food and beverages   56144.8440** |
| Linha de produto com melhor avaliação média | **food and beverages   7.113218** |
| Forma de pagamento mais utilizada | **ewallet  345** |
| Valor médio das vendas | **322.966749** |
| Maior venda registrada | **id_venda  860-79-0874** |
| Dia da semana com mais vendas | **Sábado** |

## Autoria

**Andreza Cristina Meira**  
Projeto desenvolvido para **o curso de Análise de Dados com Python**.
