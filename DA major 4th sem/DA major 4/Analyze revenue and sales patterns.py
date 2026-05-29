import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("train.csv")

print(data.head())

# datset cleaning
data = data.dropna(subset=["Sales", "Order Date"])
data = data.drop_duplicates()

# date fix
data["Order Date"] = pd.to_datetime(data["Order Date"], format="%d/%m/%Y")

# Analysis 1: Sales over time 
data["YearMonth"] = data["Order Date"].dt.to_period("M")
monthly_sales = data.groupby("YearMonth")["Sales"].sum()

print("\nMonthly Sales:\n", monthly_sales)

plt.figure()
monthly_sales.plot()
plt.title("Sales Over Time")
plt.xlabel("Year-Month")
plt.ylabel("Sales")
plt.grid(True)
plt.show()


# Analysis 2: Category wise sales
category_sales = data.groupby("Category")["Sales"].sum().sort_values()

print("\nCategory Sales:\n", category_sales)

plt.figure()
category_sales.plot(kind="bar")
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.grid(True)
plt.show()


#Analysis 3: Top 5 products
product_sales = data.groupby("Product Name")["Sales"].sum()
top_products = product_sales.sort_values(ascending=False).head(5)

print("\nTop Products:\n", top_products)

plt.figure()
top_products.plot(kind="bar")
plt.title("Top 5 Products")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.grid(True)
plt.show()