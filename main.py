import pandas as pd
import numpy as np

# load dataset
df = pd.read_csv("data.csv", encoding='latin1')  # or encoding='ISO-8859-1'

# check for null values and clean
print("Null values:\n", df.isnull().sum())
df.dropna(inplace=True)

# check for duplicates and clean
print("Duplicate rows:", df.duplicated().sum())
df.drop_duplicates(inplace=True)

# Convert InvoiceDate to datetime format
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# Remove negative and zero values in Quantity and UnitPrice
df = df[(df['Quantity'] > 0) & (df['UnitPrice'] > 0)]

# add TotalPrice column
df['TotalPrice'] = df['Quantity'] * df['UnitPrice']

# extract year, month, week, day from InvoiceDate
df['Year'] = df['InvoiceDate'].dt.year
df['Month'] = df['InvoiceDate'].dt.month
df['Week'] = df['InvoiceDate'].dt.isocalendar().week
df['Day'] = df['InvoiceDate'].dt.day

import matplotlib.pyplot as plt
import seaborn as sns

# overall sales trend
sales_trend = df.groupby('InvoiceDate')['TotalPrice'].sum()
plt.figure(figsize=(12,6))
sales_trend.plot()
plt.title("overall sales trend")
plt.xlabel("Date")
plt.ylabel("Sales amount")
plt.grid(True)
plt.show()

# top 10 most sold products
top_products = df.groupby('Description')['Quantity'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(10,6))
sns.barplot(x=top_products.values, y=top_products.index, palette="viridis")
plt.title("Top 10 most sold products")
plt.xlabel("Quantity sold")
plt.ylabel("Product")
plt.show()

# top customers (by Customer ID)
top_customers = df.groupby('CustomerID')['TotalPrice'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(10,6))
sns.barplot(x=top_customers.values, y=top_customers.index, palette="magma")
plt.title("Top 10 Biggest Customers")
plt.xlabel("Total Spend")
plt.ylabel("CustomerID")
plt.show()

# sales by country
country_sales = df.groupby('Country')['TotalPrice'].sum().sort_values(ascending=False)
plt.figure(figsize=(12,6))
sns.barplot(x=country_sales.values, y=country_sales.index, palette="coolwarm")
plt.title("Sales by Country")
plt.xlabel("Total Sales")
plt.ylabel("Country")
plt.show()

# determine the latest date
latest_date = df['InvoiceDate'].max()

# calculate RFM metrics
rfm = df.groupby('CustomerID').agg({
    'InvoiceDate': lambda x: (latest_date - x.max()).days,
    'InvoiceNo': 'count',
    'TotalPrice': 'sum'
})
rfm.columns = ['Recency', 'Frequency', 'Monetary']

# add RFM scores
rfm['R_Score'] = pd.qcut(rfm['Recency'], 4, labels=[4,3,2,1])
rfm['F_Score'] = pd.qcut(rfm['Frequency'].rank(method='first'), 4, labels=[1,2,3,4])
rfm['M_Score'] = pd.qcut(rfm['Monetary'], 4, labels=[1,2,3,4])

# RFM segment 
rfm['RFM_Segment'] = rfm['R_Score'].astype(str) + rfm['F_Score'].astype(str) + rfm['M_Score'].astype(str)
rfm['RFM_Score'] = rfm[['R_Score','F_Score','M_Score']].sum(axis=1)

# define customer segments
def segment_customer(row):
    if row['RFM_Score'] >= 9:
        return 'Loyal Customer'
    elif row['RFM_Score'] >= 6:
        return 'Potential Loyalist'
    elif row['RFM_Score'] >= 3:
        return 'At Risk'
    else:
        return 'Lost'
    
rfm['Segment'] = rfm.apply(segment_customer, axis=1)

# distribution of customers by segments
plt.figure(figsize=(8,5))
sns.countplot(data=rfm, x='Segment', palette='Set2')
plt.title("Customer Distribution by RFM Segments")
plt.xlabel("Segment")
plt.ylabel("Number of Customers")
plt.xticks(rotation=45)
plt.show()
