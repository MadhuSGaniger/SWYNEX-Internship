import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load The dataset
data=pd.read_csv("retail_sales_dirty_50000.csv")
"""print(data.head())
print(data.tail())
print(" Before cleaning - Number of data:",len(data))

# Check for missing values
print(data.isnull().sum())

# Check for duplicates
print(data.duplicated().sum())"""

# Drop duplicates
"""print(data.drop_duplicates(inplace=True))
print(data.duplicated().sum())"""

"""print(data.isnull().sum())
print(data.info())"""

# order date fill null values with mode
data["Order_Date"] = pd.to_datetime(data["Order_Date"], errors="coerce")
print("Missing or invalid dates:", data["Order_Date"].isna().sum())

data = data.dropna(subset=["Order_Date"]).copy()
print("Missing or invalid dates after dropping:", data["Order_Date"].isna().sum())

# fill null value in Customer_id UNKNOWN

data["Customer_ID"] = data["Customer_ID"].astype("string").fillna("UNKNOWN")
print("Missing Customer_ID after filling:", data["Customer_ID"].isna().sum())

# Drop rows with missing Product_Name or Quantity
data = data.dropna(subset=["Product_Name", "Quantity"])
print(data[["Product_Name", "Quantity"]].isna().sum())

# Fill missing values in Unit_Price_INR, Discount_Rate, and Region with median or mode
data["Unit_Price_INR"] = pd.to_numeric(data["Unit_Price_INR"], errors="coerce")
data["Discount_Rate"] = pd.to_numeric(data["Discount_Rate"], errors="coerce")

data["Unit_Price_INR"] = data["Unit_Price_INR"].fillna(data["Unit_Price_INR"].median())
data["Discount_Rate"] = data["Discount_Rate"].fillna(data["Discount_Rate"].median())

data["Region"] = data["Region"].fillna(data["Region"].mode()[0])

# Check missing values before cleaning
columns = [
    "Sales_Channel",
    "Payment_Method",
    "Order_Status",
    "Total_Amount_INR"
]

print("Missing values before cleaning:")
print(data[columns].isna().sum())

# Remove rows with missing values in the selected columns
data = data.dropna(subset=columns)

# Check missing values after cleaning
print("\nMissing values after cleaning:")
print(data[columns].isna().sum())

# Display remaining rows
print("\nRemaining rows:", len(data))


print(" After cleaning - Number of data:",len(data))

print(data.isnull().sum())

data.to_csv("cleaned_retail_data.csv", index=False)

