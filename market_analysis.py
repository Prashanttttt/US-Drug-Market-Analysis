"""
US Diabetes Drug Market — Competitive Sales Analysis & Segment Performance (2018-2024)
----------------------------------------------------------------------------------------
Author: Prashant Kaushik

This script analyses competitive dynamics in the US diabetes drug market, comparing
GLP-1 injectables vs. oral drug classes, tracking individual drug trajectories
(Ozempic vs. Januvia), and calculating segment-level CAGR and market share shifts
to support portfolio prioritisation insights.

Outputs:
    - outputs/ozempic_vs_januvia_trend.png
    - outputs/market_share_by_class_2024.png
    - outputs/cagr_by_drug_class.png
    - outputs/summary_metrics.csv
"""

import pandas as pd
import matplotlib.pyplot as plt
import os

DATA_PATH = "../data/diabetes_drug_sales_2018_2024.csv"
OUTPUT_DIR = "../outputs"

os.makedirs(OUTPUT_DIR, exist_ok=True)


def load_data(path=DATA_PATH) -> pd.DataFrame:
    df = pd.read_csv(path)
    return df


def calculate_cagr(start_value, end_value, periods):
    if start_value <= 0:
        return None
    return ((end_value / start_value) ** (1 / periods) - 1) * 100


def ozempic_vs_januvia(df: pd.DataFrame):
    """Reproduces the headline finding: Ozempic $280M (2018) -> $18B (2024);
    Januvia declined ~65% over the same period."""
    subset = df[df["Drug"].isin(["Ozempic", "Januvia"])]
    pivot = subset.pivot(index="Year", columns="Drug", values="Sales_USD_Million")

    ozempic_growth = (pivot["Ozempic"].iloc[-1] / pivot["Ozempic"].iloc[0])
    januvia_decline = (
        (pivot["Januvia"].iloc[0] - pivot["Januvia"].iloc[-1]) / pivot["Januvia"].iloc[0]
    ) * 100

    print(f"Ozempic grew {ozempic_growth:.1f}x from 2018 to 2024 "
          f"(${pivot['Ozempic'].iloc[0]:.0f}M -> ${pivot['Ozempic'].iloc[-1]:.0f}M)")
    print(f"Januvia declined {januvia_decline:.1f}% from 2018 to 2024 "
          f"(${pivot['Januvia'].iloc[0]:.0f}M -> ${pivot['Januvia'].iloc[-1]:.0f}M)")

    ax = pivot.plot(marker="o", figsize=(8, 5), title="Ozempic vs Januvia: Sales Trend (2018-2024)")
    ax.set_ylabel("US Sales (USD Million)")
    ax.set_xlabel("Year")
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/ozempic_vs_januvia_trend.png", dpi=150)
    plt.close()

    return pivot


def market_share_by_class(df: pd.DataFrame, year=2024):
    """GLP-1 receptor agonists vs other drug classes — market share snapshot."""
    year_df = df[df["Year"] == year]
    by_class = year_df.groupby("Drug_Class")["Sales_USD_Million"].sum().sort_values(ascending=False)
    total = by_class.sum()
    share_pct = (by_class / total * 100).round(2)

    print(f"\nMarket share by drug class ({year}):")
    print(share_pct)

    fig, ax = plt.subplots(figsize=(7, 7))
    ax.pie(share_pct, labels=share_pct.index, autopct="%1.1f%%", startangle=90)
    ax.set_title(f"US Diabetes Drug Market Share by Class ({year})")
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/market_share_by_class_2024.png", dpi=150)
    plt.close()

    return share_pct


def cagr_by_class(df: pd.DataFrame, start_year=2018, end_year=2024):
    """Segment-level CAGR — highlights GLP-1 as fastest-growing class."""
    periods = end_year - start_year
    by_class = df.groupby(["Year", "Drug_Class"])["Sales_USD_Million"].sum().unstack()

    cagr_results = {}
    for drug_class in by_class.columns:
        start_val = by_class.loc[start_year, drug_class]
        end_val = by_class.loc[end_year, drug_class]
        cagr_results[drug_class] = calculate_cagr(start_val, end_val, periods)

    cagr_series = pd.Series(cagr_results).sort_values(ascending=False)
    print(f"\nCAGR by drug class ({start_year}-{end_year}):")
    print(cagr_series.round(2))

    fig, ax = plt.subplots(figsize=(8, 5))
    cagr_series.plot(kind="bar", ax=ax, color="teal")
    ax.set_ylabel("CAGR (%)")
    ax.set_title(f"CAGR by Drug Class ({start_year}-{end_year})")
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/cagr_by_drug_class.png", dpi=150)
    plt.close()

    return cagr_series


def prescription_vs_revenue_gap(df: pd.DataFrame, year=2024):
    """Highlights the Metformin paradox: leads prescriptions, trails revenue growth."""
    year_df = df[df["Year"] == year][["Drug", "Drug_Class", "Sales_USD_Million",
                                        "Market_Share_Pct", "Prescription_Share_Pct"]]
    year_df = year_df.sort_values("Prescription_Share_Pct", ascending=False)
    print(f"\nPrescription share vs revenue market share ({year}):")
    print(year_df.to_string(index=False))
    return year_df


def build_summary(df: pd.DataFrame):
    pivot = ozempic_vs_januvia(df)
    share = market_share_by_class(df)
    cagr = cagr_by_class(df)
    rx_gap = prescription_vs_revenue_gap(df)

    summary = pd.DataFrame({
        "Ozempic_2018_M": [pivot["Ozempic"].iloc[0]],
        "Ozempic_2024_M": [pivot["Ozempic"].iloc[-1]],
        "Januvia_2018_M": [pivot["Januvia"].iloc[0]],
        "Januvia_2024_M": [pivot["Januvia"].iloc[-1]],
        "GLP1_CAGR_Pct": [cagr.get("GLP-1 Receptor Agonist")],
        "Total_Market_2024_M": [df[df["Year"] == 2024]["Sales_USD_Million"].sum()],
    })
    summary.to_csv(f"{OUTPUT_DIR}/summary_metrics.csv", index=False)
    print(f"\nSummary metrics saved to {OUTPUT_DIR}/summary_metrics.csv")


if __name__ == "__main__":
    df = load_data()
    build_summary(df)
