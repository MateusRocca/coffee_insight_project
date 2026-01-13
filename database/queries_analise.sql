-- Consulta 1: Faturamento Total e Volume de Vendas
SELECT 
    COUNT(*) AS total_vendas, 
    SUM(money) AS faturamento_total 
FROM sales_coffee;

-- Consulta 2: Top 5 cafés mais vendidos
SELECT 
    coffee_name, 
    COUNT(*) AS quantidade 
FROM sales_coffee 
GROUP BY coffee_name 
ORDER BY quantidade DESC 
LIMIT 5;

-- Consulta 3: Horários de maior movimento (PICO)
SELECT 
    hour_of_day, 
    COUNT(*) AS total_pedidos 
FROM sales_coffee 
GROUP BY hour_of_day 
ORDER BY total_pedidos DESC;

-- Consulta 4: Preferência de Pagamento
SELECT 
    cash_type, 
    COUNT(*) AS total,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM sales_coffee), 2) AS percentual
FROM sales_coffee 
GROUP BY cash_type;

-- Consulta 5: Dia que mais vende
SELECT 
	weekday,
COUNT(*) AS dia_mais_vende
FROM sales_coffee
GROUP BY weekday;

-- Consulta 6: Gastos médios por períodos
SELECT 
    time_of_day,
    COUNT(*) AS total_pedidos,
    ROUND(AVG(money), 2) AS ticket_medio,
    ROUND(SUM(money), 2) AS faturamento_total
FROM sales_coffee
GROUP BY time_of_day
ORDER BY ticket_medio DESC;