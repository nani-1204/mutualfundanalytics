# Data Dictionary

## 01_fund_master.csv

| Column        | Data Type | Description                  |
| ------------- | --------- | ---------------------------- |
| amfi_code     | Integer   | Unique AMFI mutual fund code |
| fund_house    | Text      | Mutual fund company          |
| scheme_name   | Text      | Fund scheme name             |
| category      | Text      | Equity or Debt               |
| sub_category  | Text      | Large Cap, Small Cap, etc.   |
| risk_category | Text      | Risk level of fund           |

Source: Bluestock Dataset

---

## 02_nav_history.csv

| Column    | Data Type | Description     |
| --------- | --------- | --------------- |
| amfi_code | Integer   | Fund identifier |
| date      | Date      | NAV date        |
| nav       | Float     | Net Asset Value |

Source: Bluestock Dataset

---

## 08_investor_transactions.csv

| Column           | Data Type | Description            |
| ---------------- | --------- | ---------------------- |
| investor_id      | Text      | Unique investor ID     |
| transaction_date | Date      | Transaction date       |
| transaction_type | Text      | SIP/Lumpsum/Redemption |
| amount_inr       | Float     | Transaction amount     |

Source: Bluestock Dataset
