# 📊 ETL Pipeline Results and Visualizations

## ✅ Processed Data Preview
The following table displays a preview of the **processed data** after the ETL pipeline has cleaned and transformed the dataset.

| OrderID | Customer       | Product  | Quantity | Price | Date       | TotalPrice |
|---------|--------------|----------|---------|-------|------------|------------|
| 1001    | John Doe      | Laptop   | 1       | 1200  | 2024-02-10 | 1200       |
| 1002    | Jane Smith    | Mouse    | 2       | 25    | 2024-02-11 | 50         |
| 1003    | Emily Davis   | Keyboard | 1       | 75    | 2024-02-12 | 75         |
| 1004    | Michael Brown | Monitor  | 1       | 300   | 2024-02-13 | 300        |
| 1005    | David Wilson  | Phone    | 1       | 999   | 2024-02-14 | 999        |

📌 **Full Processed Data:** [Click here](../data/processed_sales_data.csv)

---

## 📊 Data Visualizations

### **1️⃣ Sales by Product**
This bar chart shows total sales revenue by product.

![Sales by Product](../images/sales_by_product.png)

### **2️⃣ Trip Duration Distribution**
This histogram visualizes the distribution of trip durations.

![Trip Duration Distribution](../images/trip_duration_distribution.png)

### **3️⃣ Trip Duration by Hour**
This box plot shows the variation in trip durations based on the hour of the day.

![Trip Duration by Hour](../images/trip_duration_by_hour.png)

---

## 🚀 How to View Results
1. Run the **ETL Pipeline Script** to generate processed data:
   ```bash
   python scripts/etl_pipeline.py
