import pandas as pd
import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

def get_engine():
    # Lendo o .env
    load_dotenv()
    
    usuario = os.getenv("DB_USER")
    senha = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST")
    banco = os.getenv("DB_NAME")
    
    # Criando a string de conexão
    url_conexao = f"mysql+mysqlconnector://{usuario}:{senha}@{host}/{banco}"
    
    return create_engine(url_conexao)

def execute_query(sql):
    """
    Função utilitária que recebe uma string SQL, executa no banco
    e já retorna os dados prontos em um DataFrame do Pandas.
    """
    engine = get_engine()
    
    try:
        # O bloco 'with' garante que a conexão seja fechada automaticamente
        with engine.connect() as conn:
            # text(sql) é necessário no SQLAlchemy 2.0+ para segurança
            return pd.read_sql(text(sql), conn)
    except Exception as e:
        print(f"❌ Erro ao executar a consulta: {e}")
        return pd.DataFrame()