import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


print("ANALYZE REVENUE AND SALES PATTERNS\n")


# DATA READING

data = pd.read_csv("train.csv")

print("\nDataset Loaded Successfully!\n")


# SHOW DATASET COLUMNS

print("Available Columns in Dataset:\n")
print(data.columns)


# DATA CLEANING

data = data.dropna(subset=["Sales", "Order Date"])
data = data.drop_duplicates()

# DATE FORMATTING

data["Order Date"] = pd.to_datetime(
    data["Order Date"],
    format="%d/%m/%Y"
)


# NUMPY STATISTICAL ANALYSIS

sales_array = np.array(data["Sales"])

print("\n Statistical Analysis ")
print("Average Sales :", np.mean(sales_array))
print("Maximum Sales :", np.max(sales_array))
print("Minimum Sales :", np.min(sales_array))
print("Standard Deviation :", np.std(sales_array))



# MENU SYSTEM


while True:

    print("\n")
   
    print("           MAIN MENU")
   

    print("1. Sales Over Time")
    print("2. Category Wise Sales")
    print("3. Top 5 Products")
    print("4. Region Wise Sales")
    print("5. Correlation Analysis")
    print("6. Exit")

    try:
        choice = int(input("\nEnter your choice : "))

     
        # ANALYSIS 1 : SALES OVER TIME
        if choice == 1:

            data["YearMonth"] = data["Order Date"].dt.to_period("M")

            monthly_sales = data.groupby(
                "YearMonth"
            )["Sales"].sum()

            print("\nMonthly Sales:\n")
            print(monthly_sales)

            plt.figure(figsize=(10, 5))

            monthly_sales.plot(marker='o')

            plt.title("Sales Over Time")
            plt.xlabel("Year-Month")
            plt.ylabel("Sales")

            plt.grid(True)

            plt.savefig("monthly_sales.png")

            plt.show()

           
            # MOVING AVERAGE TREND
            
            moving_avg = monthly_sales.rolling(
                window=3
            ).mean()

            plt.figure(figsize=(10, 5))

            plt.plot(
                monthly_sales.index.astype(str),
                monthly_sales.values,
                label="Original Sales",
                marker='o'
            )

            plt.plot(
                monthly_sales.index.astype(str),
                moving_avg.values,
                label="3-Month Moving Average",
                linewidth=3
            )

            plt.title("Sales Trend Analysis")
            plt.xlabel("Year-Month")
            plt.ylabel("Sales")

            plt.xticks(rotation=45)

            plt.legend()
            plt.grid(True)

            plt.tight_layout()

            plt.savefig("sales_trend_analysis.png")

            plt.show()

        
        # ANALYSIS 2 : CATEGORY SALES
       
        elif choice == 2:

            category_sales = (
                data.groupby("Category")["Sales"]
                .sum()
                .sort_values()
            )

            print("\nCategory Wise Sales:\n")
            print(category_sales)

            plt.figure(figsize=(8, 5))

            category_sales.plot(kind="bar")

            plt.title("Sales by Category")
            plt.xlabel("Category")
            plt.ylabel("Sales")

            plt.grid(True)

            plt.tight_layout()

            plt.savefig("category_sales.png")

            plt.show()

        
        # ANALYSIS 3 : TOP PRODUCTS
        
        elif choice == 3:

            product_sales = data.groupby(
                "Product Name"
            )["Sales"].sum()

            top_products = (
                product_sales
                .sort_values(ascending=False)
                .head(5)
            )

            print("\nTop 5 Products:\n")
            print(top_products)

            plt.figure(figsize=(10, 5))

            top_products.plot(kind="bar")

            plt.title("Top 5 Products")
            plt.xlabel("Product")
            plt.ylabel("Sales")

            plt.grid(True)

            plt.tight_layout()

            plt.savefig("top_products.png")

            plt.show()

        
        # ANALYSIS 4 : REGION SALES
        
        elif choice == 4:

            region_sales = data.groupby(
                "Region"
            )["Sales"].sum()

            print("\nRegion Wise Sales:\n")
            print(region_sales)

            plt.figure(figsize=(8, 5))

            region_sales.plot(kind="bar")

            plt.title("Region Wise Sales")
            plt.xlabel("Region")
            plt.ylabel("Sales")

            plt.grid(True)

            plt.tight_layout()

            plt.savefig("region_sales.png")

            plt.show()

        
        # ANALYSIS 5 : CORRELATION
        
        elif choice == 5:

            numeric_data = data.select_dtypes(
                include=np.number
            )

            correlation = numeric_data.corr()

            print("\nCorrelation Matrix:\n")
            print(correlation)

            plt.figure(figsize=(6, 5))

            plt.imshow(
                correlation,
                cmap="coolwarm"
            )

            plt.colorbar()

            plt.xticks(
                range(len(correlation.columns)),
                correlation.columns,
                rotation=45
            )

            plt.yticks(
                range(len(correlation.columns)),
                correlation.columns
            )

            plt.title("Correlation Heatmap")

            plt.tight_layout()

            plt.savefig("correlation_heatmap.png")

            plt.show()

        
        # EXIT
       
        elif choice == 6:

            print("\nExiting Program...")
            print("Thank You!")

            break

       
        # INVALID CHOICE
        
        else:

            print("\nInvalid Choice! Please try again.")

    except ValueError:

        print("\nPlease enter a valid number!")