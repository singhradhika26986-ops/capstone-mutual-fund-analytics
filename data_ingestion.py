import pandas as pd

print("Data Ingestion Started")

# Add your data loading logic here

print("Data Ingestion Completed")
import os

processed_path = "data/processed"
os.makedirs(processed_path, exist_ok=True)

fund_master.to_csv(f"{processed_path}/01_fund_master_clean.csv", index=False)
nav_history.to_csv(f"{processed_path}/02_nav_history_clean.csv", index=False)
aum.to_csv(f"{processed_path}/03_aum_by_fund_house_clean.csv", index=False)
sip.to_csv(f"{processed_path}/04_monthly_sip_inflows_clean.csv", index=False)
category.to_csv(f"{processed_path}/05_category_inflows_clean.csv", index=False)
folio.to_csv(f"{processed_path}/06_industry_folio_count_clean.csv", index=False)
performance.to_csv(f"{processed_path}/07_scheme_performance_clean.csv", index=False)
transactions.to_csv(f"{processed_path}/08_investor_transactions_clean.csv", index=False)
holdings.to_csv(f"{processed_path}/09_portfolio_holdings_clean.csv", index=False)
benchmark.to_csv(f"{processed_path}/10_benchmark_indices_clean.csv", index=False)

print("All cleaned CSVs saved successfully!")