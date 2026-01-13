CREATE OR REPLACE VIEW vw_coffee_performance AS
SELECT 
    date,
    coffee_name,
    cash_type,
    time_of_day,
    weekday,
    COUNT(*) AS total_vendas,
    SUM(money) AS faturamento_total,
    ROUND(AVG(money), 2) AS ticket_medio
FROM sales_coffee
GROUP BY date, coffee_name, cash_type, time_of_day, weekday;