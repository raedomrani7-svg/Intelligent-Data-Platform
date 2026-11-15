
import pandas as pd


def clean_data(data):

    print("Starting data cleaning...")

    # 1. Remove duplicate rows
    data = data.drop_duplicates()

    # 2. Handle missing values
    for column in data.columns:
        if pd.api.types.is_numeric_dtype(data[column]):
             data[column] = data[column].fillna(data[column].median())
        else:
             data[column] = data[column].fillna("Unknown")

    print("Data cleaning completed!")

    return data
