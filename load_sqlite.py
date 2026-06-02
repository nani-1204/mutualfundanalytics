import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "sqlite:///bluestock_mf.db"
)

fund = pd.read_csv(
    "data/raw/01_fund_master.csv"
)

fund.to_sql(
    "dim_fund",
    engine,
    if_exists="replace",
    index=False
)

print("Fund Master Loaded")

nav = pd.read_csv(
    "data/processed/nav_history_clean.csv"
)

nav.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

print("NAV Loaded")

txn = pd.read_csv(
    "data/processed/investor_transactions_clean.csv"
)

txn.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

print("Transactions Loaded")

perf = pd.read_csv(
    "data/processed/scheme_performance_clean.csv"
)

perf.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

print("Performance Loaded")

aum = pd.read_csv(
    "data/raw/03_aum_by_fund_house.csv"
)

aum.to_sql(
    "fact_aum",
    engine,
    if_exists="replace",
    index=False
)

print("AUM Loaded Successfully")