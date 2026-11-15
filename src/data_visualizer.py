import matplotlib.pyplot as plt


def plot_revenue_by_region(data):

    print("Creating revenue by region chart...")

    # 1. Calculate revenue for each region
    revenue = data.groupby("Region")["Revenue"].sum()

    # 2. Draw the bar chart
    revenue.plot(kind="bar", color="steelblue")
    plt.title("Revenue by Region")
    plt.xlabel("Region")
    plt.ylabel("Revenue")
    plt.tight_layout()

    # 3. Save the chart in the reports folder
    plt.savefig("reports/revenue_by_region.png")
    plt.close()

    print("Chart saved!")


def plot_revenue_by_category(data):

    print("Creating revenue by category chart...")

    # 1. Calculate revenue for each category
    revenue = data.groupby("Category")["Revenue"].sum()

    # 2. Draw the pie chart
    revenue.plot(kind="pie", autopct="%1.1f%%")
    plt.title("Revenue by Category")
    plt.ylabel("")
    plt.tight_layout()

    # 3. Save the chart in the reports folder
    plt.savefig("reports/revenue_by_category.png")
    plt.close()

    print("Chart saved!")