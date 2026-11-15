from src.data_loader import load_data
from src.data_cleaner import clean_data
from src.data_analyzer import analyze_data
from src.data_visualizer import plot_revenue_by_region, plot_revenue_by_category
from models.sales_model import train_model, predict_revenue
from dashboard.dashboard_builder import build_dashboard

if __name__ == "__main__":

    # 1. Load the data
    data = load_data("data/raw/sales.csv")

    if data is not None:

        # 2. Clean the data
        data = clean_data(data)

        # 3. Analyze the data
        data = analyze_data(data)

        # 4. Create the charts
        plot_revenue_by_region(data)
        plot_revenue_by_category(data)

        # 5. Train the model and predict
        model = train_model(data)
        prediction = predict_revenue(model, 9)
        print("Predicted revenue for day 9:", round(prediction, 2))

        # 6. Build the dashboard
        build_dashboard(data)

        # 7. Save the clean data
        data.to_csv("data/processed/sales_clean.csv", index=False)
        print("Clean data saved!")