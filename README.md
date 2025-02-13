

# etl-nyc-taxi-trip 🚀

## 📌 Project Overview
This project demonstrates an ETL (Extract, Transform, Load) pipeline using **Azure Data Factory, SQL, and Python** to automate data integration and transformation processes.

# 🚖 ETL Pipeline for NYC Taxi Trip Data

## 📌 Overview
This project demonstrates an **ETL pipeline** that processes the **New York City Taxi Trip Duration** dataset from Kaggle. It extracts, cleans, transforms, and loads the data into **Azure Blob Storage**. The project also includes **data visualization** to analyze trip durations and trends.

## 🛠️ Tools & Technologies
- **Python**: Data Processing & Analysis
- **Pandas**: Data Manipulation
- **Azure Blob Storage**: Cloud Storage for Processed Data
- **Matplotlib & Seaborn**: Data Visualization
- **Jupyter Notebook**: Data Exploration

## 📊 Data Visualizations
**Trip Duration Distribution**  
📌 Shows how trip durations are spread across the dataset.  
![Trip Duration Distribution](images/trip_duration_distribution.png)  

**Trip Duration by Hour of Day**  
📌 Analyzes how trip duration varies by the time of the day.  
![Trip Duration by Hour](images/trip_duration_by_hour.png)  

**Number of Trips by Day of the Week**  
📌 Displays the volume of taxi trips for each day of the week.  
![Trips by Day of Week](images/trips_by_day_of_week.png)  

## 🚀 How to Run
1. **Install dependencies**:
   ```bash
   pip install pandas azure-storage-blob matplotlib seaborn
