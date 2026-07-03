# US Diabetes Drug Market — Competitive Sales Analysis & Segment Performance (2018–2024)

A market research project analysing competitive dynamics in the **$32.5B (2024) US diabetes drug market**, comparing GLP-1 injectables vs. oral drug classes, tracking individual drug trajectories, and quantifying segment-level growth to support portfolio prioritisation decisions.

## 🎯 Objective

Healthcare and pharma commercial teams need to understand *where growth is actually happening* in a therapeutic market — not just where prescription volume sits today. This project models that shift for the US diabetes drug landscape, using historical sales data (2018–2024) to answer:

- How has the GLP-1 injectable class reshaped the competitive landscape?
- Which legacy drug classes are losing share, and how fast?
- Where does prescription volume diverge from revenue growth — and what does that mean for portfolio strategy?

## 🔑 Key Findings

- **Ozempic** (GLP-1 receptor agonist) grew from **$280M (2018) to $18B (2024)** — a ~64x increase — while legacy **Januvia** (DPP-4 inhibitor) declined **65%** over the same period, signalling a major therapeutic class shift.
- **GLP-1 receptor agonists** are the top-performing drug class: **38.76% market share**, the fastest-growing segment, with a **CAGR of ~10.75% projected through 2030**.
- **Metformin** leads in prescription volume (**45–50% share**) but trails significantly in revenue growth — a classic high-volume/low-value dynamic with direct implications for portfolio prioritisation.
- SGLT2 inhibitors (e.g. Jardiance) are the second-fastest-growing class, indicating a broader shift toward newer mechanism-of-action drug classes over legacy oral therapies.

## 🧠 Methodology

1. **Data compilation** — Drug-level annual US sales (2018–2024) segmented by drug class (GLP-1 Receptor Agonist, DPP-4 Inhibitor, SGLT2 Inhibitor, Biguanide, Insulin) and administration route (injectable/oral).
2. **Trend analysis** — Year-over-year sales trajectories for headline drugs (Ozempic vs. Januvia).
3. **Segment performance** — Market share and CAGR calculated by drug class to identify winners/laggards.
4. **Volume vs. value analysis** — Cross-referencing prescription share against revenue share to surface the "high-volume, low-growth" vs. "low-volume, high-growth" divide.
5. **Visualisation** — Trend lines, market share breakdown, and CAGR comparison charts built in Python (pandas + matplotlib).

## 📁 Repository Structure

```
us-diabetes-drug-market-analysis/
│
├── data/
│   └── diabetes_drug_sales_2018_2024.csv     # Drug-level annual sales data
│
├── notebooks/
│   └── market_analysis.py                    # Main analysis script
│
├── outputs/
│   ├── ozempic_vs_januvia_trend.png
│   ├── market_share_by_class_2024.png
│   ├── cagr_by_drug_class.png
│   └── summary_metrics.csv
│
├── requirements.txt
└── README.md
```

## ⚙️ How to Run

```bash
git clone https://github.com/<your-username>/us-diabetes-drug-market-analysis.git
cd us-diabetes-drug-market-analysis
pip install -r requirements.txt
cd notebooks
python market_analysis.py
```

This regenerates all charts and the summary metrics file in `outputs/`.

## 🛠️ Tools & Skills Demonstrated

- **Market research & competitive intelligence:** segment sizing, CAGR analysis, competitive benchmarking
- **Data analysis:** Python (pandas), time-series trend analysis
- **Data visualisation:** matplotlib (trend lines, share-of-market, bar charts)
- **Commercial insight generation:** translating raw sales data into portfolio-prioritisation recommendations

## 📌 Note on Data

Figures are compiled and reconstructed from **publicly reported industry sources** (company earnings disclosures, IQVIA/market commentary, and diabetes drug market reports) to illustrate the analytical approach. This is an independent research project for portfolio/learning purposes and is not affiliated with or endorsed by any pharmaceutical company.

## 👤 Author

**Prashant Kaushik**
MSc Biotechnology & Business Management, University of Warwick
📧 prashantkaushikgzb@gmail.com

