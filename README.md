# Sales Data Analysis & Forecasting Dashboard

![Python](https://img.shields.io/badge/Python-3.14-blue) ![Plotly](https://img.shields.io/badge/Plotly-Interactive-orange) ![SQL](https://img.shields.io/badge/SQL-SQLite-green) ![ML](https://img.shields.io/badge/ML-Forecasting-purple)

## Overview
End-to-end data analysis project analyzing **4 years of retail sales data (9,994 transactions)** to uncover business insights and forecast future revenue using machine learning.

Built with Python, SQL, and an interactive Plotly dashboard — combining data engineering, analytics, and visualization skills.

---

## Business Questions Answered
- Which product categories and regions drive the most revenue and profit?
- What are the seasonal sales patterns across 4 years?
- Which customer segments are most valuable?
- What will sales look like in the next 6 months?

---

## Key Business Insights

| Finding | Detail |
|---------|--------|
| Top category | Technology ($836K revenue, 17.4% profit margin) |
| Hidden issue | Furniture has $742K revenue but only 2.5% profit margin |
| Top region | West ($725K) — outperforms South by 85% |
| Best month | November peaks every year (pre-holiday surge) |
| Weakest month | January dips every year (post-holiday slowdown) |
| Top product | Canon imageCLASS 2200 Copier ($61K from just 5 orders) |
| Best margin | Paper sub-category at 43.4% profit margin |
| Forecast accuracy | 82.9% accuracy on 6-month holdout test |

---

## Forecasting Model
- **Algorithm:** Holt-Winters Exponential Smoothing
- **Training data:** 48 months (2014–2017)
- **Forecast horizon:** 6 months (Jan–Jun 2018)
- **Accuracy:** 82.9% (MAPE: 17.1%)
- **RMSE:** $18,273 per month

---

## Advanced SQL Analysis
Beyond basic queries, this project uses:
- **Window functions** — running totals with `SUM() OVER`
- **LAG functions** — year-over-year growth by category
- **RANK()** — customer segment revenue ranking
- **Profit margin calculations** — across regions, segments, sub-categories

---

## Tech Stack
| Tool | Purpose |
|------|---------|
| Python (Pandas, NumPy) | Data cleaning & analysis |
| SQLite + SQL | Advanced querying & aggregation |
| Statsmodels | Time-series forecasting |
| Plotly | Interactive dashboard |
| Matplotlib / Seaborn | Static EDA charts |
| Scikit-learn | Model evaluation metrics |
| Jupyter Notebooks | Analysis & storytelling |

---

## Project Structure

├── data/                  # Raw dataset (see below to download)
├── notebooks/
│   ├── 01_eda.ipynb       # Exploratory data analysis
│   └── 02_forecasting.ipynb # Forecasting model & evaluation
├── outputs/
│   ├── dashboard.html     # Interactive Plotly dashboard
│   └── *.png              # Static EDA charts
├── sql_analysis.py        # Advanced SQL queries
├── dashboard.py           # Interactive dashboard script
└── requirements.txt       # Dependencies

## Dataset
Download from Kaggle: https://www.kaggle.com/datasets/vivek468/superstore-dataset-final

Place the CSV file in the `data/` folder before running.

---

## How to Run

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/sales-forecasting-dashboard.git
cd sales-forecasting-dashboard

# Install dependencies
pip install -r requirements.txt

# Run SQL analysis
python3 sql_analysis.py

# Launch interactive dashboard
python3 dashboard.py
open outputs/dashboard.html

# Open Jupyter notebooks
jupyter notebook
```

---

## Business Recommendations
1. **Investigate Furniture margins** — high revenue but only 2.5% profit suggests heavy discounting
2. **Double down on Technology** — highest revenue AND healthy margins
3. **Target Central region** — significantly underperforms despite large geography
4. **Plan inventory for November** — consistent peak every year
5. **Promote in January/February** — counter the recurring seasonal dip