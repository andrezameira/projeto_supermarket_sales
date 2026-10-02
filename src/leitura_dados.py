
import pandas as pd
from datetime import time
from config import engine_supermarket

def extrair_csv():
    df_sales = pd.read_csv(
    "data/raw/supermarket_sales.csv", 
    sep=",", 
    encoding="utf-8-sig"
    )
    
    df_sales.to_sql(
        "raw_vendas",
        engine_supermarket,
        schema="raw",
        if_exists="replace",
        index=False
    )
    print("Extração do csv concluída")
    print("Dados gravados no schema raw")