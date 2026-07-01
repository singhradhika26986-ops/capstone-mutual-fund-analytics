
import pandas as pd

def recommend_funds(df, risk_level):
    return (
        df[df["risk_category"].str.upper() == risk_level.upper()]
        .sort_values("Sharpe Ratio", ascending=False)
        .head(3)
    )
