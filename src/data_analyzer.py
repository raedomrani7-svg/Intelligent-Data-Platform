import pandas as pd


def analyze_data(data):

    print("Starting data analysis...")

    # 1. Convert the Date column to a real date type
    data["Date"] = pd.to_datetime(data["Date"])

    # 2. Create the Revenue column
    data["Revenue"] = data["Quantity"] * data["Price"]

    # 3. Revenue by region
    print("Revenue by region:")
    print(data.groupby("Region")["Revenue"].sum())

    # 4. Revenue by category
    print("Revenue by category:")
    print(data.groupby("Category")["Revenue"].sum())

    print("Data analysis completed!")

    return data