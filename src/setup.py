from sqlalchemy import text
from config import engine_supermarket

# Para executar o arquivo
def configurar_banco():
    print("Configurando o banco supermarket")

    with engine_supermarket.begin() as conn:
        conn.execute(text("create schema if not exists raw"))
        conn.execute(text("create schema if not exists processed"))
    print("Schemas Raw e Processed criados")