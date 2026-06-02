import sqlite3
import pandas as pd

conn = sqlite3.connect("bluestock_mf.db")

# Query 1
print("\n===== QUERY 1: Total Funds =====")
query1 = """
SELECT COUNT(*) AS total_funds
FROM dim_fund;
"""
print(pd.read_sql_query(query1, conn))

# Query 2
print("\n===== QUERY 2: Top 5 Fund Houses by AUM =====")
query2 = """
SELECT
fund_house,
SUM(aum_crore) AS total_aum
FROM fact_aum
GROUP BY fund_house
ORDER BY total_aum DESC
LIMIT 5;
"""
print(pd.read_sql_query(query2, conn))

# Query 3
print("\n===== QUERY 3: Average NAV Per Month =====")
query3 = """
SELECT
strftime('%Y-%m', date) AS month,
AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY month
ORDER BY month;
"""
print(pd.read_sql_query(query3, conn))

# Query 4
print("\n===== QUERY 4: Transactions By Fund =====")
query4 = """
SELECT
amfi_code,
COUNT(*) AS transaction_count
FROM fact_transactions
GROUP BY amfi_code
ORDER BY transaction_count DESC;
"""
print(pd.read_sql_query(query4, conn))

# Query 5
print("\n===== QUERY 5: Average Transaction Amount =====")
query5 = """
SELECT
AVG(amount_inr) AS avg_transaction_amount
FROM fact_transactions;
"""
print(pd.read_sql_query(query5, conn))

# Query 6
print("\n===== QUERY 6: Funds With Expense Ratio < 1% =====")
query6 = """
SELECT
scheme_name,
expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;
"""
print(pd.read_sql_query(query6, conn))

# Query 7
print("\n===== QUERY 7: Top Performing Fund (5-Year Return) =====")
query7 = """
SELECT
scheme_name,
return_5yr_pct
FROM fact_performance
ORDER BY return_5yr_pct DESC
LIMIT 1;
"""
print(pd.read_sql_query(query7, conn))

# Query 8
print("\n===== QUERY 8: Risk Category Distribution =====")
query8 = """
SELECT
risk_grade,
COUNT(*) AS fund_count
FROM fact_performance
GROUP BY risk_grade;
"""
print(pd.read_sql_query(query8, conn))

# Query 9
print("\n===== QUERY 9: Average Returns Across Funds =====")
query9 = """
SELECT
AVG(return_1yr_pct) AS avg_1yr_return,
AVG(return_3yr_pct) AS avg_3yr_return,
AVG(return_5yr_pct) AS avg_5yr_return
FROM fact_performance;
"""
print(pd.read_sql_query(query9, conn))

# Query 10
print("\n===== QUERY 10: Average NAV By Fund =====")
query10 = """
SELECT
amfi_code,
AVG(nav) AS average_nav
FROM fact_nav
GROUP BY amfi_code
ORDER BY average_nav DESC;
"""
print(pd.read_sql_query(query10, conn))

conn.close()