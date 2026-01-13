☕ Coffee Insight Project
Este projeto consiste em um ecossistema completo de Engenharia e Análise de Dados focado no monitoramento de vendas de uma cafeteria. 
A solução abrange desde a ingestão de dados reais até a disponibilização de insights estratégicos via terminal (CLI) e Power BI.

📁 Fonte de Dados (Kaggle)
Os dados brutos foram extraídos do dataset Coffee Sales - Coffee Shop Analysis disponível no Kaggle.
O conjunto de dados contém registros transacionais detalhados de uma cafeteria real.
Foi realizado um processo de Data Cleaning e normalização utilizando Python e Pandas para garantir a integridade dos dados antes da carga no banco MySQL.

🏗️ Arquitetura e Tecnologias
O projeto foi desenvolvido sob os princípios de Orientação a Objetos (OOP), garantindo um código modular, 
escalável e de fácil manutenção para futuras expansões.
Python 3.10+: Linguagem base para automação e análise.
MySQL: Banco de dados relacional para armazenamento e modelagem.
SQLAlchemy: ORM utilizado para gestão eficiente de conexões.
WSL 2 (Ubuntu): Ambiente de desenvolvimento Linux.
Power BI: Visualização de dados e dashboards gerenciais.

Organização do Projeto
database/analyzer.py: Contém a classe CoffeeAnalyzer, que centraliza a lógica de negócio e conexão.
database/utils.py: Funções utilitárias para formatação de moeda (BRL) e tratamento de DataFrames.
scripts/dashboard_cli.py: Interface de linha de comando interativa para o usuário final.
sql/: Repositório de queries originais para documentação e portfólio.

📊 Business Insights
O dashboard CLI fornece respostas em tempo real para indicadores chave (KPIs):
Sales Metrics: Faturamento total e volume de vendas formatados em Reais.
Top Products: Ranking dos 5 cafés mais vendidos.
Peak Hours: Identificação dos horários de maior fluxo para gestão de staff.
Payment Distribution: Análise de métodos de pagamento (Dinheiro vs. Cartão).
Average Order Value (AOV): Gasto médio e performance financeira por período do dia.

🛠️ Como Executar
Clonar o repositório:
Bash
git clone https://github.com/seu-usuario/coffee_insight_project.git
cd coffee_insight_project
Configurar o ambiente virtual e dependências:
Bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
Configurar Variáveis de Ambiente: Crie um arquivo .env na raiz do projeto (não o envie para o GitHub) com suas credenciais:
Snippet de código
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
DB_HOST=localhost
DB_NAME=coffee_db
Iniciar o Dashboard:
Bash
python3 scripts/dashboard_cli.py

🛡️ Licença
Este projeto foi desenvolvido como parte de um portfólio técnico em Engenharia de Dados. Sinta-se à vontade para utilizá-lo como referência.
