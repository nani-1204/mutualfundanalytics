# Mutual Fund Analytics

Bluestock Fintech Capstone Internship Project

## Project Overview

This project analyzes mutual fund data using Python, Pandas, SQL, and SQLite. The objective is to build a complete analytics pipeline covering data ingestion, cleaning, validation, database design, and analytical reporting.

## Technologies Used

* Python
* Pandas
* NumPy
* SQLAlchemy
* SQLite
* Requests
* Git
* GitHub
* VS Code

---

## Project Structure

```text
mutualfundanalytics/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── reports/
│   └── data_dictionary.md
│
├── sql/
│   ├── schema.sql
│   └── queries.sql
│
├── bluestock_mf.db
├── data_ingestion.py
├── data_cleaning.py
├── load_sqlite.py
├── test_queries.py
├── live_nav_fetch.py
├── fund_master_analysis.py
├── amfi_validation.py
└── requirements.txt
```

---

## Day 1 Deliverables

### Data Ingestion

* Loaded 10 mutual fund datasets using Pandas
* Performed data profiling using:

  * Shape
  * Data Types
  * Head Records
* Checked missing values and duplicates

### Live NAV API Integration

Fetched live NAV data from MFAPI:

* SBI Bluechip Fund
* ICICI Bluechip Fund
* Nippon Large Cap Fund
* Axis Bluechip Fund
* Kotak Bluechip Fund

### Data Validation

* Explored fund categories and risk grades
* Validated AMFI codes against NAV history
* Generated data quality report

---

## Day 2 Deliverables

### Data Cleaning

* Converted date fields to datetime
* Removed duplicate records
* Validated NAV values
* Standardized transaction types
* Validated expense ratios

### SQLite Database

Created star-schema inspired database:

Tables:

* dim_fund
* fact_nav
* fact_transactions
* fact_performance
* fact_aum

### SQL Analytics

Implemented analytical SQL queries including:

* Top funds by AUM
* Average NAV trends
* Transaction analysis
* Expense ratio analysis
* Risk distribution analysis

### Documentation

* Data Dictionary
* Database Schema
* SQL Query Library

---

## Key Insights

* Successfully processed 46,000+ NAV records
* Analyzed 32,000+ investor transactions
* Validated all AMFI scheme codes
* Built SQLite analytical database
* Generated reusable SQL reporting layer

---

## Future Enhancements

* Interactive Power BI Dashboard
* Streamlit Web Application
* Portfolio Risk Analytics
* Fund Performance Benchmarking
* Automated Data Refresh Pipeline

---

## Author

Devi Sri Prasad Asadi

Bluestock Fintech Capstone Internship Project
