# 📊 E-commerce Sales Analysis with RFM Segmentation

This project presents a comprehensive analysis of e-commerce transaction data using Python. It includes data cleaning, feature engineering, visual insights, and customer segmentation based on the RFM (Recency, Frequency, Monetary) model.

---

## 📦 Dataset

The dataset contains historical transaction records from an online retail store. It includes:

- `InvoiceNo`: Unique invoice number
- `StockCode`: Product code
- `Description`: Product name
- `Quantity`: Number of items purchased
- `InvoiceDate`: Date of transaction
- `UnitPrice`: Price per item
- `CustomerID`: Unique customer identifier
- `Country`: Country of purchase

> 🔐 The dataset is provided as a compressed file: `data.zip`  
> Please unzip it before running the analysis.

## 🧹 Data Cleaning & Preparation

```python
import pandas as pd

# Load dataset
df = pd.read_csv("data.csv", encoding='latin1')

# Remove null and duplicate entries
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)

# Convert InvoiceDate to datetime format
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# Filter out rows with negative or zero Quantity and UnitPrice
df = df[(df['Quantity'] > 0) & (df['UnitPrice'] > 0)]

# Create TotalPrice column
df['TotalPrice'] = df['Quantity'] * df['UnitPrice']

# Extract time-based features
df['Year'] = df['InvoiceDate'].dt.year
df['Month'] = df['InvoiceDate'].dt.month
df['Week'] = df['InvoiceDate'].dt.isocalendar().week
df['Day'] = df['InvoiceDate'].dt.day
```
## 📈 Exploratory Data Analysis (EDA)

The following visualizations were created using Matplotlib and Seaborn:

- 📊 **Sales Trend Over Time**  
  Time series plot showing revenue growth

- 🛍️ **Top-Selling Products**  
  Bar chart of most purchased items

- 👥 **Top Customers by Spend**  
  Bar chart of highest paying customers

- 🌍 **Sales by Country**  
  Country-wise revenue comparison

## 🔍 RFM Segmentation

- **Recency**: Days since last purchase  
- **Frequency**: Number of purchases  
- **Monetary**: Total amount spent  
- Customers scored from 1–4 per metric using `qcut`  
- Segments: Loyal, Potential, At Risk, Lost  
- Final chart saved as `rfm_segments.png`

## 🛠️ Technologies Used

- Python: pandas, numpy  
- Visualization: matplotlib, seaborn  
- Segmentation: RFM scoring

## 🚀 How to Run

```bash
pip install -r requirements.txt
unzip data.zip
python main.py
```

### 🔹 Project Structure

```markdown
## 📂 Project Structure
e-commerce-analysis/
├── main.py
├── data.zip
├── README.md
├── requirements.txt
```

## 👤 Author

**Muxiddin**  
📍 Samarqand, Uzbekistan  
🔗 [My Portfolio](https://your-portfolio-link.com)  
📧 muxiddin@example.com
