import pandas as pd

from src.data_cleaner import clean_data
from src.data_analyzer import analyze_data


def test_clean_data_removes_duplicates():

    # 1. Create a small table with a duplicate row
    data = pd.DataFrame({
        "Product": ["Laptop", "Laptop", "Mouse"],
        "Price": [800, 800, 20]
    })

    # 2. Clean it
    result = clean_data(data)

    # 3. Check: only 2 rows should remain
    assert len(result) == 2


def test_clean_data_fills_missing_values():

    # 1. Create a table with missing values
    data = pd.DataFrame({
        "Product": ["Laptop", None, "Mouse"],
        "Price": [800.0, None, 20.0]
    })

    # 2. Clean it
    result = clean_data(data)

    # 3. Check: no missing value should remain
    assert result.isnull().sum().sum() == 0


def test_analyze_data_creates_revenue():

    # 1. Create a small sales table
    data = pd.DataFrame({
        "Date": ["2026-01-01", "2026-01-02"],
        "Category": ["Electronics", "Accessories"],
        "Quantity": [2, 5],
        "Price": [800, 20],
        "Region": ["Tunis", "Ariana"]
    })

    # 2. Analyze it
    result = analyze_data(data)

    # 3. Check: Revenue = Quantity * Price
    assert result["Revenue"].tolist() == [1600, 100]