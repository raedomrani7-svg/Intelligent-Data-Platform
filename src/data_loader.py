import pandas as pd

def load_data(file_path):
    try:
        # Read the CSV file
        data = pd.read_csv(file_path)

        print("Dataset loaded successfully!")

        # Display the first 5 rows
        print(data.head())

        return data

    except FileNotFoundError:
        print("Error: File not found!")
        return None

    except Exception as error:
        print("Unexpected error:", error)
        return None


# Test the function
if __name__ == "__main__":
    load_data("data/raw/sales.csv")