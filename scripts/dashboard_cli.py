import sys
import os

# Ajuste para que o Python encontre a pasta 'database' no seu ambiente WSL
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scripts.analyses import CoffeeAnalyzer
from database.utils import format_currency_columns

def clear_screen():
    """Limpa o terminal de acordo com o Sistema Operacional"""
    os.system('clear' if os.name == 'posix' else 'cls')

def show_menu():
    # Instanciamos a classe uma única vez. 
    # Isso abre a conexão com o banco no início do programa.
    analyzer = CoffeeAnalyzer()
    
    while True:
        print("\n" + "="*50)
        print("☕ COFFEE SALES - TERMINAL DASHBOARD (O.O. Version)")
        print("="*50)
        print("1. Faturamento Total e Volume de Vendas")
        print("2. Top 5 Cafés")
        print("3. Horário mais movimentado")
        print("4. Preferência de pagamento")
        print("5. Dias de maiores vendas")
        print("6. Gastos médios por período")
        print("0. Sair")
        print("="*50)

        choice = input("Selecione a opção desejada: ")
        clear_screen()

        if choice == "1":
            print("\n📈 FATURAMENTO TOTAL E VOLUME DE VENDAS")
            df = analyzer.get_sales_metrics()
            # Aplicando sua função de formatação para Reais
            df = format_currency_columns(df, ['total_revenue'])
            print(df.to_string(index=False))

        elif choice == "2":
            print("\n🏆 TOP 5 CAFÉS")
            df = analyzer.get_top_products()
            print(df.to_string(index=False))

        elif choice == "3":
            print("\n⏰ HORÁRIOS DE MAIOR MOVIMENTO")
            df = analyzer.get_peak_hours()
            print(df.to_string(index=False))

        elif choice == "4":
            print("\n💳 PREFERÊNCIA DE PAGAMENTO")
            df = analyzer.get_payment_distribution()
            print(df.to_string(index=False))

        elif choice == "5":
            print("\n📅 DIA QUE MAIS VENDE")
            df = analyzer.get_best_selling_day()
            print(df.to_string(index=False))

        elif choice == "6":
            print("\n🕒 GASTOS MÉDIOS POR PERÍODOS")
            df = analyzer.get_period_performance()
            # Formatando as duas colunas financeiras com os novos nomes em inglês
            df = format_currency_columns(df, ['avg_order_value', 'total_revenue'])
            print(df.to_string(index=False))

        elif choice == "0":
            print("Encerrando o sistema Coffee Insights... Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.")

        input("\nAperte ENTER para voltar ao menu...")
        clear_screen()

if __name__ == "__main__":
    show_menu()