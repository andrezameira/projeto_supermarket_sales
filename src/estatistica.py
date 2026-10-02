import pandas as pd
from config import engine_supermarket
import matplotlib.pyplot as plt


def estatistica():

    # Leitura da tabela vendas_tratadas da camada processed  para dataframe
    df_vendas = pd.read_sql(
        "SELECT * FROM processed.vendas_tratadas",
        engine_supermarket
    )

    # 1. Filial com maior faturamento
    faturamento_filial = df_vendas.groupby("filial")["valor_total"].sum()
    filial_maior_faturamento = faturamento_filial.idxmax()

    print(faturamento_filial.sort_values(ascending=False))

    print("Filial com maior faturamento:", filial_maior_faturamento)

    faturamento_filial = df_vendas.groupby("filial")["valor_total"].sum().sort_values(ascending=False)
    plt.figure(figsize=(4, 3))
    plt.bar(faturamento_filial.index, faturamento_filial.values, color="steelblue")
    plt.title("Faturamento por Filial")
    plt.xlabel("Filial")
    plt.ylabel("Faturamento Total")
    plt.tight_layout()
    plt.savefig("resultado/graficos/filial_maior_faturamento.png", dpi=150, bbox_inches="tight")
    plt.close()

    # 2. Filial com maior quantidade de vendas
    qtd_vendas_filial = df_vendas.groupby("filial")["quantidade"].sum()
    filial_maior_qtd = qtd_vendas_filial.idxmax()

    print(qtd_vendas_filial.sort_values(ascending=False))

    print("\nFilial com maior quantidade de vendas:", filial_maior_qtd)

    qtd_vendas_filial = df_vendas.groupby("filial")["quantidade"].sum().sort_values(ascending=False)
    plt.figure(figsize=(4, 3))
    plt.bar(qtd_vendas_filial.index, qtd_vendas_filial.values, color="darkorange")
    plt.title("Quantidade de Vendas por Filial")
    plt.xlabel("Filial")
    plt.ylabel("Quantidade Vendida")
    plt.tight_layout()
    plt.savefig("resultado/graficos/filial_maior_qtd_venda.png", dpi=150, bbox_inches="tight")
    plt.close()


    # 3. Linha de produto com maior faturamento
    faturamento_linha = df_vendas.groupby("linha_produto")["valor_total"].sum()
    linha_maior_faturamento = faturamento_linha.idxmax()

    print(faturamento_linha.sort_values(ascending=False))

    print("\nLinha de produto com maior faturamento:", linha_maior_faturamento)

    faturamento_linha = df_vendas.groupby("linha_produto")["valor_total"].sum().sort_values(ascending=True)
    plt.figure(figsize=(6, 3))
    plt.barh(faturamento_linha.index, faturamento_linha.values, color="seagreen")
    plt.title("Faturamento por Linha de Produto")
    plt.xlabel("Faturamento Total")
    plt.ylabel("Linha de Produto")
    plt.tight_layout()
    plt.savefig("resultado/graficos/linha_produto_maior_faturamento.png", dpi=150, bbox_inches="tight")
    plt.close()


    # 4. Linha de produto com melhor avaliação média
    avaliacao_media_linha = df_vendas.groupby("linha_produto")["avaliacao"].mean()
    linha_melhor_avaliacao = avaliacao_media_linha.idxmax()

    print(avaliacao_media_linha.sort_values(ascending=False))

    print("\nLinha de produto com melhor avaliação média:", linha_melhor_avaliacao)

    avaliacao_media_linha = df_vendas.groupby("linha_produto")["avaliacao"].mean().sort_values()
    plt.figure(figsize=(6, 3))
    plt.barh(avaliacao_media_linha.index, avaliacao_media_linha.values, color="purple")
    plt.title("Avaliação Média por Linha de Produto")
    plt.xlabel("Avaliação Média")
    plt.ylabel("Linha de Produto")
    plt.tight_layout()
    plt.savefig("resultado/graficos/linha_produto_maior_avaliacao.png", dpi=150, bbox_inches="tight")
    plt.close()


    # 5. Forma de pagamento mais utilizada
    forma_pagamento_mais_usada = df_vendas["forma_pagamento"].value_counts().idxmax()

    print(df_vendas["forma_pagamento"].value_counts())

    print("\nForma de pagamento mais utilizada:", forma_pagamento_mais_usada)

    forma_pagamento = df_vendas["forma_pagamento"].value_counts()
    plt.figure(figsize=(3.5, 3.5))
    plt.pie(forma_pagamento.values, labels=forma_pagamento.index, autopct="%1.1f%%", startangle=90)
    plt.title("Formas de Pagamento Utilizadas")
    plt.tight_layout()
    plt.savefig("resultado/graficos/forma_pagamento_mais_usada.png", dpi=150, bbox_inches="tight")
    plt.close()

    # 6. Valor médio das vendas
    valor_medio_vendas = df_vendas["valor_total"].mean()

    print("\nValor médio das vendas:", valor_medio_vendas)

    plt.figure(figsize=(6, 3))
    plt.hist(df_vendas["valor_total"], bins=30, color="teal", edgecolor="black")
    plt.axvline(df_vendas["valor_total"].mean(), color="red", linestyle="--", label="Média")
    plt.title("Distribuição do Valor das Vendas")
    plt.xlabel("Valor da Venda")
    plt.ylabel("Frequência")
    plt.legend()
    plt.tight_layout()
    plt.savefig("resultado/graficos/valor_medio_vendas.png", dpi=150, bbox_inches="tight")
    plt.close()

    # 7. Maior venda registrada
    maior_venda = df_vendas["valor_total"].max()
    linha_maior_venda = df_vendas.loc[df_vendas["valor_total"].idxmax()]

    print(linha_maior_venda)

    print("\nMaior venda registrada:", maior_venda)

    top10_vendas = df_vendas.sort_values("valor_total", ascending=False).head(10)
    plt.figure(figsize=(6, 3))
    plt.bar(top10_vendas["id_venda"].astype(str), top10_vendas["valor_total"], color="firebrick")
    plt.title("Top 10 Maiores Vendas")
    plt.xlabel("ID da Venda")
    plt.ylabel("Valor da Venda")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig("resultado/graficos/maior_venda.png", dpi=150, bbox_inches="tight")
    plt.close()

    # 8. Dia da semana com maior quantidade de vendas
    dias = {
            "Monday": "Segunda-feira",
            "Tuesday": "Terça-feira",
            "Wednesday": "Quarta-feira",
            "Thursday": "Quinta-feira",
            "Friday": "Sexta-feira",
            "Saturday": "Sábado",
            "Sunday": "Domingo"
        }

    df_vendas["dia_semana"] = df_vendas["data_venda"].dt.day_name().map(dias)

    vendas_dia_semana = df_vendas.groupby("dia_semana")["quantidade"].sum()
    dia_maior_vendas = vendas_dia_semana.idxmax()

    print(vendas_dia_semana.sort_values(ascending=False))

    print("\nDia da semana com maior quantidade de vendas:", dia_maior_vendas)

    ordem_dias = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]
    vendas_dia_semana = df_vendas.groupby("dia_semana")["quantidade"].sum().reindex(ordem_dias)
    plt.figure(figsize=(6, 3))
    plt.bar(vendas_dia_semana.index, vendas_dia_semana.values, color="navy")
    plt.title("Quantidade de Vendas por Dia da Semana")
    plt.xlabel("Dia da Semana")
    plt.ylabel("Quantidade Vendida")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("resultado/graficos/dia_semana_maior_venda.png", dpi=150, bbox_inches="tight")
    plt.close()


    # Estatísticas das colunas numéricas
    colunas_numericas = [
        "preco_unitario", "quantidade", "imposto", "valor_total",
        "custo_mercadoria", "margem_percentual", "receita_bruta",
        "avaliacao", "ticket_medio_filial"
    ]

    estatisticas_numericas = df_vendas[colunas_numericas].describe().T
    estatisticas_numericas["mediana"] = df_vendas[colunas_numericas].median()
    estatisticas_numericas["variancia"] = df_vendas[colunas_numericas].var()
    estatisticas_numericas = estatisticas_numericas.reset_index().rename(columns={"index": "coluna"})
    estatisticas_numericas["tipo"] = "numerica"

    # Frequências das colunas categóricas
    colunas_categoricas = [
        "filial", "cidade", "tipo_cliente", "genero",
        "linha_produto", "forma_pagamento", "classificacao"
    ]

    frequencias = []
    for col in colunas_categoricas:
        freq = df_vendas[col].value_counts().reset_index()
        freq.columns = ["categoria", "quantidade"]
        freq["coluna"] = col
        frequencias.append(freq)

    df_frequencias = pd.concat(frequencias, ignore_index=True)
    df_frequencias["tipo"] = "categorica"

    # Junta tudo e salva o CSV
    metricas_final = pd.concat([estatisticas_numericas, df_frequencias], ignore_index=True)
    metricas_final = metricas_final.round(2)

    metricas_final.to_csv("resultado/estatistica/metricas.csv", index=False, encoding="utf-8-sig")
    
    print("Estatísitca concluída")

