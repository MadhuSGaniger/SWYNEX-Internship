import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load cleaned dataset
data = pd.read_csv("cleaned_retail_data.csv")
amounts = (
    data["Total_Amount_INR"]
    .astype("string")
    .str.replace(r"[₹,\s]", "", regex=True)
)
data["Total_Amount_INR"] = pd.to_numeric(amounts, errors="coerce")
invalid_amounts = data["Total_Amount_INR"].isna().sum()
print(f"\nRows with invalid sales amounts (excluded from sales analysis): {invalid_amounts}")
sales_data = data.dropna(subset=["Total_Amount_INR"]).copy()

# 2. Basic information
print("Dataset Shape:", data.shape)
print("\nDataset Information:")
data.info()

# 3. Statistical summary
print("\nStatistical Summary:")
print(data.describe())

# 4. Check missing values
print("\nMissing Values:")
print(data.isnull().sum())

# 5. Top 5 products
print("\nTop 5 Products:")
print(data["Product_Name"].value_counts().head(5))

# 6. Sales by region
print("\nSales by Region:")
print(sales_data.groupby("Region")["Total_Amount_INR"].sum().sort_values(ascending=False))

# 7. Sales by payment method
print("\nPayment Method Counts:")
print(data["Payment_Method"].value_counts())

# python
# 8. Monthly Sales Trend
sales_data["Order_Date"] = pd.to_datetime(sales_data["Order_Date"], errors="coerce")

sales_data["Month"] = sales_data["Order_Date"].dt.to_period("M")

monthly_sales = sales_data.groupby("Month")["Total_Amount_INR"].sum()

monthly_sales.plot(kind="line", marker="o", title="Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales (INR)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# 9. Sales by Region
sales_data.groupby("Region")["Total_Amount_INR"].sum().plot(kind="bar", title="Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales (INR)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# 10. Sales Amount Distribution and Outliers
sns.boxplot(x=sales_data["Total_Amount_INR"].dropna())
plt.title("Sales Amount Outliers")
plt.xlabel("Total Amount (INR)")
plt.tight_layout()
plt.show()


# 11. Correlation Between Numerical Columns
columns = ["Unit_Price_INR", "Discount_Rate", "Total_Amount_INR"]

sns.heatmap(sales_data[columns].corr(),annot=True,cmap="coolwarm",fmt=".2f")
plt.title("Correlation Between Sales Variables")
plt.tight_layout()
plt.show()

