# 🛒 Retail Sales Analysis & Customer Segmentation

## 📌 Project Overview
This project analyzes retail transaction data to uncover sales trends, top products, key customers, geographic performance, and customer segmentation using **RFM (Recency, Frequency, Monetary)** analysis.  

The workflow includes:
- Data cleaning & preprocessing  
- Exploratory data analysis (EDA)  
- Visualization of sales insights  
- Customer segmentation for marketing strategies  

---

## 📂 Dataset
- **File:** `data.csv`  
- **Encoding:** `latin1` (ISO-8859-1)  
- **Columns:** `InvoiceNo`, `StockCode`, `Description`, `Quantity`, `InvoiceDate`, `UnitPrice`, `CustomerID`, `Country`  

---

## ⚙️ Steps Performed

```python
# 1️⃣ Load dataset
df = pd.read_csv("data.csv", encoding='latin1')

# 2️⃣ Data cleaning
df.dropna(inplace=True)                    # Remove nulls
df.drop_duplicates(inplace=True)           # Remove duplicates
df = df[(df['Quantity'] > 0) & (df['UnitPrice'] > 0)]  # Remove invalid values

# 3️⃣ Feature engineering
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
df['TotalPrice'] = df['Quantity'] * df['UnitPrice']
df['Year'] = df['InvoiceDate'].dt.year
df['Month'] = df['InvoiceDate'].dt.month
df['Week'] = df['InvoiceDate'].dt.isocalendar().week
df['Day'] = df['InvoiceDate'].dt.day

# 4️⃣ Exploratory Data Analysis (EDA)
# - Overall sales trend
# - Top 10 most sold products
# - Top 10 biggest customers
# - Sales by country

# 5️⃣ RFM Analysis
# Calculate Recency, Frequency, Monetary
# Assign RFM scores and segment customers
```
##  📊 Key Insights
1. Overall Sales Trend

Shows fluctuations in daily sales. Useful for identifying seasonal peaks and slow periods.
