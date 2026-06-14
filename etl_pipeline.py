import pandas as pd


def extract_data(file_path):
    """
    Extract raw sales data from CSV file.
    """
    print("Extracting data...")
    data = pd.read_csv(file_path)
    return data


def transform_data(data):
    """
    Clean and transform raw data.
    """
    print("Transforming data...")

    data = data.drop_duplicates()

    data["customer_name"] = data["customer_name"].str.title()
    data["product"] = data["product"].str.title()
    data["category"] = data["category"].str.title()
    data["region"] = data["region"].str.title()

    data["order_date"] = pd.to_datetime(data["order_date"])

    data["total_amount"] = data["quantity"] * data["price"]

    data["month"] = data["order_date"].dt.month
    data["year"] = data["order_date"].dt.year

    data = data[
        [
            "order_id",
            "customer_name",
            "product",
            "category",
            "quantity",
            "price",
            "total_amount",
            "order_date",
            "month",
            "year",
            "region"
        ]
    ]

    return data


def load_data(data, output_file):
    """
    Load cleaned data into a new CSV file.
    """
    print("Loading cleaned data...")
    data.to_csv(output_file, index=False)
    print(f"Cleaned data saved to {output_file}")


def run_etl_pipeline():
    input_file = "raw_sales_data.csv"
    output_file = "cleaned_sales_data.csv"

    raw_data = extract_data(input_file)
    cleaned_data = transform_data(raw_data)
    load_data(cleaned_data, output_file)

    print("ETL pipeline completed successfully!")


if __name__ == "__main__":
    run_etl_pipeline()
