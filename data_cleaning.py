import pandas as pd

nav = pd.read_csv("data/raw/02_nav_history.csv")

print("Original Shape:", nav.shape)

# Convert date
nav["date"] = pd.to_datetime(nav["date"])

# Sort
nav = nav.sort_values(
    ["amfi_code", "date"]
)

# Remove duplicates
nav = nav.drop_duplicates()

# Keep valid NAV
nav = nav[nav["nav"] > 0]

print("Clean Shape:", nav.shape)

nav.to_csv(
    "data/processed/nav_history_clean.csv",
    index=False
)
print("\nDuplicate Rows:")
print(nav.duplicated().sum())

print("\nInvalid NAV Values:")
print((nav["nav"] <= 0).sum())

print("\nMissing NAV Values:")
print(nav["nav"].isnull().sum())
nav["nav"] = nav.groupby(
    "amfi_code"
)["nav"].ffill()

txn = pd.read_csv(
    "data/raw/08_investor_transactions.csv"
)

txn["transaction_date"] = pd.to_datetime(
    txn["transaction_date"]
)

txn["transaction_type"] = (
    txn["transaction_type"]
    .str.strip()
    .str.title()
)
txn = txn[
    txn["amount_inr"] > 0
]
print(
    txn["kyc_status"].unique()
)
txn.to_csv(
 "data/processed/investor_transactions_clean.csv",
 index=False
)

perf = pd.read_csv(
    "data/raw/07_scheme_performance.csv"
)
return_cols = [
 "return_1yr_pct",
 "return_3yr_pct",
 "return_5yr_pct"
]

for col in return_cols:
    perf[col] = pd.to_numeric(
        perf[col],
        errors="coerce"
    )
    anomaly = perf[
    (perf["expense_ratio_pct"] < 0.1)
    |
    (perf["expense_ratio_pct"] > 2.5)
]

print(anomaly)
perf.to_csv(
 "data/processed/scheme_performance_clean.csv",
 index=False
)