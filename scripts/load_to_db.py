import pandas as pd
import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

# 1. Carregar as variáveis do arquivo .env
load_dotenv()

# 2. Pegando credênciais do .env
USUARIO = os.getenv("DB_USER")
SENHA = os.getenv("DB_PASSWORD")
HOST = os.getenv("DB_HOST")
BANCO = os.getenv("DB_NAME")

# 3. Criando a conexão com o MySQL
engine = create_engine(f"mysql+mysqlconnector://{USUARIO}:{SENHA}@{HOST}/{BANCO}")

# 4. Caminho do arquivo tratado
caminho_csv = "data/processed/coffee_sales_clean.csv"

try:
    # carregando csv para df temporário
    df = pd.read_csv(caminho_csv)

    #enviando para tabela mysql
    print(f"Enviando {len(df)} linhas para o banco de dados...")
    df.to_sql('sales_coffee', con=engine, if_exists='append', index=False)
    
    print("✅ Carga finalizada com sucesso!")

except Exception as e:
    print(f"❌ Erro durante a carga: {e}")