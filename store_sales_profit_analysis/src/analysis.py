import pandas as pd

# Load dataset
df = pd.read_csv("data/store_sales.csv", encoding="latin1")

# Show first 5 rows
print(df.head())

# Show dataset information
print(df.info())
# Check missing values
print("\nMissing values in each column:")
print(df.isnull().sum())
# Total Sales and Profit
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()

print("\nTotal Sales:", total_sales)
print("Total Profit:", total_profit)

# Sales by Category
sales_by_category = df.groupby("Category")["Sales"].sum()
print("\nSales by Category:")
print(sales_by_category)
import matplotlib.pyplot as plt

# Profit by Category
profit_by_category = df.groupby("Category")["Profit"].sum()

print("\nProfit by Category:")
print(profit_by_category)

# Bar chart
profit_by_category.plot(kind="bar", title="Profit by Category")
plt.ylabel("Profit")
plt.xlabel("Category")
plt.tight_layout()
plt.show()
