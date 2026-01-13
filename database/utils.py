import pandas as pd

def format_currency_columns(df, columns):
    """
    Recebe um DataFrame e uma LISTA de colunas para formatar em R$.
    """
    df_formatted = df.copy()
    
    for col in columns:
        if col in df_formatted.columns:
            # Aplica a formatação apenas se a coluna existir
            df_formatted[col] = df_formatted[col].apply(
                lambda x: f"R$ {x:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
                if pd.notnull(x) else "R$ 0,00"
            )
            
    return df_formatted