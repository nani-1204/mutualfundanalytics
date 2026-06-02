SELECT *
FROM fact_aum
ORDER BY aum_crore DESC
LIMIT 5;

SELECT
strftime('%Y-%m', date) AS month,
AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY month;

SELECT
state,
SUM(amount_inr) AS total_amount
FROM fact_transactions
GROUP BY state
ORDER BY total_amount DESC;

SELECT
scheme_name,
expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;

SELECT
category,
AVG(return_3yr_pct) AS avg_return
FROM fact_performance
GROUP BY category;

SELECT
scheme_name,
return_5yr_pct
FROM fact_performance
ORDER BY return_5yr_pct DESC
LIMIT 1;

SELECT
fund_house,
SUM(aum_crore) AS total_aum
FROM fact_aum
GROUP BY fund_house
ORDER BY total_aum DESC
LIMIT 1;

SELECT
risk_grade,
COUNT(*) AS total_funds
FROM fact_performance
GROUP BY risk_grade;

SELECT
city,
SUM(amount_inr) AS total_amount
FROM fact_transactions
GROUP BY city
ORDER BY total_amount DESC
LIMIT 10;

SELECT
amfi_code,
AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY amfi_code;
