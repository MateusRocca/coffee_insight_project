import os
import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

class CoffeeAnalyzer:
    """
    Classe responsável por gerenciar a conexão com o banco de dados 
    e realizar análises de negócio sobre as vendas de café.
    """

    def __init__(self):
        """Inicializa as configurações e cria a conexão com o banco."""
        load_dotenv()
        self.engine = self._create_engine()

    def _create_engine(self):
        """Método interno para configurar a engine do SQLAlchemy."""
        user = os.getenv("DB_USER")
        password = os.getenv("DB_PASSWORD")
        host = os.getenv("DB_HOST")
        database = os.getenv("DB_NAME")
        
        url = f"mysql+mysqlconnector://{user}:{password}@{host}/{database}"
        return create_engine(url)

    def _execute_query(self, query):
        """
        Método centralizado para executar SQL. 
        Garante que a conexão seja fechada e erros sejam tratados.
        """
        try:
            with self.engine.connect() as conn:
                return pd.read_sql(text(query), conn)
        except Exception as e:
            print(f"❌ Erro na base de dados: {e}")
            return pd.DataFrame()

    # --- MÉTODOS DE ANÁLISE DE NEGÓCIO ---

    def get_sales_metrics(self):
        """Consulta 1: Faturamento Total e Volume de Vendas."""
        query = """
        SELECT 
            COUNT(*) AS total_sales, 
            SUM(money) AS total_revenue 
        FROM sales_coffee;
        """
        return self._execute_query(query)

    def get_top_products(self):
        """Consulta 2: Top 5 cafés mais vendidos."""
        query = """
        SELECT 
            coffee_name, 
            COUNT(*) AS quantity 
        FROM sales_coffee 
        GROUP BY coffee_name 
        ORDER BY quantity DESC 
        LIMIT 5;
        """
        return self._execute_query(query)

    def get_peak_hours(self):
        """Consulta 3: Horários de maior movimento (PICO)."""
        query = """
        SELECT 
            hour_of_day, 
            COUNT(*) AS total_orders 
        FROM sales_coffee 
        GROUP BY hour_of_day 
        ORDER BY total_orders DESC;
        """
        return self._execute_query(query)

    def get_payment_distribution(self):
        """Consulta 4: Preferência de Pagamento."""
        query = """
        SELECT 
            cash_type, 
            COUNT(*) AS total,
            ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM sales_coffee), 2) AS percentage
        FROM sales_coffee 
        GROUP BY cash_type;
        """
        return self._execute_query(query)

    def get_best_selling_day(self):
        """Consulta 5: Dias que mais vendem."""
        query = """
        SELECT 
            weekday,
            COUNT(*) AS sales_count
        FROM sales_coffee
        GROUP BY weekday
        ORDER BY sales_count DESC;
        """
        return self._execute_query(query)

    def get_period_performance(self):
        """Consulta 6: Gastos médios por períodos."""
        query = """
        SELECT 
            time_of_day,
            COUNT(*) AS total_orders,
            ROUND(AVG(money), 2) AS avg_order_value,
            ROUND(SUM(money), 2) AS total_revenue
        FROM sales_coffee
        GROUP BY time_of_day
        ORDER BY avg_order_value DESC;
        """
        return self._execute_query(query)