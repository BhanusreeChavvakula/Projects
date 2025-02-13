import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load processed data
df = pd.read_csv("data/processed_sales_data.csv")

# Visualization: Sales by Product
plt.figure(figsize=(10, 6))
sns.barplot(x="Product", y="TotalPrice", data=df, palette="viridis")
plt.xticks(rotation=45)
plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.savefig("images/sales_by_product.png")
plt.show()
