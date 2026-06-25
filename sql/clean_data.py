import pandas as pd
import os

raw_folder = "data/raw"
processed_folder = "data/processed"

os.makedirs(processed_folder, exist_ok=True)

files = [
    "01_fund_master.csv",
    "02_nav_history.csv",
    "03_aum_by_fund_house.csv",
    "04_monthly_sip_inflows.csv",
    "05_category_inflows.csv",
    "06_industry_folio_count.csv",
    "07_scheme_performance.csv",
    "08_investor_transactions.csv",
    "09_portfolio_holdings.csv",
    "10_benchmark_indices.csv"
]

for file in files:
    path = os.path.join(raw_folder, file)

    if os.path.exists(path):
        df = pd.read_csv(path)

        # Basic Cleaning
        df.drop_duplicates(inplace=True)
        df.columns = df.columns.str.strip()

        for col in df.select_dtypes(include="object").columns:
            df[col] = df[col].astype(str).str.strip()

        df.fillna("", inplace=True)

        output_name = file.replace(".csv", "_clean.csv")
        output_path = os.path.join(processed_folder, output_name)

        df.to_csv(output_path, index=False)
        print(f"Saved: {output_name}")

print("All cleaned CSV files created successfully!")