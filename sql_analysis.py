import pandas as pd
import sqlite3

# Load data into SQLite
df = pd.read_csv('data/Sample - Superstore.csv', encoding='latin-1')
df['Order Date'] = pd.to_datetime(df['Order Date']).dt.strftime('%Y-%m-%d')
df['Ship Date'] = pd.to_datetime(df['Ship Date']).dt.strftime('%Y-%m-%d')
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

query4 = """
SELECT 
    strftime('%Y-%m', "Order Date") as Month,
    ROUND(SUM(Sales), 2) as Monthly_Sales,
    ROUND(SUM(SUM(Sales)) OVER (ORDER BY strftime('%Y-%m', "Order Date")), 2) as Running_Total
FROM sales
GROUP BY Month
ORDER BY Month;
"""
print("\nMonthly Sales with Running Total:")
print(pd.read_sql(query4, conn))

query5 = """
SELECT 
    Category,
    strftime('%Y', "Order Date") as Year,
    ROUND(SUM(Sales), 2) as Annual_Sales,
    ROUND(SUM(Sales) - LAG(SUM(Sales)) OVER (PARTITION BY Category ORDER BY strftime('%Y', "Order Date")), 2) as YoY_Growth
FROM sales
GROUP BY Category, Year
ORDER BY Category, Year;
"""
print("\nYear over Year Sales Growth by Category:")
print(pd.read_sql(query5, conn))

# Query 6 - Customer segment performance with ranking
query6 = """
SELECT 
    Segment,
    ROUND(SUM(Sales), 2) as Total_Sales,
    ROUND(SUM(Profit), 2) as Total_Profit,
    ROUND(SUM(Profit) * 100.0 / SUM(Sales), 2) as Profit_Margin_Pct,
    RANK() OVER (ORDER BY SUM(Sales) DESC) as Revenue_Rank
FROM sales
GROUP BY Segment;
"""
print("\nCustomer Segment Performance with Ranking:")
print(pd.read_sql(query6, conn))

# Query 7 - Top performing sub-categories with profit margin
query7 = """
SELECT 
    "Sub-Category",
    Category,
    ROUND(SUM(Sales), 2) as Total_Sales,
    ROUND(SUM(Profit), 2) as Total_Profit,
    ROUND(SUM(Profit) * 100.0 / SUM(Sales), 2) as Profit_Margin_Pct,
    RANK() OVER (ORDER BY SUM(Profit) DESC) as Profit_Rank
FROM sales
GROUP BY "Sub-Category", Category
ORDER BY Total_Profit DESC
LIMIT 10;
"""
print("\nTop 10 Sub-Categories by Profit with Margin:")
print(pd.read_sql(query7, conn))

conn.close()
print("\nDone!")