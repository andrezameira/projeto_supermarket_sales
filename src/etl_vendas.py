import pandas as pd
from config import engine_supermarket
from datetime import time

def etl():

    # Pegando os dados diretamente da camada raw e salvando em um dataframe
    df_vendas = pd.read_sql(
        "select * from raw.raw_vendas",
        engine_supermarket
    )

    # Ajustando o nome das colunas:
    nomes_colunas = {
        "Invoice ID": "id_venda",
        "Branch": "filial",
        "City": "cidade",
        "Customer type": "tipo_cliente",
        "Gender": "genero",
        "Product line": "linha_produto",
        "Unit price": "preco_unitario",
        "Quantity": "quantidade",
        "Tax 5%": "imposto",
        "Sales": "valor_total",
        "Date": "data_venda",
        "Time": "hora_venda",
        "Payment": "forma_pagamento",  
        "cogs": "custo_mercadoria",
        "gross margin percentage": "margem_percentual",
        "gross income": "receita_bruta",
        "Rating": "avaliacao"
    }
    df_vendas = df_vendas.rename(columns=nomes_colunas)

    # Transformando a data de vendas em datetime e extraindo o ano
    df_vendas["data_venda"] = pd.to_datetime(
        df_vendas["data_venda"]
    )
    df_vendas["ano"] = df_vendas["data_venda"].dt.year


    # Criando uma função para tratar o am/pm manualmente
    def converter_para_time(texto):
        texto = texto.strip()
        periodo = texto[-2:].upper()
        hora_str = texto[:-2].strip()
        hora, minuto, segundo = map(int, hora_str.split(":"))

        if periodo == "PM" and hora != 12:
            hora += 12
        if periodo == "AM" and hora == 12:
            hora = 0

        return time(hora, minuto, segundo)

    df_vendas["hora_venda"] = pd.to_datetime(
        df_vendas["hora_venda"].astype(str).str.strip(),
        format="%I:%M:%S %p",
        errors="raise"
    ).dt.time

    # Normalização 
    colunas_texto = (
    df_vendas.select_dtypes(include=["object", "string"])
    .columns
    .drop("hora_venda")
    )
    
    for col in colunas_texto:
        df_vendas[col] = df_vendas[col].str.strip().str.lower()


    # Criando uma coluna com uma classificação da satisfação com base na nota de avaliacao
    df_vendas["classificacao"] = df_vendas["avaliacao"].apply(
        lambda avaliacao:
        "Satisfação Baixa" if avaliacao < 7
        else "Satisfação Média" if avaliacao < 9
        else "Satisfação Alta"
    )


    # Criando uma coluna de ticket médio por filial
    df_vendas["ticket_medio_filial"] = (
        df_vendas.groupby("filial")["valor_total"]
        .transform("mean")
        .round(2)
    )

    # Faz a gravação do dataframe já ajustado no schema processed
    df_vendas.to_sql(
        "vendas_tratadas",
        engine_supermarket,
        schema="processed",
        if_exists="replace",
        index=False
    )

    # Exportação dos dados para o formato CSV na camada processed
    df_vendas.to_csv(
        "data/processed/vendas_tratadas.csv",
        index=False,
        encoding="utf-8-sig"
    )
    
    print("Transformações realizadas e processed carregada")
