# Sales Data Analysis & Forecasting Dashboard

## Overview
End-to-end data analysis project on a retail superstore dataset.
Includes exploratory data analysis, SQL querying, and time-series sales forecasting.

## Tech Stack
Python | Pandas | SQL (SQLite) | Matplotlib | Seaborn | Statsmodels

## Key Findings
- Technology category drives the highest revenue ($836K) and profit
- West region leads all regions in total revenue ($725K)
- Clear seasonal pattern — Q4 consistently peaks, January dips
- Forecasted 6-month sales trend shows continued seasonal growth into 2018

## Project Structure
├── data/               # Raw dataset (download from Kaggle link below)
├── notebooks/          # Jupyter notebooks (EDA + Forecasting)
├── outputs/            # Generated charts
├── sql_analysis.py     # SQL queries via Python
└── README.md

## Dataset
Download from Kaggle: https://www.kaggle.com/datasets/vivek468/superstore-dataset-final

## How to Run
pip install -r requirements.txt
jupyter notebook notebooks/01_eda.ipynb