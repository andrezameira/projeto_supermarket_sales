# Arquivo que vai iniciar o setup (vai ler as credenciais para iniciar a conexão)

import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

engine_supermarket = create_engine(
    f"postgresql+psycopg2://"
    f"{os.getenv('SUPERMARKET_USUARIO')}:{os.getenv('SUPERMARKET_SENHA')}"
    f"@{os.getenv('SUPERMARKET_HOST')}:{os.getenv('SUPERMARKET_PORTA')}"
    f"/{os.getenv('SUPERMARKET_BANCO')}"
)


