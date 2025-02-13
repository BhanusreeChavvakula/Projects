import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load processed data
df = pd.read_csv("../data/processed_sales_data.csv")

# Visualization 1: Trip Duration Distribution
plt.figure(figsize=(10, 6))
sns.histplot(df['TotalPrice'], bins=50, kde=True, color="blue")
plt.title("Trip Duration Distribution")
plt.xlabel("Trip Duration (seconds)")
plt.ylabel("Frequency")
plt.savefig("../images/trip_duration_distribution.png")
plt.show()

# Visualization 2: Trip Duration by Hour
plt.figure(figsize=(12, 6))
sns.boxplot(x=df['Quantity'], y=df['TotalPrice'], palette="coolwarm")
plt.title("Trip Duration by Hour of Day")
plt.xlabel("Quantity")
plt.ylabel("Total Price")
plt.savefig("../images/trip_duration_by_hour.png")
plt.show()

# Visualization 3: Number of Trips by Day
plt.figure(figsize=(10, 5))
sns.countplot(x=df['Product'], data=df, palette="viridis")
plt.title("Number of Trips by Product")
plt.xlabel("Product")
plt.ylabel("Number of Trips")
plt.savefig("../images/trips_by_day_of_week.png")
plt.show()
