def build_dashboard(data):

    print("Building the dashboard...")

    # 1. Calculate the key numbers
    total_revenue = data["Revenue"].sum()
    total_sales = len(data)
    best_region = data.groupby("Region")["Revenue"].sum().idxmax()

    # 2. Convert the table to HTML
    table_html = data.to_html(index=False)

    # 3. Build the HTML page
    html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Intelligent Data Platform</title>
</head>
<body style="font-family: Arial; margin: 40px; background: #f4f6f8;">

    <h1>Intelligent Data Platform</h1>

    <h2>Key numbers</h2>
    <p><b>Total revenue:</b> {total_revenue}</p>
    <p><b>Number of sales:</b> {total_sales}</p>
    <p><b>Best region:</b> {best_region}</p>

    <h2>Charts</h2>
    <img src="../reports/revenue_by_region.png" width="450">
    <img src="../reports/revenue_by_category.png" width="450">

    <h2>Data</h2>
    {table_html}

</body>
</html>"""

    # 4. Save the page in the dashboard folder
    with open("dashboard/dashboard.html", "w", encoding="utf-8") as file:
        file.write(html)

    print("Dashboard saved!")