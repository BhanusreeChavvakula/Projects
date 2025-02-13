import pandas as pd
from azure.storage.blob import BlobServiceClient

# Load raw data
df = pd.read_csv("data/raw_sales_data.csv")

# Data Cleaning & Transformation
df["TotalPrice"] = df["Quantity"] * df["Price"]
df["Date"] = pd.to_datetime(df["Date"])

# Save processed data
df.to_csv("data/processed_sales_data.csv", index=False)
print("✅ Data transformation completed!")

# Upload to Azure Blob Storage
CONNECTION_STRING = "your_connection_string_here"
blob_service_client = BlobServiceClient.from_connection_string(CONNECTION_STRING)

container_name = "sales-data"
blob_client = blob_service_client.get_blob_client(container=container_name, blob="processed_sales_data.csv")

with open("data/processed_sales_data.csv", "rb") as data:
    blob_client.upload_blob(data, overwrite=True)

print("✅ File uploaded to Azure Blob Storage!")
