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

```python
# After unzipping
import pandas as pd
df = pd.read_csv("data.csv", encoding='latin1')
