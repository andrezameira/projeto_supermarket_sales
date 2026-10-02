# Importar os módulos
from setup import configurar_banco
from leitura_dados import extrair_csv
from etl_vendas import etl
from estatistica import estatistica

# Função de execução
def main():
    configurar_banco()

    #extrair dados
    extrair_csv()

    #transformações
    etl()

    #análises
    estatistica()
    
    print("Pipeline ETL concluído")

if __name__ == "__main__":
    main()