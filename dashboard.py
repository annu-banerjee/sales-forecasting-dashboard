import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
from statsmodels.tsa.holtwinters import ExponentialSmoothing

# Load and prepare data
df = pd.read_csv('data/Sample - Superstore.csv', encoding='latin-1')
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Month'] = df['Order Date'].dt.to_period('M').dt.to_timestamp()
df['Year'] = df['Order Date'].dt.year

# Prepare all datasets
monthly_sales = df.groupby('Month')['Sales'].sum().reset_index()
category_sales = df.groupby('Category')['Sales'].sum().reset_index()
regional_sales = df.groupby('Region').agg({'Sales':'sum','Profit':'sum'}).reset_index()
regional_sales['Profit_Margin'] = (regional_sales['Profit']/regional_sales['Sales']*100).round(1)
top_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10).reset_index()
top_products['Short Name'] = top_products['Product Name'].str[:35] + '...'
segment_data = df.groupby('Segment').agg({'Sales':'sum','Profit':'sum'}).reset_index()
subcategory = df.groupby('Sub-Category').agg({'Sales':'sum','Profit':'sum'}).reset_index()
subcategory['Profit_Margin'] = (subcategory['Profit']/subcategory['Sales']*100).round(1)
subcategory_sorted = subcategory.sort_values('Profit_Margin', ascending=True)

# Forecast
monthly_ts = monthly_sales.set_index('Month')['Sales']
model = ExponentialSmoothing(monthly_ts, trend='add', seasonal='add', seasonal_periods=12)
fit = model.fit()
forecast_index = pd.date_range(start='2018-01-01', periods=6, freq='MS')
forecast_values = fit.forecast(6)

# Build dashboard
fig = make_subplots(
    rows=4, cols=2,
    subplot_titles=(
        'Monthly Sales Trend & Forecast', 'Sales by Category',
        'Regional Performance', 'Customer Segment Analysis',
        'Top 10 Products by Revenue', '',
        'Sub-Category Profit Margin', ''
    ),
    vertical_spacing=0.16,
    horizontal_spacing=0.12,
    specs=[
        [{"colspan": 1}, {"colspan": 1}],
        [{"colspan": 1}, {"colspan": 1}],
        [{"colspan": 2}, None],
        [{"colspan": 2}, None]
    ]
)

# Chart 1: Monthly trend + forecast
fig.add_trace(go.Scatter(
    x=monthly_sales['Month'], y=monthly_sales['Sales'],
    name='Actual Sales', line=dict(color='#2196F3', width=2),
    fill='tozeroy', fillcolor='rgba(33,150,243,0.1)'
), row=1, col=1)

fig.add_trace(go.Scatter(
    x=forecast_index, y=forecast_values,
    name='Forecast', line=dict(color='#FF9800', width=2, dash='dash'),
    marker=dict(size=6)
), row=1, col=1)

# Chart 2: Sales by category
fig.add_trace(go.Bar(
    x=category_sales['Category'], y=category_sales['Sales'],
    name='Category Sales',
    marker_color=['#2196F3','#4CAF50','#FF9800']
), row=1, col=2)

# Chart 3: Regional performance
fig.add_trace(go.Bar(
    x=regional_sales['Region'], y=regional_sales['Sales'],
    name='Regional Sales', marker_color='#2196F3'
), row=2, col=1)

# Chart 4: Segment analysis
fig.add_trace(go.Bar(
    x=segment_data['Segment'], y=segment_data['Sales'],
    name='Segment Sales', marker_color='#9C27B0'
), row=2, col=2)

# Chart 5: Top 10 products (full width)
fig.add_trace(go.Bar(
    x=top_products['Sales'],
    y=top_products['Short Name'],
    orientation='h', name='Product Revenue',
    marker_color='#4CAF50',
    hovertext=top_products['Product Name'],
    hoverinfo='text+x'
), row=3, col=1)

# Chart 6: Sub-category profit margin (full width)
fig.add_trace(go.Bar(
    x=subcategory_sorted['Profit_Margin'],
    y=subcategory_sorted['Sub-Category'],
    orientation='h', name='Profit Margin %',
    marker_color='#00BCD4'
), row=4, col=1)

# Layout
fig.update_layout(
    title=dict(text='Sales Analytics & Forecasting Dashboard', font=dict(size=24)),
    height=2000,
    showlegend=False,
    template='plotly_white',
    margin=dict(t=80, b=80, l=80, r=80)
)

fig.write_html('outputs/dashboard.html')
print("Dashboard saved!")