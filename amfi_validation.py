import pandas as pd

master = pd.read_csv("data/raw/01_fund_master.csv")
nav = pd.read_csv("data/raw/02_nav_history.csv")

missing_codes = set(master["amfi_code"]) - set(nav["amfi_code"])

print("Missing AMFI Codes:")
print(missing_codes)

print("\nCount:")
print(len(missing_codes))