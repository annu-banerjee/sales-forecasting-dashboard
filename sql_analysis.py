import pandas as pd
import sqlite3

# Load data into SQLite
df = pd.read_csv('data/Sample - Superstore.csv', encoding='latin-1')
conn = sqlite3.connect('sales.db')
df.to_sql('sales', conn, if_exists='replace', index=False)

# Query 1 - Top 10 products by revenue
query1 = """
SELECT "Product Name", 
       ROUND(SUM(Sales), 2) as Total_Sales,
       COUNT(*) as Orders
FROM sales
GROUP BY "Product Name"
ORDER BY Total_Sales DESC
LIMIT 10;
"""
print("Top 10 Products by Revenue:")
print(pd.read_sql(query1, conn))

# Query 2 - Regional performance
query2 = """
SELECT Region, 
       ROUND(SUM(Sales), 2) as Revenue,
       ROUND(AVG(Profit), 2) as Avg_Profit
FROM sales
GROUP BY Region
ORDER BY Revenue DESC;
"""
print("\nRegional Performance:")
print(pd.read_sql(query2, conn))

# Query 3 - Sales by Category
query3 = """
SELECT Category,
       ROUND(SUM(Sales), 2) as Total_Sales,
       ROUND(SUM(Profit), 2) as Total_Profit
FROM sales
GROUP BY Category
ORDER BY Total_Sales DESC;
"""
print("\nSales by Category:")
print(pd.read_sql(query3, conn))

conn.close()
print("\nDone!")