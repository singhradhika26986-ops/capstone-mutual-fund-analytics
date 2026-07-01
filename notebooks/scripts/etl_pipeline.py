import pandas as pd
import sqlite3
import os

# Database Connection
conn = sqlite3.connect("mutual_fund.db")
cursor = conn.cursor()

with open("schema.sql", "r") as f:
    cursor.executescript(f.read())

conn.commit()
# CSV Files
files = {
    "01_fund_master": "data/raw/01_fund_master.csv",
    "02_nav_history": "data/raw/02_nav_history.csv",
    "03_aum_by_fund_house": "data/raw/03_aum_by_fund_house.csv",
    "04_monthly_sip_inflows": "data/raw/04_monthly_sip_inflows.csv",
    "05_category_inflows": "data/raw/05_category_inflows.csv",
    "06_industry_folio_count": "data/raw/06_industry_folio_count.csv",
    "07_scheme_performance": "data/raw/07_scheme_performance.csv",
    "08_investor_transactions": "data/raw/08_investor_transactions.csv",
    "09_portfolio_holdings": "data/raw/09_portfolio_holdings.csv",
    "10_benchmark_indices": "data/raw/10_benchmark_indices.csv"
}

for table_name, file_path in files.items():

    if os.path.exists(file_path):

        df = pd.read_csv(file_path)

        df.to_sql(
            table_name,
            conn,
            if_exists="replace",
            index=False
        )

        print(f"{table_name} loaded successfully. Shape: {df.shape}")

    else:

        print(f"{file_path} not found.")

conn.close()

print("ETL Pipeline Completed Successfully.")